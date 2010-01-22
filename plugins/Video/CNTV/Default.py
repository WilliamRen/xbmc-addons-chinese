# -*- coding: cp936 -*-
import xbmc,xbmcgui,xbmcplugin,urllib2,urllib,re,sys

#CNTV - by robinttt 2010.

def Roots():
	li=xbmcgui.ListItem(u'爱西柚'.encode('utf8'))
	u=sys.argv[0]+"?mode=1&name="+urllib.quote_plus(u'爱西柚'.encode('utf8'))
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem('爱布谷')
	u=sys.argv[0]+"?mode=8&name="+urllib.quote_plus('爱布谷')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def BuguA(name):
	li=xbmcgui.ListItem(name+'>分类')
	u=sys.argv[0]+"?mode=9&name="+urllib.quote_plus(name+'>分类')+"&url="+urllib.quote_plus('http://bugu.cntv.cn/category/index.shtml')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>频道')
	u=sys.argv[0]+"?mode=9&name="+urllib.quote_plus(name+'>频道')+"&url="+urllib.quote_plus('http://bugu.cntv.cn/channel/index.shtml')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>栏目')
	u=sys.argv[0]+"?mode=9&name="+urllib.quote_plus(name+'>栏目')+"&url="+urllib.quote_plus('http://bugu.cntv.cn/column/index.shtml')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>影视')
	u=sys.argv[0]+"?mode=9&name="+urllib.quote_plus(name+'>影视')+"&url="+urllib.quote_plus('http://bugu.cntv.cn/television/index.shtml')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def BuguB(name,url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=re.sub('\r','',link)
        link=re.sub('\n','',link)
        link=re.sub('\t','',link)
        match=re.compile('<p class="edh"(.+?)id="(.+?)">(.+?)</p>').findall(link)
        for i in range(0,len(match)):
                name1=re.sub('<a(.+?)>','',match[i][2])
                name1=re.sub('</a>','',name1)
	        li=xbmcgui.ListItem(name+'>'+name1)
	        u=sys.argv[0]+"?mode=10&name="+urllib.quote_plus(name+'>'+name1)+"&url="+urllib.quote_plus(url)+"&id="+urllib.quote_plus('<p class="edh"'+match[i][0]+'id="'+match[i][1]+'">'+match[i][2]+'</p>')
	        xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def BuguC(name,url,id):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=re.sub('\r','',link)
        link=re.sub('\n','',link)
        link=re.sub('\t','',link)
        match=re.compile(id+'(.+?)</table>').findall(link)
        match0=re.compile('href="(.+?)" target="_blank" class="cyan">(.+?)</a>').findall(match[0])
        for url1,name1 in match0:
	        li=xbmcgui.ListItem(name+'>'+name1)
	        u=sys.argv[0]+"?mode=11&name="+urllib.quote_plus(name+'>'+name1)+"&url="+urllib.quote_plus(url1)
	        xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def BuguD(name,url):
	li=xbmcgui.ListItem('当前位置：'+name)
	u=sys.argv[0]+"?mode=20&name="+urllib.quote_plus(name)
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('var brief="(.+?)";').findall(link)
        plot=match[0]
        match=re.compile("new title_array\('(.+?)','(.+?)','(.+?)','(.+?)'").findall(link)
        for i in range(0,len(match)):
	        li=xbmcgui.ListItem(str(i+1)+'. '+match[i][0]+'  (时长:'+match[i][2]+')',match[i][1],match[i][1])
	        u=sys.argv[0]+"?mode=12&name="+urllib.quote_plus(name)+"&url="+urllib.quote_plus(match[i][3].replace('shtml','txt'))+"&plot="+urllib.quote_plus(plot)+"&thumb="+urllib.quote_plus(match[i][1])
	        xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li)

def BuguE(name,url,thumb,plot):
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
        match=re.compile('"chapters":\[(.+?)\]').findall(link)
        match0=re.compile('"url":"(.+?)"').findall(match[0])
        for i in range(0,len(match0)):
        	listitem=xbmcgui.ListItem(name,thumb,thumb)
                listitem.setInfo(type="Video",infoLabels={"Title":name,"plot":plot})
                playlist.add(match0[i], listitem)
        xbmc.Player(player_type).play(playlist)

def XiyouA(name):
	li=xbmcgui.ListItem(name+u'>视频'.encode('utf8'))
	u=sys.argv[0]+"?mode=2&name="+urllib.quote_plus(name+u'>视频'.encode('utf8'))+"&category="+urllib.quote_plus('Video')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+u'>专辑'.encode('utf8'))
	u=sys.argv[0]+"?mode=2&name="+urllib.quote_plus(name+u'>专辑'.encode('utf8'))+"&category="+urllib.quote_plus('Playlist')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def XiyouB(name,category):
        req = urllib2.Request('http://xiyou.cntv.cn/'+category.lower()+'/index.html')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=re.sub('\r','',link)
        link=re.sub('\n','',link)
        link=re.sub('\t','',link)
	li=xbmcgui.ListItem(name+u'>全部'.encode('utf8'))
	u=sys.argv[0]+"?mode=3&name="+urllib.quote_plus(name+u'>全部'.encode('utf8'))+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus('0')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
        match=re.compile('<table id="table_1"(.+?)</table>').findall(link)
        match0=re.compile('<a id="(.+?)" href="(.+?)">(.+?)</a>').findall(match[0])
        for id,url1,name1 in match0:
	        li=xbmcgui.ListItem(name+'>'+name1)
	        u=sys.argv[0]+"?mode=3&name="+urllib.quote_plus(name+'>'+name1)+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus(id)
	        xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def XiyouC(name,category,id):
	li=xbmcgui.ListItem(name+u'>今天'.encode('utf8'))
	u=sys.argv[0]+"?mode=4&name="+urllib.quote_plus(name+u'>今天'.encode('utf8'))+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus(id)+"&type="+urllib.quote_plus('today')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+u'>本周'.encode('utf8'))
	u=sys.argv[0]+"?mode=4&name="+urllib.quote_plus(name+u'>本周'.encode('utf8'))+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus(id)+"&type="+urllib.quote_plus('week')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+u'>本月'.encode('utf8'))
	u=sys.argv[0]+"?mode=4&name="+urllib.quote_plus(name+u'>本月'.encode('utf8'))+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus(id)+"&type="+urllib.quote_plus('month')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+u'>历史'.encode('utf8'))
	u=sys.argv[0]+"?mode=4&name="+urllib.quote_plus(name+u'>历史'.encode('utf8'))+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus(id)+"&type="+urllib.quote_plus('year')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def XiyouD(name,category,id,type):
	li=xbmcgui.ListItem(name+u'>最热'.encode('utf8'))
	u=sys.argv[0]+"?mode=5&name="+urllib.quote_plus(name+u'>最热'.encode('utf8'))+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus(id)+"&type="+urllib.quote_plus(type)+"&handler="+urllib.quote_plus('HotMax')+"&page="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+u'>收藏最多'.encode('utf8'))
	u=sys.argv[0]+"?mode=5&name="+urllib.quote_plus(name+u'>收藏最多'.encode('utf8'))+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus(id)+"&type="+urllib.quote_plus(type)+"&handler="+urllib.quote_plus('PlayMax')+"&page="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+u'>评论最多'.encode('utf8'))
	u=sys.argv[0]+"?mode=5&name="+urllib.quote_plus(name+u'>评论最多'.encode('utf8'))+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus(id)+"&type="+urllib.quote_plus(type)+"&handler="+urllib.quote_plus('CommentMax')+"&page="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+u'>顶的最多'.encode('utf8'))
	u=sys.argv[0]+"?mode=5&name="+urllib.quote_plus(name+u'>顶的最多'.encode('utf8'))+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus(id)+"&type="+urllib.quote_plus(type)+"&handler="+urllib.quote_plus('UpMax')+"&page="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+u'>最新'.encode('utf8'))
	u=sys.argv[0]+"?mode=5&name="+urllib.quote_plus(name+u'>最新'.encode('utf8'))+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus(id)+"&type="+urllib.quote_plus(type)+"&handler="+urllib.quote_plus('Newest')+"&page="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def XiyouE(name,category,handler,id,type,page):
        tmp='Ajax'+category+handler
        url='http://rpc.xiyou.cntv.cn/rpc.php?id='+id+'&handler='+tmp+'&type='+type+'&table%5Fpage%5F1='+page+'&display%5Fid='+tmp.lower()
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=re.sub('\r','',link)
        link=re.sub('\n','',link)
        link=re.sub('\t','',link)
        link=re.sub(' ','',link)

        if link.find('id="noRecordRow">')==-1:
        #获取当前页码
                match=re.compile('<aclass="current_page"(.+?)table_page_1=(.+?)\',').findall(link)
	        li=xbmcgui.ListItem(u'当前位置：'.encode('utf8')+name+u' 【第'.encode('utf8')+match[0][1]+u'页】'.encode('utf8'))
	        u=sys.argv[0]+"?mode=20"
	        xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
                #获取当前列表
                match=re.compile('<tableid="table_1"(.+?)</table>').findall(link)
                if category=='Video':
                        match0=re.compile('<imgsrc="(.+?)"title="(.+?)"/>(.+?)"videotime"><span>(.+?)</span>(.+?)<divclass="addtolist"id="(.+?)">(.+?)<spanclass="itemtitle">(.+?)title="(.+?)"(.+?)title="(.+?)">').findall(match[0])
                       	for i in range(0,len(match0)):
                        	li=xbmcgui.ListItem(str(i+1)+'.'+match0[i][8],match0[i][0],match0[i][0])
                        	u=sys.argv[0]+"?mode=7&name="+urllib.quote_plus(match0[i][8])+"&id="+urllib.quote_plus(match0[i][5])+"&thumb="+urllib.quote_plus(match0[i][0])+"&director="+urllib.quote_plus(match0[i][10])+"&duration="+urllib.quote_plus(match0[i][3])+"&plot="+urllib.quote_plus(match0[i][1])
                        	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
                else:
                        match0=re.compile('<imgsrc="(.+?)"/>(.+?)<ahref="/playlistinfo/(.+?)"title="(.+?)>(.+?)</a>').findall(match[0])
                        for i in range(0,len(match0)):
                        	li=xbmcgui.ListItem(str(i+1)+'.'+match0[i][4],match0[i][0],match0[i][0])
                        	u=sys.argv[0]+"?mode=6&name="+urllib.quote_plus(name+'>'+match0[i][4])+"&id="+urllib.quote_plus(match0[i][2])
                        	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
                #获取其他页码
                match=re.compile('<divclass="paging">(.+?)</div>').findall(link)
                match0=re.compile('<aclass="(.+?)"(.+?)table_page_1=(.+?)\',(.+?)">(.+?)</a>').findall(match[0])
                for i in range(0,len(match0)):
                        if match0[i][0]=='first_page' or match0[i][0]=='last_page' or match0[i][0]=='prev_page' or match0[i][0]=='next_page':
                        	li=xbmcgui.ListItem('..'+match0[i][4])
                        	u=sys.argv[0]+"?mode=5&name="+urllib.quote_plus(name)+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus(id)+"&type="+urllib.quote_plus(type)+"&handler="+urllib.quote_plus(handler)+"&page="+urllib.quote_plus(match0[i][2])
                        	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
                        elif match0[i][0]!='current_page':
                        	li=xbmcgui.ListItem(u'..第'.encode('utf8')+match0[i][4]+u'页'.encode('utf8'))
                        	u=sys.argv[0]+"?mode=6&name="+urllib.quote_plus(name)+"&category="+urllib.quote_plus(category)+"&id="+urllib.quote_plus(id)+"&type="+urllib.quote_plus(type)+"&handler="+urllib.quote_plus(handler)+"&page="+urllib.quote_plus(match0[i][2])
                        	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def XiyouF(name,id):
        li=xbmcgui.ListItem(u'当前位置：'.encode('utf8')+name)
        u=sys.argv[0]+"?mode=20"
        xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

        url='http://rpc.xiyou.cntv.cn/rpc.php?orderBy=0&handler=AjaxPlaylistVideoList&display%5Fid=playlistVideoList&id='+id
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=re.sub('\r','',link)
        link=re.sub('\n','',link)
        link=re.sub('\t','',link)
        link=re.sub(' ','',link)
        match=re.compile('<imgsrc="(.+?)"title="(.+?)"/>(.+?)"videotime"><span>(.+?)</span>(.+?)<divclass="addtolist"id="(.+?)">(.+?)<spanclass="itemtitle">(.+?)title="(.+?)"').findall(link)
        for i in range(0,len(match)):
                li=xbmcgui.ListItem(str(i+1)+'.'+match[i][8],match[i][0],match[i][0])
                u=sys.argv[0]+"?mode=7&name="+urllib.quote_plus(match[i][8])+"&id="+urllib.quote_plus(match[i][5])+"&thumb="+urllib.quote_plus(match[i][0])+"&director="+urllib.quote_plus('')+"&duration="+urllib.quote_plus('')+"&plot="+urllib.quote_plus(match[i][1])
                xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def XiyouG(name,id,director,thumb,plot,duration):
        #播放当前视频
        url='http://rpc.xiyou.cntv.cn/rpc.php?id='+id+'&module=VideoDescShow'
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('\\\u4e0a\\\u4f20\\\u65f6\\\u95f4\\\uff1a(.+?)<').findall(link)
        path='http://59.151.104.234/video/'+match[0].replace('-','/')+'/'+id+'_001.mp4'
        li=xbmcgui.ListItem(u'播放当前视频：'.encode('utf8')+name,'',thumb)
        li.setInfo(type="Video",infoLabels={"Title":name,"Director":director,"Duration":duration,"Plot":plot})
        xbmcplugin.addDirectoryItem(int(sys.argv[1]),path,li)

        #播放相关视频
        url='http://xiyou.cntv.cn/video-relative.php?item_id='+id
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('"title":"(.+?)","userName":"(.+?)","(.+?)"timeSpan":"(.+?)","(.+?)"imagePath":"(.+?)"(.+?)"videoFilePath":"(.+?)"}').findall(link)
        for i in range(0,len(match)):
                if match[i][7].find('qgds')==-1:
                        path0=match[i][7].replace('\\','')
                        path1=path0.split('#')
                        path=path1[0]+'_001.mp4'
                li=xbmcgui.ListItem(u'播放相关视频：'+eval('u"'+match[i][0]+'"'),match[i][5].replace('\\',''),match[i][5].replace('\\',''))
                li.setInfo(type="Video",infoLabels={"Title":eval('u"'+match[i][0]+'"'),"Director":eval('u"'+match[i][1]+'"'),"Duration":match[i][3],"Plot":plot})
                xbmcplugin.addDirectoryItem(int(sys.argv[1]),path,li)



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

params=get_params()

mode=None
name=None
url=None
category=None
id=None
type=None
handler=None
page=None
thumb=None
director=None
studio=None
plot=None
duration=None


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
        category=urllib.unquote_plus(params["category"])
except:
        pass
try:
        id=urllib.unquote_plus(params["id"])
except:
        pass
try:
        type=urllib.unquote_plus(params["type"])
except:
        pass
try:
        handler=urllib.unquote_plus(params["handler"])
except:
        pass
try:
        page=urllib.unquote_plus(params["page"])
except:
        pass
try:
        director=urllib.unquote_plus(params["director"])
except:
        pass
try:
        studio=urllib.unquote_plus(params["studio"])
except:
        pass
try:
        plot=urllib.unquote_plus(params["plot"])
except:
        pass
try:
        thumb=urllib.unquote_plus(params["thumb"])
except:
        pass
try:
        duration=urllib.unquote_plus(params["duration"])
except:
        pass



if mode==None:
	name=''
	Roots()

elif mode==1:
	XiyouA(name)

elif mode==2:
	XiyouB(name,category)

elif mode==3:
	XiyouC(name,category,id)

elif mode==4:
	XiyouD(name,category,id,type)

elif mode==5:
        XiyouE(name,category,handler,id,type,page)

elif mode==6:
        XiyouF(name,id)

elif mode==7:
        XiyouG(name,id,director,thumb,plot,duration)

elif mode==8:
        BuguA(name)

elif mode==9:
        BuguB(name,url)

elif mode==10:
        BuguC(name,url,id)

elif mode==11:
        BuguD(name,url)

elif mode==12:
        BuguE(name,url,plot,thumb)


xbmcplugin.setPluginCategory(int(sys.argv[1]), name )
xbmcplugin.endOfDirectory(int(sys.argv[1]))

    
