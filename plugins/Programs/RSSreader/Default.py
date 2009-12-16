import xml.dom.minidom,urllib,urllib2,re,xbmcplugin,xbmcgui,os,xbmc,string

# 
# Constants
#
__plugin__  = "RSSreader"
__author__  = "rabbitgg"
__url__     = "http://"
__date__    = "27 oct 2009"
__version__ = "0.31"


class GUI( xbmcgui.WindowXMLDialog ):
    # Constants
    ACTION_EXIT_SCRIPT = ( 9, 10, )

    #
    # Init
    #
    def __init__( self, *args, **kwargs ):
        
        # Show dialog window...
        xbmcgui.WindowXML.__init__( self )
        
        # File parameter
        self.title = kwargs[ "info" ]
        self.cont = kwargs[ "text" ]
        

    #
    # onInit handler
    #
    def onInit( self ):
        xbmcgui.lock()
        self.getControl( 4 ).setLabel("[B]" +self.title + "[/B]")
        self.getControl( 30 ).setText(self.cont)
        xbmcgui.unlock()
    
    #
    # onFocus handler
    #
    def onFocus( self, controlId ):
        pass

    #
    # onAction handler
    #
    def onAction( self, action ):
        #
        # Exit
        #
        if ( action in self.ACTION_EXIT_SCRIPT ):
            # File changed, save?
           
            # Close window...
            self.close()
        if ( action == 4 ):
            xbmc.executebuiltin('XBMC.PageDown(61)')
        if ( action == 3 ):
            xbmc.executebuiltin('XBMC.PageUp(61)')
            
    #
    # onClick handler
    #
    def onClick( self, controlId ):
        pass
        
class FeedListLoader:
    def __init__(self, listFile):
        self.listFile = listFile
        self.listXML = None
        self.node = []
        self.currfeed = []
        self.loadList()

    def loadList(self):
        try:
            f = open(self.listFile)
        except IOError:
            pass
        fl = f.read()
        f.close()
        #fl = fl.replace('&', 'amp;')
        #fl = fl.replace('=', 'apos;')
        #fl = fl.replace('apos;\"', '=\"')
        self.listXML = xml.dom.minidom.parseString(fl)

    def getText(self, nodelist):
        rc = ""
        for node in nodelist.childNodes:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data.encode('utf8')
        return rc

    def getFeedList(self):
        #currfeed = []
        #self.feedList=[]
        feeds = self.listXML.getElementsByTagName("feed")
        #print "fees length is %s" % str(len(feeds))
        for feed in feeds:
            node = feed.getElementsByTagName("name")[0]
            #print self.getText()
            self.currfeed.append(self.getText(node))
            node = feed.getElementsByTagName("link")[0]
            self.currfeed.append(self.getText(node))
            node = feed.getElementsByTagName("contextStart")[0]
            self.currfeed.append(self.getText(node))
            node = feed.getElementsByTagName("contextEnd")[0]
            self.currfeed.append(self.getText(node))
            try:
               node = feed.getElementsByTagName("thumb")[0]
            except:
               self.currfeed.append('')
            else:
               self.currfeed.append(self.getText(node))
        
def CATEGORIES():
        feedlist = FeedListLoader("%s\\%s" % (os.getcwd(),"feedlist.xml"))
        feedlist.getFeedList()
        for feed in range(len(feedlist.currfeed)/5):
            name = feedlist.currfeed[feed*5+0]
            url = feedlist.currfeed[feed*5+1]
            cstart = feedlist.currfeed[feed*5+2]
            cend = feedlist.currfeed[feed*5+3]
            thumbicon = feedlist.currfeed[feed*5+4]
            addDir(name, url, 1, cstart, cend, thumbicon, folder=True)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
                       
def INDEX(url,cstart,cend):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match0=re.sub('\r','',link)
        match0=re.sub('\n','',match0)
        match=re.compile('<item(.+?)</item>').findall(match0)
        for info in match:
                match1=re.compile('<!\[CDATA\[(.+?)\]\]>').findall(info)
                name=match1[0]
                match1=re.compile('<link>(.+?)</link>').findall(info)
                url=match1[0]
                addLink(name,url,2,cstart,cend)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def RSSLINKS(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match0=re.sub('\r','',link)
        match0=re.sub('\n','',match0)
        regExp = cstart+'(.+?)'+cend
        match=re.compile(regExp).findall(match0)
        
        if (len(match) > 0):
            cont=re.sub('</p>','\n', match[0])
            cont=re.sub('</P>','\n', cont)
            cont=re.sub('<style(.+?)</style>','', cont)
            cont=re.sub('<script(.+?)</script>','', cont)
            cont=re.sub('&nbsp;',' ', cont)
            cont=re.sub('\t',' ', cont)
            cont=re.sub('<.+?>','', cont)
            mydisplay = GUI( "RSSreader.xml", os.getcwd(), "default", info=name, text=cont)
            mydisplay.doModal()
            del mydisplay
        else:
            dialog = xbmcgui.Dialog()
            dialog.ok('出错了', ' 解析页面出错。 ')
                
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







def addDir(name,url,mode,cstart,cend,iconimage,folder):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&cstart="+urllib.quote_plus(cstart)+"&cend="+urllib.quote_plus(cend)
        ok=True
        icon = ""
        if (len(iconimage) == 0):
            icon = "DefaultFolder.png"
        else:
            icon = "%s\\resources\\thumb\\%s" % (os.getcwd(),iconimage)
        liz=xbmcgui.ListItem(name, iconImage=icon, thumbnailImage="")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz, isFolder=folder)
        return ok
        
def addLink(name,url,mode,cstart,cend):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&cstart="+urllib.quote_plus(cstart)+"&cend="+urllib.quote_plus(cend)
        ok=True
        icon="%s\\resources\\thumb\\item.png" % os.getcwd()
        liz=xbmcgui.ListItem(name, iconImage=icon, thumbnailImage="")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz, isFolder=False)
        return ok        
              
params=get_params()
url=None
name=None
mode=None
cstart=None
cend=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:
        cstart=urllib.unquote_plus(params["cstart"])
except:
        pass
try:
        cend=urllib.unquote_plus(params["cend"])
except:
        pass

#print "Mode: "+str(mode)
#print "URL: "+str(url)
#print "Name: "+str(name)
#print "Cstart:"+str(cstart)
#print "Cend:"+str(cend)

if mode==None or url==None or len(url)<1:
        #print ""
        CATEGORIES()
       
elif mode==1:
        #print ""+url
        INDEX(url,cstart,cend)
        
elif mode==2:
        #print ""+url
        RSSLINKS(url,name)




