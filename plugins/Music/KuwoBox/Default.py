# -*- coding: cp936 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,os

#TV DASH - by You 2008.

def Categories():
         addDir(u'榜单'.encode('utf8'),'http://yinyue.kuwo.cn/yy/billboard_index.htm',1,'')
         addDir(u'歌手'.encode('utf8'),'http://yinyue.kuwo.cn/yy/artist.htm',3,'')
         addDir(u'歌单'.encode('utf8'),'',9,'')

def ChannelsA(url,name):
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub('&nbsp;','',link)
         link=re.sub('&quot;','',link)
         link=re.sub(' ','',link)
         match=re.compile('<divclass="mp3Frame"(.+?)</div>').findall(link)
         match0=re.compile('href="(.+?)"(.+?)>(.+?)</a>').findall(match[0])       
         for url1,other,name1 in match0:
                addDir(name+'>'+name1,'http://yinyue.kuwo.cn'+url1,2,'')

def ListsA(url,name):
         addDir(u'当前位置：'.encode('utf8')+name,url,20,'')
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub('&nbsp;','',link)
         link=re.sub('&quot;','',link)
         link=re.sub(' ','',link)
         match=re.compile('id="musicList1">(.+?)</div>').findall(link)
         match0=re.compile('musicId="(.+?)">(.+?)</a>(.+?)title="(.+?)"').findall(match[0]) 
         listp=''
         listn=''
         lista='' 
         for i in range(0,len(match0)):
                listp=listp+'/'+match0[i][0]
                lista=lista+'/'+match0[i][0]
                addLink(str(i+1)+'.'+match0[i][1]+'('+match0[i][3]+')',match0[i][0],15,'')
                if (i+1)%25==0:
                        listp=listp+'/{'
                        listn=listn+u'播放 第'.encode('utf8')+str(i-23)+u'至'.encode('utf8')+str(i+1)+u'首'.encode('utf8')+'/{'
                if i+1==len(match0):
                        if (i+1)%25!=0:
                                listp=listp+'/{'
                                listn=listn+u'播放 第'.encode('utf8')+str(i+2-(i+1)%25)+u'至'.encode('utf8')+str(i+1)+u'首'.encode('utf8')+'/{'

         ids=listp.split('/{')
         nms=listn.split('/{')
         for i in range(0,len(ids)-1):
                addLink(nms[i],ids[i],15,'')

         addLink(u'播放 全部歌曲'.encode('utf8'),lista,15,'')


def ChannelsB(url,name):
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub('&nbsp;','',link)
         link=re.sub('&quot;','',link)
         link=re.sub(' ','',link)
         match=re.compile('<ulclass="songList">(.+?)</ul>').findall(link)
         match0=re.compile('href="(.+?)"(.+?)>(.+?)</a>').findall(match[0])       
         for url1,other,name1 in match0:
                addDir(name+'>'+name1,'http://yinyue.kuwo.cn'+url1,4,'')


def ChannelsB1(url,name):
         addDir(name+'>'+u' 热门'.encode('utf8'),url,5,'')
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         match=re.compile('<a class="disp_block t_black_14 font_b pdl8"(.+?)">(.+?)</a>').findall(link)
         for other,name1 in match:
                addDir(name+'>'+name1,url,5,'')

def ChannelsB2(url,name):
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub('&nbsp;','',link)
         link=re.sub('&quot;','',link)
         link=re.sub(' ','',link)
         letter=name.split('>')
         name=''
         for i in range(0,len(letter)-1):
                name=name+letter[i]+'>'

         if letter[len(letter)-1]==u' 热门'.encode('utf8'):
                match=re.compile('<ulclass="songContant">(.+?)</ul>').findall(link)
                match0=re.compile('<imgsrc="(.+?)"(.+?)<ahref="(.+?)"(.+?)>(.+?)</a>').findall(match[0])    
                for thumbnail,other1,url1,other2,name1 in match0:
                       addDir(name+name1,url1,6,thumbnail)
         else:
                match=re.compile('>'+letter[len(letter)-1]+'</a><ulclass="(.+?)</div>').findall(link)
                match0=re.compile('href="(.+?)"(.+?)>(.+?)</a>').findall(match[0])       
                for url1,other,name1 in match0:
                       addDir(name+name1,url1,6,'')

def ChannelsB3(url,name):
         addDir(name+'>'+u'热门曲目'.encode('utf8'),url,8,'')
         addDir(name+'>'+u'最新曲目'.encode('utf8'),url,8,'')
         art=url.replace('http://www.kuwo.cn/mingxing/','')
         art=art.replace('/','')
         url1='http://yinyue.kuwo.cn/yy/st/ArtistAlbum?name='+art+'&page=1'
         addDir(name+u'>全部专辑'.encode('utf8'),url1,7,'')


def ChannelsB4(url,name):
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub('&nbsp;','',link)
         link=re.sub('&quot;','',link)
         link=re.sub(' ','',link)

         match=re.compile('<liclass="gray">(.+?)</li>').findall(link)  
         if len(match)>0:
                  name=name.replace(u'全部专辑'.encode('utf8'),u'专辑'.encode('utf8'))
                  name=re.sub(' \xe3\x80\x90\xe7\xac\xac(.+?)\xe9\xa1\xb5\xe3\x80\x91','',name)
                  url0=url.split('&')                  
                  tmp=match[0].replace(u'页'.encode('utf8'),'')
                  page=tmp.split('/')
                  pagecur=int(page[0])
                  pagenum=int(page[1])
                  for i in range(0,pagenum):
                          if i+1!=pagecur:
                                  addDir(name+u' 【第'.encode('utf8')+str(i+1)+u'页】'.encode('utf8'),url0[0]+'&page='+str(i+1),7,'')    

         match=re.compile('<divid="jxzjblock"(.+?)</div>').findall(link)   
         match0=re.compile('<imgsrc="(.+?)"title="(.+?)"(.+?)href="(.+?)"').findall(match[0])   
         num=0      
         for thumbnail,name1,other,url1 in match0:
                  num=num+1
                  addDir(name+'>'+name1,url1,8,thumbnail)     

def ListB(url,name):
         addDir(u'当前位置：'.encode('utf8')+name,url,20,'')
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub('&nbsp;','',link)
         link=re.sub('&quot;','',link)
         link=re.sub(' ','',link)

         if name.find(u'最新曲目'.encode('utf8'))!=-1:
                match=re.compile('<divid="listContent_1"(.+?)</div>').findall(link)         
                match0=re.compile('value="(.+?)"(.+?)title="(.+?)"').findall(match[0])    
                lista='' 
                for i in range(0,len(match0)):
                       lista=lista+'/'+match0[i][0]
                       addLink(str(i+1)+'.'+match0[i][2],match0[i][0],15,'')
                       if i+1==len(match0):
                               addLink(u'播放全部'.encode('utf8'),lista,15,'')

         else:
                match=re.compile('<divid="listContent_0"(.+?)</div>').findall(link)         
                match0=re.compile('value="(.+?)"(.+?)title="(.+?)"').findall(match[0])    
                lista='' 
                for i in range(0,len(match0)):
                       lista=lista+'/'+match0[i][0]
                       addLink(str(i+1)+'.'+match0[i][2],match0[i][0],15,'')
                       if i+1==len(match0):
                               addLink(u'播放全部'.encode('utf8'),lista,15,'')

def ChannelsC(url,name):
         addDir(name+u'>人气'.encode('utf8'),'http://fang.kuwo.cn/p/hot_playlist_1.htm',10,'')
         addDir(name+u'>最新'.encode('utf8'),'http://fang.kuwo.cn/p/latest_playlist_1.htm',10,'')
         addDir(name+u'>推荐'.encode('utf8'),'http://fang.kuwo.cn/p/recommend_playlist_1.htm',10,'')
         addDir(name+u'>分类'.encode('utf8'),'http://fang.kuwo.cn/p/cat_1.htm',11,'')

def ChannelsC1(url,name):
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub('&nbsp;','',link)
         link=re.sub('&quot;','',link)
         link=re.sub(' ','',link)

         name=re.sub(' \xe3\x80\x90\xe7\xac\xac(.+?)\xe9\xa1\xb5\xe3\x80\x91','',name) 
         name=re.sub(u' 【首页】'.encode('utf8'),'',name) 
         name=re.sub(u' 【尾页】'.encode('utf8'),'',name) 
         name=re.sub(u' 【上一页】'.encode('utf8'),'',name) 
         name=re.sub(u' 【下一页】'.encode('utf8'),'',name) 

         match=re.compile('<divclass="gd_popleft">(.+?)<imgsrc="(.+?)"(.+?)href="(.+?)"(.+?)title="(.+?)">').findall(link)
         for other0,thumbnail,other1,url1,other2,name1 in match:
                  addDir(name+'>'+name1,url1,14,thumbnail)

         match=re.compile('<divclass="manu_c">(.+?)</div>').findall(link)
         if len(match)>0:
                  match0=re.compile('href="(.+?)">(.+?)</a>').findall(match[0])
                  for url1,name1 in match0:
                           if name1.find(u'页'.encode('utf8'))==-1:
                                    addDir(name+u' 【第'.encode('utf8')+name1+u'页】'.encode('utf8'),url1,10,'')
                           else:
                                    addDir(name+u' 【'.encode('utf8')+name1+u'】'.encode('utf8'),url1,10,'')

def ChannelsC2(url,name):
         addDir(name+u'>华人男歌手'.encode('utf8'),url,12,'')
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub('&nbsp;','',link)
         link=re.sub('&quot;','',link)
         link=re.sub(' ','',link)
         match=re.compile('<ulclass="fang_fl">(.+?)</ul>').findall(link)
         for info in match:
                  match0=re.compile('href="(.+?)"(.+?)>(.+?)</a>').findall(info)
                  for url1,other,name1 in match0:
                           addDir(name+'>'+name1,url1,12,'')

def ChannelsC3(url,name):
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub('&nbsp;','',link)
         link=re.sub('&quot;','',link)
         link=re.sub(' ','',link)
         match=re.compile('<ulclass="fang_star">(.+?)</ul>').findall(link)
         for info in match:
                  match0=re.compile('href="(.+?)"(.+?)>(.+?)</a>').findall(info)
                  for url1,other,name1 in match0:
                           addDir(name+'>'+name1,url1,13,'')

def ChannelsC4(url,name):
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub('&nbsp;','',link)
         link=re.sub('&quot;','',link)
         link=re.sub(' ','',link)

         name=re.sub(' \xe3\x80\x90\xe7\xac\xac(.+?)\xe9\xa1\xb5\xe3\x80\x91','',name) 
         name=re.sub(u' 【首页】'.encode('utf8'),'',name) 
         name=re.sub(u' 【尾页】'.encode('utf8'),'',name) 
         name=re.sub(u' 【上一页】'.encode('utf8'),'',name) 
         name=re.sub(u' 【下一页】'.encode('utf8'),'',name) 

         match=re.compile('<divclass="left"><div(.+?)href="(.+?)"target="_blank"class="l_pic70"><imgtitle="(.+?)"src="(.+?)"').findall(link)
         for other,url1,name1,thumbnail in match:
                  addDir(name+'>'+name1,url1,14,thumbnail)

         match=re.compile('<divclass="manu_c"(.+?)</div>').findall(link)
         if len(match)>0:
                  match0=re.compile('href="(.+?)">(.+?)</a>').findall(match[0])
                  for url1,name1 in match0:
                           if name1.find(u'页'.encode('utf8'))==-1:
                                    addDir(name+u' 【第'.encode('utf8')+name1+u'页】'.encode('utf8'),'http://sou.kuwo.cn'+url1,13,'')
                           else:
                                    addDir(name+u' 【'.encode('utf8')+name1+u'】'.encode('utf8'),'http://sou.kuwo.cn'+url1,13,'')



def ListC(url,name):
         addDir(u'当前位置：'.encode('utf8')+name,url,20,'')
         req = urllib2.Request(url)
         req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
         response = urllib2.urlopen(req)
         link=response.read()
         response.close()
         link=re.sub('\r','',link)
         link=re.sub('\n','',link)
         link=re.sub('\t','',link)
         link=re.sub('&nbsp;','',link)
         link=re.sub('&quot;','',link)
         link=re.sub(' ','',link)

         match=re.compile('<tdclass="newSong_name1"(.+?)href="(.+?)"title="(.+?)"').findall(link)
         lista='' 
         for i in range(0,len(match)):
                  tmp=match[i][1].split('/')
                  id=tmp[len(tmp)-1]
                  id=id.replace('.htm','')
                  lista=lista+'/'+id
                  addLink(str(i+1)+'.'+match[i][2],id,15,'')
                  if i+1==len(match):
                         addLink(u'播放全部'.encode('utf8'),lista,15,'')


def PlayMusic(url,name):
         playlist=xbmc.PlayList(0)
         playlist.clear()

         ids=url.split('/')
         for id in ids:
                if id!='':
                       req = urllib2.Request('http://plugin.kuwo.cn/mbox/st/FlashData?rid=MUSIC_'+id)
                       req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                       response = urllib2.urlopen(req)
                       link=response.read()
                       response.close()
                       match=re.compile('<name>(.+?)</name>').findall(link)
                       mname=match[0]
                       match=re.compile('<artist>(.+?)</artist>').findall(link)
                       mart=match[0]
                       match=re.compile('<path>(.+?)</path>').findall(link)
                       mpath='http://dl.cdn.kuwo.cn/'+match[0]
                       #addDir(mname+mart+mpath,'',4,'')

	               listitem=xbmcgui.ListItem(mname)
                       listitem.setInfo( type="Music", infoLabels={ "Title": mname, "Artist": mart} )
                       playlist.add(mpath, listitem)
         xbmc.Player().play(playlist)


                
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
        Categories()

elif mode==1:
        print ""+url
        ChannelsA(url,name) 
 
elif mode==2:
        print ""+url
        ListsA(url,name)
        
elif mode==3:
        print ""+url
        ChannelsB(url,name)
        
elif mode==4:
        print ""+url
        ChannelsB1(url,name)
        
elif mode==5:
        print ""+url
        ChannelsB2(url,name)
        
elif mode==6:
        print ""+url
        ChannelsB3(url,name)
        
elif mode==7:
        print ""+url
        ChannelsB4(url,name)
        
elif mode==8:
        print ""+url
        ListB(url,name)

elif mode==9:
        print ""+url
        ChannelsC(url,name)

elif mode==10:
        print ""+url
        ChannelsC1(url,name)

elif mode==11:
        print ""+url
        ChannelsC2(url,name)

elif mode==12:
        print ""+url
        ChannelsC3(url,name)

elif mode==13:
        print ""+url
        ChannelsC4(url,name)

elif mode==14:
        print ""+url
        ListC(url,name)
   
elif mode==15:
        print ""+url
        PlayMusic(url,name)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
