#"""
#ListItem([label, label2, iconImage, thumbnailImage, path]) -- Creates a new ListItem.
# 
#label          : [opt] string or unicode - label1 text.
#label2         : [opt] string or unicode - label2 text.
#iconImage      : [opt] string - icon filename.
#thumbnailImage : [opt] string - thumbnail filename.
#path           : [opt] string or unicode - listitem's path.
#"""
import xml.dom.minidom,urllib,urllib2,re,xbmcplugin,xbmcgui,os,xbmc,string,sys,codecs

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addDir(name,url,mode,shsz,folder):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&shsz="+urllib.quote_plus(shsz)+"&name="+urllib.quote_plus(name)
        ok=True
        icon = "%s\\resources\\stock.png" % (os.getcwd())
        liz=xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz, isFolder=folder)
        return ok
        
def addLink(name,url,mode,shsz,folder,isZX=False):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&shsz="+urllib.quote_plus(shsz)+"&name="+urllib.quote_plus(name)
        ok=True
        icon = "%s\\resources\\stock.png" % (os.getcwd())
        detail = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=show_detail&shsz="+urllib.quote_plus(shsz)+"&name="+urllib.quote_plus(name)
        liz=xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
        if (isZX==True):
            u=u+"&zx=yes"
            detail = detail + "&zx=yes"
            sx = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=op_zx&shsz="+urllib.quote_plus(shsz)+"&name="+urllib.quote_plus(name)+"&zx=yes"
            cm = [ ( u'K线'.encode('utf8'), "XBMC.RunPlugin(%s)" % (u,) ,), ( u'详细信息'.encode('utf8'), "XBMC.RunPlugin(%s)" % (detail,), ),( u'自选移出'.encode('utf8'), "XBMC.RunPlugin(%s)" % (sx,), ) ]
        else:
            sx = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=op_zx&shsz="+urllib.quote_plus(shsz)+"&name="+urllib.quote_plus(name)+"&zx=no"
            cm = [ ( u'K线'.encode('utf8'), "XBMC.RunPlugin(%s)" % (u,) ,), ( u'详细信息'.encode('utf8'), "XBMC.RunPlugin(%s)" % (detail,), ) ,( u'加入自选'.encode('utf8'), "XBMC.RunPlugin(%s)" % (sx,), )]
        liz.addContextMenuItems(cm, replaceItems = True)
        
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz, isFolder=folder)
        return ok

class CustomLoader:
    def __init__(self, listFile):
        self.listFile = listFile
        self.listXML = None
        self.node = []
        self.currfeed = []
        self.hasXML = self.loadList()

    def loadList(self):
        try:
            f = open(self.listFile)
        except IOError:
            return False
        fl = f.read()
        f.close()
        try:
            self.listXML = xml.dom.minidom.parseString(fl)
        except:
            print "parse error"
            return False
        return True

    def getText(self, nodelist):
        rc = ""
        for node in nodelist.childNodes:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data.encode('utf8')
        return rc

    def getStockList(self):
        stocks = self.listXML.getElementsByTagName("stock")
        for stock in stocks:
            node = stock.getElementsByTagName("name")[0]
            self.currfeed.append(self.getText(node))
            node = stock.getElementsByTagName("id")[0]
            self.currfeed.append(self.getText(node))
            node = stock.getElementsByTagName("shsz")[0]
            self.currfeed.append(self.getText(node))
            
    def findNode(self, text):
        try:
            stocks = self.listXML.getElementsByTagName("stock")
        except:
            return False
        for stock in stocks:
            if(text  == self.getText(stock.getElementsByTagName("id")[0]).strip()):
               return True
        return False
     
    def delNode(self, text):
        if(text.strip() in self.currfeed):
            c = self.currfeed.index(text.strip())
            self.currfeed.remove(self.currfeed[c-1])
            self.currfeed.remove(self.currfeed[c-1])
            self.currfeed.remove(self.currfeed[c-1])
        self.rebuildXML()
        
    def rebuildXML(self):
        impl = xml.dom.minidom.getDOMImplementation()
        dom = impl.createDocument(None, 'MyStocks', None)
        root = dom.getElementsByTagName('MyStocks')[0]
        if(len(self.currfeed) > 0):
            for feed in range(len(self.currfeed)/3):
                self.addElement(dom,root,self.currfeed[feed*3+1],self.currfeed[feed*3+0],self.currfeed[feed*3+2])
        try:
              f=open(self.listFile, 'w')
        except:
              pass
        writer = codecs.lookup('utf-8')[3](f)
        dom.writexml(writer, encoding='utf-8')
        writer.close()
        f.close()  
    
    def addNode(self,tagname,value):
        tag = self.listXML.createElement(tagname)
        text = self.listXML.createTextNode(value)
        tag.appendChild(text)
        return tag
        
    def addElement(self, dom, root, id, name, shsz):
         node = dom.createElement('stock')
             
         item = dom.createElement('name')
         text = dom.createTextNode(unicode(name,'utf8'))
         item.appendChild(text)
         node.appendChild(item)
         
         item = dom.createElement('id')
         text = dom.createTextNode(id)
         item.appendChild(text)
         node.appendChild(item)
         
         item = dom.createElement('shsz')
         text = dom.createTextNode(shsz)
         item.appendChild(text)
         node.appendChild(item)
         
         root.appendChild(node)
         #print root.toxml()
         
         try:
              f=open(self.listFile, 'w')
         except:
              pass
         writer = codecs.lookup('utf-8')[3](f)
         dom.writexml(writer, encoding='utf-8')
         writer.close()
         f.close()  
         
    def newXML(self, id, name, shsz):
         if(self.hasXML == False):
             impl = xml.dom.minidom.getDOMImplementation()
             dom = impl.createDocument(None, 'MyStocks', None)
             root = dom.getElementsByTagName('MyStocks')[0]
             self.addElement(dom,root,id,name,shsz)
         else:
             if(self.findNode(id) == False):
                 dom = self.listXML
                 root = dom.getElementsByTagName('MyStocks')[0]
                 self.addElement(dom,root,id,name,shsz)