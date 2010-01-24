# -*- coding: cp936 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,os

#BaiduRadio - by Robinttt 2009.

def Roots():
         url='http://list.mp3.baidu.com/radio/iframe.html'
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub(' ','',link)
         match=re.compile('</a><h3>(.+?)</h3>').findall(link) 
         for name in match:
                addDir(name,url,1,'')

def Lists(url,name):
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub(' ','',link)
         name1=name.replace('(','\(')
         name1=name1.replace(')','\)')
         name=re.sub('\((.+?)\)','',name)
         addDir('当前类别：'+name,'',20,'')
         match=re.compile('<h3>'+name1+'</h3>(.+?)</div></div>').findall(link) 
         match0=re.compile('<imgsrc="(.+?)"(.+?)<div><ahref="(.+?)">(.+?)</a>').findall(match[0]) 
         num=0
         for img1,tmp1,url1,name1 in match0:
                img1=img1.replace('./','http://list.mp3.baidu.com/radio/')
                if name1=='中国之声': url1='mms://211.89.225.104/cnr1?MTUjMCM='
                if name1=='音乐之声': url1='mms://211.89.225.104/cnr3?MTUjMCM='
                if url1.find('http://listen.rbc.cn/baidu')==-1 and url1.find('http://listen.bjradio.com.cn/baidu')==-1:
                        num=num+1
	                li=xbmcgui.ListItem(str(num)+'.'+name1,iconImage=os.getcwd()+'\\Default.tbn', thumbnailImage=img1)
	                li.setInfo(type="Music",infoLabels={"Title":name1})
	                xbmcplugin.addDirectoryItem(int(sys.argv[1]),url1,li)

         #北广网
         if name.find('北京')!=-1:
                req = urllib2.Request('http://listen.rbc.cn/baidu/')
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                link=re.sub('\r','',link)
                link=re.sub('\n','',link)
                link=re.sub('\t','',link)
                link=re.sub(' ','',link)
                match=re.compile('varaddrs=newArray\("","(.+?)"\);').findall(link)
                ids=match[0].split('","')
                match=re.compile('varstation=newArray\("","(.+?)"\);').findall(link)
                nms=match[0].split('","')
                for i in range(0,len(ids)):
                        num=num+1
	                li=xbmcgui.ListItem(str(num)+'.'+nms[i])
	                li.setInfo(type="Music",infoLabels={"Title":nms[i]})
	                xbmcplugin.addDirectoryItem(int(sys.argv[1]),'mms://alive.rbc.cn/'+ids[i],li)
                
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

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=os.getcwd()+'\\Default.tbn', thumbnailImage=iconimage)
        liz.setInfo( type="Music", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
  

params=get_params()
url=None
name=None
mode=None

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

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None:
        print ""
        Roots()

elif mode==1:
        print ""+url
        Lists(url,name) 

xbmcplugin.endOfDirectory(int(sys.argv[1]))
