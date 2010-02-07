# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,os

#OpenV - by Robinttt 2009.

def CATEGORIES():
         addDir(u'电影'.encode('utf8'),'http://hd.openv.com/index_list-3.html',1,'')
         addDir(u'电视剧'.encode('utf8'),'http://hd.openv.com/index_list-2.html',1,'')
         #addDir(u'电视节目'.encode('utf8'),'http://tv.openv.com/tv_all.php',1,'')
         #addDir(u'游戏'.encode('utf8'),'http://game.openv.com/',1,'')


def Channels(url,name):
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub(' ','',link)
         match=re.compile('<divclass="gyong_top">(.+?)</div>').findall(link)
         for i in range(1,len(match)):
                addDir(name+'>'+match[i],url,2,'')


def ChannelsA(url,name):
         name0=name.split('>')[1]
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub(' ','',link)
         match=re.compile('<divclass="gyong_top">'+name0+'</div>(.+?)</ul>').findall(link)
         match0=re.compile("javascript:window.open\('(.+?)'\)\"><a>(.+?)</a>").findall(match[0])
         for url1,name1 in match0:
                 addDir(name+'>'+name1,'http://hd.openv.com/'+url1,3,'')
         match0=re.compile('href="(.+?)"target="_blank">(.+?)</a>').findall(match[0])
         for url1,name1 in match0:
                 addDir(name+'>'+name1,'http://hd.openv.com/'+url1,3,'')



def ChannelsB(url,name):
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub(' ','',link)
         if name.find(u'首字母'.encode('utf8'))==-1:
                 match=re.compile('<atitle=""href="(.+?)"><span>'+u'按最新排序'.encode('utf8')+'</span>').findall(link)
                 addDir(name+'>'+u'最新'.encode('utf8'),'http://hd.openv.com/'+match[0],4,'')
                 match=re.compile('<atitle=""href="(.+?)"><span>'+u'按最热排序'.encode('utf8')+'</span>').findall(link)
                 addDir(name+'>'+u'最热'.encode('utf8'),'http://hd.openv.com/'+match[0],4,'')
         else:
                 addDir(u'当前位置：'.encode('utf8')+name,'',20,'')
                 match=re.compile('<divclass="zmpx_one">(.+?)</div></div>').findall(link)
                 match0=re.compile('href="(.+?)"(.+?)>(.+?)</a>').findall(match[0])
                 for i in range(0,len(match0)):
                         #addDir(str(i+1)+'.'+match0[i][2]+match0[i][0],'http://hd.openv.com/',3,'')
                         if match0[i][0].find('tv_show')==-1:
                                  ids=match0[i][0].split('-')
                                  id=ids[1].replace('.html','')
                                  addLink(str(i+1)+'.'+match0[i][2],'http://casting.openv.com/PLGS/plgs.php?pid='+id,5,'')
                         else:
                                  addDir(str(i+1)+'.'+match0[i][2],'http://hd.openv.com/'+match0[i][0],6,'')
        

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

         match=re.compile('<title>(.+?)</title>').findall(link)
         addDir(u'当前位置：'.encode('utf8')+match[0],'',20,'')

         match=re.compile('<divclass="img"><ahref="(.+?)"target="_hdplay"><img(.+?)="(.+?)"src="(.+?)"').findall(link)
         for i in range(0,len(match)):
                 if match[i][0].find('tv_show')==-1:
                          ids=match[i][0].split('-')
                          id=ids[1].replace('.html','')
                          addLink(str(i+1)+'.'+match[i][2],'http://casting.openv.com/PLGS/plgs.php?pid='+id,5,match[i][3])
                 else:
                          addDir(str(i+1)+'.'+match[i][2],'http://hd.openv.com/'+match[i][0],6,match[i][3])

         match=re.compile('<divclass="page">(.+?)</div>').findall(link)
         match0=re.compile('href="(.+?)">(.+?)</a>').findall(match[0])
         for url1,name1 in match0:
                 if url1.find('"class="nob')==-1:
                         addDir(u'第'.encode('utf8')+name1+u'页'.encode('utf8'),'http://hd.openv.com/'+url1,4,'')
                 else:
                         url1=url1.replace('"class="nob','')
                         addDir(name1,'http://hd.openv.com/'+url1,4,'')

def ListsA(url,name):
         names=name.split('.')
         name=names[1]

         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub(' ','',link)

         match=re.compile('<divclass="ct">(.+?)</ul>').findall(link)
         match0=re.compile('href="tv_play-(.+?).html">(.+?)</a>').findall(match[0])
         for i in range(0,len(match0)):
                addLink(name+u'【'.encode('utf8')+match0[i][1]+u'】'.encode('utf8'),'http://casting.openv.com/PLGS/plgs.php?pid='+match0[i][0],5,'')
         match0=re.compile('href="tv_play-(.+?).html"title="(.+?)"').findall(match[0])
         for i in range(0,len(match0)):
                if match0[i][0]!='__': addLink(match0[i][1],'http://casting.openv.com/PLGS/plgs.php?pid='+match0[i][0],5,'')

def PlayVideo(url,name):
	 if xbmcplugin.getSetting("dvdplayer") == "true":
		player_type = xbmc.PLAYER_CORE_DVDPLAYER
	 else:
		player_type = xbmc.PLAYER_CORE_MPLAYER

         playlist=xbmc.PlayList(1)
         playlist.clear()
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         match=re.compile('<flvpath>(.+?)</flvpath>').findall(link)
         for i in range(0,len(match)):
         	 listitem=xbmcgui.ListItem(name)
                 listitem.setInfo(type="Video",infoLabels={"Title":name})
                 playlist.add(match[i], listitem)

         xbmc.Player(player_type).play(playlist)
                
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


def addLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=os.getcwd()+'\\Default.tbn', thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=os.getcwd()+'\\Default.tbn', thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
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
        CATEGORIES()

elif mode==1:
        print ""+url
        Channels(url,name) 
 
elif mode==2:
        print ""+url
        ChannelsA(url,name)
      
elif mode==3:
        print ""+url
        ChannelsB(url,name)

elif mode==4:
        print ""+url
        Lists(url,name)

elif mode==5:
        print ""+url
        PlayVideo(url,name)

elif mode==6:
        print ""+url
        ListsA(url,name)

elif mode==7:
        print ""+url
        ListsB(url,name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

