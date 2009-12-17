# -*- coding: cp936 -*-
import httplib,urllib,re,xbmcplugin,xbmcgui,xbmc,os

#CCTV Video - by Robinttt 2009.

def CATEGORIES():
         addDir('标清直播','/index.shtml',6,os.getcwd()+'\\resources\\media\\Default1.jpg')
         addDir('高清直播','/live_h/index.shtml',6,os.getcwd()+'\\resources\\media\\Default2.jpg')
         addDir('蓝光直播','/cctv1/l/index.shtml',6,os.getcwd()+'\\resources\\media\\Default3.jpg')
         addDir('视频点播','/podcast/index',1,os.getcwd()+'\\resources\\media\\Default4.jpg')

def LiveChannel(url,name):
         req=httplib.HTTPConnection("zhibo.cctv.com")
         req.request("get", url)
         response=req.getresponse()
         link=response.read()
         response.close()
         match=re.compile("<span class='list_til'(.+?)href='(.+?)'(.+?)>(.+?)</a>").findall(link)
         if len(match)>0:
                  check=''
                  for temp1,url1,temp2,name1 in match:
                             name1=name1.replace('<center>','')
                             name1=name1.replace('</center>','')
                             name1=name1.replace('<font size=2>','')
                             name1=name1.replace('</font>','')
                             if url1.find('Arabic')!=-1:name1='CCTV-阿拉伯语'
                             if url1!=check and name1.find('<img')==-1:
                                        check=url1
                                        url1=url1.replace('http://zhibo.cctv.com','')
                                        addDir(name+'>'+name1,url1,7,os.getcwd()+'\\resources\\media\\play.png')

def LiveLink(url,name):
         #获取p2p播放地址
         req=httplib.HTTPConnection("zhibo.cctv.com")
         req.request("get", url)
         response=req.getresponse()
         link=response.read()
         response.close()
         match=re.compile('<iframe src="(.+?)channel=(.+?)&').findall(link)
         if len(match)>0:xbmc.executebuiltin('System.ExecWait(\\"'+ os.getcwd()+'\\resources\\player\\cctvlive.exe\\" '+match[0][1]+')')

def DibbleChannel(url,name):
         req=httplib.HTTPConnection("vod.cctv.com")
         req.request("get", url)
         response=req.getresponse()
         link=response.read()
         response.close()                  
         match=re.compile('<dd><a href="/podcast/(.+?)">(.+?)</a></dd>').findall(link)
         for url1,name1 in match:
                  addDir(name+'>'+name1,'http://vod.cctv.com/podcast/'+url1,2,os.getcwd()+'\\resources\\media\\Default4.jpg')
         match=re.compile('<dd><a href="/page/(.+?)">(.+?)</a></dd>').findall(link)
         for url1,name1 in match:
                  if name1.find('回看')==-1:
                          addDir(name+'>'+name1,'/page/'+url1,2,os.getcwd()+'\\resources\\media\\Default4.jpg')

def DibbleABC(url,name):
         req=httplib.HTTPConnection("vod.cctv.com")
         req.request("get", url)
         response=req.getresponse()
         link=response.read()
         response.close()
         match=re.compile('<h3>(.+?)</h3>').findall(link)
         for name1 in match:
                  addDir(name+'>'+name1,url,3,os.getcwd()+'\\resources\\media\\Default4.jpg')  

def DibbleColumn(url,name):
         req=httplib.HTTPConnection("vod.cctv.com")
         req.request("get", url)
         response=req.getresponse()
         link=response.read()
         response.close()
         match0=re.sub('\r','',link)
         match0=re.sub('\n','',match0)
         name1=name.split('>')
         name2=name.replace('>'+name1[len(name1)-1],'')
         match1=re.compile('<h3>'+name1[len(name1)-1]+'</h3>(.+?)</ul>').findall(match0)
         match=re.compile('<a href="(.+?)" target="_blank">(.+?)</a>').findall(match1[0])
         for url1,name1 in match:
                  addDir(name2+'>'+name1,url1,4,os.getcwd()+'\\resources\\media\\Default4.jpg')

def DibbleList(url,name):
         #此处必须用httplib，用urllib2得到的永远是第1页的数据，花了我半个月时间研究才搞定AJAX
         #首先判断url，是否需要初始化
         if url.find('|')!=-1:
                tmp=url.split('|')
                elementId=tmp[0]
                pagec=tmp[1]
                paget=tmp[2]
         else:
                req=httplib.HTTPConnection("vod.cctv.com")
                req.request("get", url)
                response=req.getresponse()
                link=response.read()
                response.close()

                elementId=''
                paget=''
                match=re.compile('var elementId = "(.+?)"').findall(link)
                if len(match)>0: elementId=match[0]
                pagec='1'
                match=re.compile('"total_page">(.+?)</b>').findall(link)
                if len(match)>0: paget=match[0] 

         if elementId!='':  #获取影片列表
                headers = {'elementId':elementId,'currpage':pagec}
                req = httplib.HTTPConnection("vod.cctv.com") 
                req.request("get", "/act/platform/view/page/showElement.jsp", '', headers)
                response=req.getresponse()
                link= response.read()
                response.close()
                match=re.compile('href="/video/VIDE(.+?)" title="(.+?)" target="_blank"><img(.+?)src="(.+?)"').findall(link)	

                if len(match)>0:
                       match1=re.compile('"mh_title">(.+?)</span>').findall(link)
                       name=match1[0]
                       addDir('..当前位置:'+name+' 第'+pagec+'/'+paget+'页',elementId+'|1|'+paget,4,os.getcwd()+'\\resources\\media\\Default4.jpg')
                       if int(pagec)>1:
                              addDir('..上一页',elementId+'|'+str(int(pagec)-1)+'|'+paget,4,os.getcwd()+'\\resources\\media\\Pageup.png')
                       if int(pagec)<int(paget): 
                              addDir('..下一页',elementId+'|'+str(int(pagec)+1)+'|'+paget,4,os.getcwd()+'\\resources\\media\\Pagedown.png')
                              addDir('..最后一页',elementId+'|'+paget+'|'+paget,4,os.getcwd()+'\\resources\\media\\Default4.jpg')
                       for url1,name1,temp,thumbnail in match:
                              thumbnail=re.sub(' ','%20',thumbnail)
                              addDir(name1,url1,5,thumbnail)


def DibbleLink(url,name):
         #获取影片实际播放地址
         req=httplib.HTTPConnection("vod.cctv.com")
         req.request("get", "/video/VIDE"+url)
         response=req.getresponse()
         link=response.read()
         response.close()
         Duration=''
         Plot=''
         Studio=''
         match=re.compile('本集时长：</strong><span class="color_jh">(.+?)</span>').findall(link)
         if len(match)>0:Duration=match[0]
         match=re.compile('内容描述：</strong>(.+?)</p>').findall(link)
         if len(match)>0:Plot=match[0]
         match=re.compile('首播频道：</strong><span class="color_jh">(.+?)</span>').findall(link)
         if len(match)>0:Studio=match[0]
         match=re.compile('栏目名称：</strong>(.+?)</p>').findall(link)
         if len(match)>0:Studio=Studio+'  栏目:'+match[0]
         match=re.compile('首播时间：</strong><span class="color_jh">(.+?)</span>').findall(link)
         if len(match)>0:Studio=Studio+'  首播:'+match[0]

         headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.6) Gecko/2009011913 Firefox/3.0.6'}
         req=httplib.HTTPConnection("vod.cctv.com")
         req.request("get", "/playcfg/flv_info_new.jsp?&videoId=VIDE"+url,'',headers)
         response=req.getresponse()
         link=response.read()
         response.close()
         match=re.compile('"title":"(.+?)"embed":').findall(link)
         if len(match)>0:
                  match1=re.compile('"url":"(.+?)"').findall(match[0])
                  if len(match1)==1:
                           li=xbmcgui.ListItem('播放：'+name,iconImage='', thumbnailImage=os.getcwd()+'\\resources\\media\\PLay.png')
                           li.setInfo(type="Video",infoLabels={"Title":name,"Plot":Plot,"Duration":Duration,"Studio":Studio})
                           xbmcplugin.addDirectoryItem(int(sys.argv[1]),'http://58.221.41.93/v.cctv.com/flash/'+match1[0],li)
                  else:
                           num=0
                           for url1 in match1:   
                                    num=num+1
                                    li=xbmcgui.ListItem('播放：'+name+' 【第'+str(num)+'节】',iconImage='', thumbnailImage=os.getcwd()+'\\resources\\media\\PLay.png')
                                    li.setInfo(type="Video",infoLabels={"Title":name+" 【第"+str(num)+"节】","Plot":Plot,"Duration":Duration,"Studio":Studio})
                                    xbmcplugin.addDirectoryItem(int(sys.argv[1]),'http://58.221.41.93/v.cctv.com/flash/'+url1,li)

                
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
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
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
        DibbleChannel(url,name) 
 
elif mode==2:
        print ""+url
        DibbleABC(url,name)
      
elif mode==3:
        print ""+url
        DibbleColumn(url,name)
      
elif mode==4:
        print ""+url
        DibbleList(url,name)   
     
elif mode==5:
        print ""+url
        DibbleLink(url,name)

elif mode==6:
        print ""+url
        LiveChannel(url,name)

elif mode==7:
        print ""+url
        LiveLink(url,name)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
