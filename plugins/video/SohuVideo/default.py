# -*- coding: cp936 -*-
import xbmc,xbmcgui,xbmcplugin,urllib2,urllib,re,sys

#Sohu Video - by robinttt 2010.

def Roots():
	li=xbmcgui.ListItem('����Ӱ��')
	u=sys.argv[0]+"?mode=1&name="+urllib.quote_plus('����Ӱ��')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem('���ӽ�Ŀ(�����ڴ�)')
	u=sys.argv[0]+"?mode=40&name="+urllib.quote_plus('���ӽ�Ŀ')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem('��Ƶ����(�����ڴ�)')
	u=sys.argv[0]+"?mode=40&name="+urllib.quote_plus('��Ƶ����')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def Channels(name):
	li=xbmcgui.ListItem(name+'>����')
	u=sys.argv[0]+"?mode=2&name="+urllib.quote_plus(name)
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>��')
	u=sys.argv[0]+"?mode=6&name="+urllib.quote_plus(name+'>��')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def ListsA(name):
	li=xbmcgui.ListItem(name+'>��Ӱ����')
	u=sys.argv[0]+"?mode=3&name="+urllib.quote_plus(name+'>��Ӱ')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>���Ӿ����')
	u=sys.argv[0]+"?mode=3&name="+urllib.quote_plus(name+'>���Ӿ�')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>��¼Ƭ����')
	u=sys.argv[0]+"?mode=3&name="+urllib.quote_plus(name+'>��¼Ƭ')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>��Ա����')
	u=sys.argv[0]+"?mode=4&name="+urllib.quote_plus(name+'>��Ա����')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>���Է���')
	u=sys.argv[0]+"?mode=4&name="+urllib.quote_plus(name+'>���Է���')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>��ݼ���')
	u=sys.argv[0]+"?mode=4&name="+urllib.quote_plus(name+'>��ݼ���')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def ListsB(name):
        if name=='����Ӱ��>��¼Ƭ':
		li=xbmcgui.ListItem(name+'>����')
		u=sys.argv[0]+"?mode=4&name="+urllib.quote_plus(name+'>����')
		xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		li=xbmcgui.ListItem(name+'>����')
		u=sys.argv[0]+"?mode=4&name="+urllib.quote_plus(name+'>����')
		xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
        else:
		li=xbmcgui.ListItem(name+'>����')
		u=sys.argv[0]+"?mode=4&name="+urllib.quote_plus(name+'>����')
		xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		li=xbmcgui.ListItem(name+'>����')
		u=sys.argv[0]+"?mode=4&name="+urllib.quote_plus(name+'>����')
		xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def ListsC(name):
        req = urllib2.Request('http://tv.sohu.com/hdsearch/')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=re.sub('\r','',link)
        link=re.sub('\n','',link)
        link=re.sub('\t','',link)

        if name=='����Ӱ��>��¼Ƭ>����':
                match=re.compile('<div class="realCls clear">(.+?)</div>').findall(link)
                match0=re.compile('<li><a href="(.+?)>(.+?)</a>').findall(match[0])
                for url1,name1 in match0:
	                li=xbmcgui.ListItem(name+'>'+name1)
	                u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name+'>'+name1)+"&jsona="+urllib.quote_plus(name1)+"&jsonf="+urllib.quote_plus('7')+"&jsono="+urllib.quote_plus('4')+"&jsonc="+urllib.quote_plus('8')+"&jsonn="+urllib.quote_plus('1')
	                xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

        elif name=='����Ӱ��>��¼Ƭ>����':
                match=re.compile('href="http://tv.sohu.com/tagreal/#key=(.+?)"').findall(link)
                for name1 in match:
	                li=xbmcgui.ListItem(name+'>'+name1)
	                u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name+'>'+name1)+"&jsona="+urllib.quote_plus(name1)+"&jsonf="+urllib.quote_plus('22')+"&jsono="+urllib.quote_plus('4')+"&jsonc="+urllib.quote_plus('8')+"&jsonn="+urllib.quote_plus('1')
	                xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

        elif name=='����Ӱ��>��Ӱ>����':
                match=re.compile('</div><div class="list clear">(.+?)</div></div>').findall(link)
                match0=re.compile('searchKey\("(.+?)"').findall(match[1])
                for name1 in match0:
	                li=xbmcgui.ListItem(name+'>'+name1)
	                u=sys.argv[0]+"?mode=5&name="+urllib.quote_plus(name+'>'+name1)+"&jsona="+urllib.quote_plus(name1)+"&jsonf="+urllib.quote_plus('7')
	                xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

        elif name=='����Ӱ��>��Ӱ>����':
                match=re.compile('<div class="mvCls clear">(.+?)</div>').findall(link)
                match0=re.compile('searchKey\("(.+?)"').findall(match[0])
                for name1 in match0:
	                li=xbmcgui.ListItem(name+'>'+name1)
	                u=sys.argv[0]+"?mode=5&name="+urllib.quote_plus(name+'>'+name1)+"&jsona="+urllib.quote_plus(name1)+"&jsonf="+urllib.quote_plus('12')
	                xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

        elif name=='����Ӱ��>���Ӿ�>����':
                match=re.compile('</div><div class="list clear">(.+?)</div></div>').findall(link)
                match0=re.compile('searchKey\("(.+?)"').findall(match[2])
                for name1 in match0:
	                li=xbmcgui.ListItem(name+'>'+name1)
	                u=sys.argv[0]+"?mode=5&name="+urllib.quote_plus(name+'>'+name1)+"&jsona="+urllib.quote_plus(name1)+"&jsonf="+urllib.quote_plus('7')
	                xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

        elif name=='����Ӱ��>���Ӿ�>����':
                match=re.compile('<div class="tvCls clear">(.+?)</div>').findall(link)
                match0=re.compile('searchKey\("(.+?)"').findall(match[0])
                for name1 in match0:
	                li=xbmcgui.ListItem(name+'>'+name1)
	                u=sys.argv[0]+"?mode=5&name="+urllib.quote_plus(name+'>'+name1)+"&jsona="+urllib.quote_plus(name1)+"&jsonf="+urllib.quote_plus('12')
	                xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

        elif name=='����Ӱ��>��Ա����':
                match=re.compile('<div class="actorCls clear">(.+?)</div>').findall(link)
                match0=re.compile('href="http://tv.sohu.com/hdsearch_test/#key=(.+?)&amp;').findall(match[0])
                for name1 in match0:
	                li=xbmcgui.ListItem(name+'>'+name1)
	                u=sys.argv[0]+"?mode=5&name="+urllib.quote_plus(name+'>'+name1)+"&jsona="+urllib.quote_plus(name1)+"&jsonf="+urllib.quote_plus('04')
	                xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

        elif name=='����Ӱ��>���Է���':
                match=re.compile('<div class="nfCls clear">(.+?)</div>').findall(link)
                match0=re.compile('href="http://tv.sohu.com/tagsearch/#key=(.+?)"').findall(match[0])
                for name1 in match0:
	                li=xbmcgui.ListItem(name+'>'+name1)
	                u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name+'>'+name1)+"&jsona="+urllib.quote_plus(name1)+"&jsonf="+urllib.quote_plus('22')+"&jsono="+urllib.quote_plus('4')+"&jsonc="+urllib.quote_plus('')+"&jsonn="+urllib.quote_plus('1')
	                xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

        elif name=='����Ӱ��>��ݼ���':
                match=re.compile('<div class="yearSearch clear">(.+?)</div>').findall(link)
                match0=re.compile('href="http://tv.sohu.com/hdsearch_test/#key=(.+?)&type=').findall(match[0])
                for name1 in match0:
	                li=xbmcgui.ListItem(name+'>'+name1)
	                u=sys.argv[0]+"?mode=5&name="+urllib.quote_plus(name+'>'+name1)+"&jsona="+urllib.quote_plus(name1)+"&jsonf="+urllib.quote_plus('15')
	                xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def ListsD(name,jsona,jsonf):
	li=xbmcgui.ListItem(name+'>��ಥ��')
	u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name+'>��ಥ��')+"&jsona="+urllib.quote_plus(jsona)+"&jsonf="+urllib.quote_plus(jsonf)+"&jsono="+urllib.quote_plus('1')+"&jsonc="+urllib.quote_plus('')+"&jsonn="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>���·���')
	u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name+'>���·���')+"&jsona="+urllib.quote_plus(jsona)+"&jsonf="+urllib.quote_plus(jsonf)+"&jsono="+urllib.quote_plus('0')+"&jsonc="+urllib.quote_plus('')+"&jsonn="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>��س̶�')
	u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name+'>��س̶�')+"&jsona="+urllib.quote_plus(jsona)+"&jsonf="+urllib.quote_plus(jsonf)+"&jsono="+urllib.quote_plus('')+"&jsonc="+urllib.quote_plus('')+"&jsonn="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def SortsA(name):
	li=xbmcgui.ListItem(name+'>����')
	u=sys.argv[0]+"?mode=7&name="+urllib.quote_plus(name+'>����')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>����')
	u=sys.argv[0]+"?mode=10&name="+urllib.quote_plus(name+'>����')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>����')
	u=sys.argv[0]+"?mode=12&name="+urllib.quote_plus(name+'>����')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)


def SortsB(name):
	li=xbmcgui.ListItem(name+'>ȫ��')
	u=sys.argv[0]+"?mode=8&name="+urllib.quote_plus(name+'>ȫ��')+"&url="+urllib.quote_plus('total')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>ÿ��')
	u=sys.argv[0]+"?mode=8&name="+urllib.quote_plus(name+'>ÿ��')+"&url="+urllib.quote_plus('week')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>ÿ��')
	u=sys.argv[0]+"?mode=8&name="+urllib.quote_plus(name+'>ÿ��')+"&url="+urllib.quote_plus('day')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)


def SortsC(url,name):
	li=xbmcgui.ListItem(name+'>��Ӱ')
	u=sys.argv[0]+"?mode=9&name="+urllib.quote_plus(name+'>��Ӱ')+"&url="+urllib.quote_plus('http://tv.sohu.com/frag/vrs_inc/phb_mv_'+url+'_50.js')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>���Ӿ�')
	u=sys.argv[0]+"?mode=9&name="+urllib.quote_plus(name+'>���Ӿ�')+"&url="+urllib.quote_plus('http://tv.sohu.com/frag/vrs_inc/phb_tv_'+url+'_50.js')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>��¼Ƭ')
	u=sys.argv[0]+"?mode=9&name="+urllib.quote_plus(name+'>��¼Ƭ')+"&url="+urllib.quote_plus('http://tv.sohu.com/frag/vrs_inc/phb_doc_'+url+'_50.js')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def SortsD(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('"DIRECTOR":"(.+?)"(.+?)"tv_comment":"(.+?)"(.+?)"tv_url":"(.+?)"(.+?)"tv_name":"(.+?)"(.+?)"tv_big_pic":"(.+?)"').findall(link)
        if len(match)>0:
		li=xbmcgui.ListItem('��ǰλ��:'+name+'  TOP50')
		u=sys.argv[0]+"?mode=40&name="+urllib.quote_plus(name)
		xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
                for i in range(0,len(match)):
	        	li=xbmcgui.ListItem(str(i+1)+'.'+match[i][6],iconImage='', thumbnailImage=match[i][8])
	        	u=sys.argv[0]+"?mode=16&name="+urllib.quote_plus(match[i][6])+"&url="+urllib.quote_plus(match[i][4])+"&director="+urllib.quote_plus(match[i][0])+"&studio="+urllib.quote_plus('')+"&plot="+urllib.quote_plus(match[i][2])
	        	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def SortsE(url,name):
	li=xbmcgui.ListItem(name+'>����')
	u=sys.argv[0]+"?mode=11&name="+urllib.quote_plus(name+'>����')+"&url="+urllib.quote_plus('4')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>�ܺ�')
	u=sys.argv[0]+"?mode=11&name="+urllib.quote_plus(name+'>�ܺ�')+"&url="+urllib.quote_plus('3')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>һ��')
	u=sys.argv[0]+"?mode=11&name="+urllib.quote_plus(name+'>һ��')+"&url="+urllib.quote_plus('2')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>��Ƭ')
	u=sys.argv[0]+"?mode=11&name="+urllib.quote_plus(name+'>��Ƭ')+"&url="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def SortsF(url,name):
	li=xbmcgui.ListItem(name+'>ȫ��')
	u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name+'>ȫ��')+"&jsona="+urllib.quote_plus(url)+"&jsonf="+urllib.quote_plus('16')+"&jsono="+urllib.quote_plus('3')+"&jsonc="+urllib.quote_plus('')+"&jsonn="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>��Ӱ')
	u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name+'>��Ӱ')+"&jsona="+urllib.quote_plus(url)+"&jsonf="+urllib.quote_plus('16')+"&jsono="+urllib.quote_plus('3')+"&jsonc="+urllib.quote_plus('1')+"&jsonn="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>���Ӿ�')
	u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name+'>���Ӿ�')+"&jsona="+urllib.quote_plus(url)+"&jsonf="+urllib.quote_plus('16')+"&jsono="+urllib.quote_plus('3')+"&jsonc="+urllib.quote_plus('2')+"&jsonn="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>��¼Ƭ')
	u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name+'>��¼Ƭ')+"&jsona="+urllib.quote_plus(url)+"&jsonf="+urllib.quote_plus('16')+"&jsono="+urllib.quote_plus('3')+"&jsonc="+urllib.quote_plus('8')+"&jsonn="+urllib.quote_plus('1')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def SortsG(url,name):
	li=xbmcgui.ListItem(name+'>����')
	u=sys.argv[0]+"?mode=13&name="+urllib.quote_plus(name+'>����')+"&url="+urllib.quote_plus('219')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>��Ա')
	u=sys.argv[0]+"?mode=13&name="+urllib.quote_plus(name+'>��Ա')+"&url="+urllib.quote_plus('220')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>����')
	u=sys.argv[0]+"?mode=13&name="+urllib.quote_plus(name+'>����')+"&url="+urllib.quote_plus('221')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>����')
	u=sys.argv[0]+"?mode=13&name="+urllib.quote_plus(name+'>����')+"&url="+urllib.quote_plus('222')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>����')
	u=sys.argv[0]+"?mode=13&name="+urllib.quote_plus(name+'>����')+"&url="+urllib.quote_plus('223')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def SortsH(url,name):
	li=xbmcgui.ListItem(name+'>ȫ��')
	u=sys.argv[0]+"?mode=14&name="+urllib.quote_plus(name+'>ȫ��')+"&url="+urllib.quote_plus('http://tv.sohu.com/frag/vrs_inc/phb_score_'+url+'_50.js')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>��Ӱ')
	u=sys.argv[0]+"?mode=14&name="+urllib.quote_plus(name+'>��Ӱ')+"&url="+urllib.quote_plus('http://tv.sohu.com/frag/vrs_inc/phb_score_mv_'+url+'_50.js')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
	li=xbmcgui.ListItem(name+'>���Ӿ�')
	u=sys.argv[0]+"?mode=14&name="+urllib.quote_plus(name+'>���Ӿ�')+"&url="+urllib.quote_plus('http://tv.sohu.com/frag/vrs_inc/phb_score_tv_'+url+'_50.js')
	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def SortsI(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('"DIRECTOR":"(.+?)"(.+?)"tv_comment":"(.+?)","MAIN_ACTOR":"(.+?)","tv_score":"(.+?)"(.+?)"tv_big_pic":"(.+?)"(.+?)"tv_url":"(.+?)","tv_name":"(.+?)"').findall(link)
        if len(match)>0:
		li=xbmcgui.ListItem('��ǰλ��:'+name+'  TOP50')
		u=sys.argv[0]+"?mode=40&name="+urllib.quote_plus(name)
		xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
        	for i in range(0,len(match)):
	  	        li=xbmcgui.ListItem(str(i+1)+'.'+match[i][9]+' ('+match[i][4][0:3]+'��)',iconImage='', thumbnailImage=match[i][6])
	  	     	u=sys.argv[0]+"?mode=16&name="+urllib.quote_plus(match[i][9])+"&url="+urllib.quote_plus(match[i][8])+"&director="+urllib.quote_plus(match[i][0])+"&studio="+urllib.quote_plus(match[i][3])+"&plot="+urllib.quote_plus(match[i][2])
	   	    	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def MovieList(name,jsona,jsonf,jsono,jsonc,jsonn):
        if name.find('��ݼ���')!=-1 or name.find('����')!=-1:
                url='http://search.vrs.sohu.com/video_f'+jsonf+'_o'+jsono+'_c'+jsonc+'_s_n'+jsonn+'_p50_chltv.sohu.com_k'+jsona+'.json'
        else:
                name1=''
                for item in jsona.decode('gbk'):
                       name1=name1+"%25u"+"%X"%ord(item)
                       url='http://search.vrs.sohu.com/video_f'+jsonf+'_o'+jsono+'_c'+jsonc+'_s_n'+jsonn+'_p50_chltv.sohu.com_k'+name1+'.json'

        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()

        match=re.compile('"totalCount":(.+?),"').findall(link)
        paget=abs(int(match[0])/-50)
        if paget>0:
		li=xbmcgui.ListItem('��ǰλ��:'+name+'  ��'+jsonn+'/'+str(paget)+'ҳ')
		u=sys.argv[0]+"?mode=40&name="+urllib.quote_plus(name)
		xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
                if int(jsonn)>1:
			li=xbmcgui.ListItem('..��һҳ')
			u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name)+"&jsona="+urllib.quote_plus(jsona)+"&jsonf="+urllib.quote_plus(jsonf)+"&jsono="+urllib.quote_plus(jsono)+"&jsonc="+urllib.quote_plus(jsonc)+"&jsonn="+urllib.quote_plus('1')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
			li=xbmcgui.ListItem('..��һҳ')
			u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name)+"&jsona="+urllib.quote_plus(jsona)+"&jsonf="+urllib.quote_plus(jsonf)+"&jsono="+urllib.quote_plus(jsono)+"&jsonc="+urllib.quote_plus(jsonc)+"&jsonn="+urllib.quote_plus(str(int(jsonn)-1))
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
                if int(jsonn)<paget:
			li=xbmcgui.ListItem('..��һҳ')
			u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name)+"&jsona="+urllib.quote_plus(jsona)+"&jsonf="+urllib.quote_plus(jsonf)+"&jsono="+urllib.quote_plus(jsono)+"&jsonc="+urllib.quote_plus(jsonc)+"&jsonn="+urllib.quote_plus(str(int(jsonn)+1))
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
			li=xbmcgui.ListItem('..���ҳ')
			u=sys.argv[0]+"?mode=15&name="+urllib.quote_plus(name)+"&jsona="+urllib.quote_plus(jsona)+"&jsonf="+urllib.quote_plus(jsonf)+"&jsono="+urllib.quote_plus(jsono)+"&jsonc="+urllib.quote_plus(jsonc)+"&jsonn="+urllib.quote_plus(str(paget))
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

                match=re.compile('"videoDirector":"(.+?)"(.+?)"videoUrl":"(.+?)"(.+?)"videoBigPic":"(.+?)","videoName":"(.+?)"(.+?)"videoActor":"(.+?)"(.+?)"videoScore":(.+?),"(.+?)"videoDesc":"(.+?)"').findall(link)
                for i in range(0,len(match)):
	        	li=xbmcgui.ListItem(str(i+1)+'.'+match[i][5]+' ('+match[i][9][0:3]+'��)',iconImage='', thumbnailImage=match[i][4])
	        	u=sys.argv[0]+"?mode=16&name="+urllib.quote_plus(match[i][5])+"&url="+urllib.quote_plus(match[i][2])+"&director="+urllib.quote_plus(match[i][0])+"&studio="+urllib.quote_plus(match[i][7])+"&plot="+urllib.quote_plus(match[i][11])
	        	xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)

def MovieId(name,url,director,studio,plot):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=re.sub(' ','',link)
        match=re.compile('varvid="(.+?)";').findall(link)
        vid=match[0]
        match=re.compile('varpid="(.+?)";').findall(link)
        pid=match[0]

        url='http://hot.vrs.sohu.com/vrs_videolist.action?vid='+vid+'&pid='+pid
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('"videoImage":"(.+?)"(.+?)"videoId":(.+?),"(.+?)"videoName":"(.+?)"').findall(link)
        if len(match)>0:
		li=xbmcgui.ListItem('��ǰӰ������:'+name)
		u=sys.argv[0]+"?mode=40&name="+urllib.quote_plus(name)
		xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
                for i in range(0,len(match)):
                        li=xbmcgui.ListItem(str(i+1)+'.'+match[i][4],match[i][0],match[i][0])
                        li.setInfo(type="Video",infoLabels={"Title":match[i][4],"Director":director,"Studio":studio,"Plot":plot})
                	u=sys.argv[0]+"?mode=17&name="+urllib.quote_plus(match[i][4])+"&url="+urllib.quote_plus(match[i][2])+"&thumb="+urllib.quote_plus(match[i][0])+"&director="+urllib.quote_plus(director)+"&studio="+urllib.quote_plus(studio)+"&plot="+urllib.quote_plus(plot)
	                xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li)  

def MoviePlay(name,url,thumb,director,studio,plot):
        url='http://hot.vrs.sohu.com/vrs_flash.action?vid='+url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('"clipsURL"\:\["(.+?)"\]').findall(link)
        paths=match[0].split('","')
        playlist=xbmc.PlayList(1)
        playlist.clear()
        for i in range(0,len(paths)):
	        listitem=xbmcgui.ListItem(name,thumb,thumb)
                listitem.setInfo(type="Video",infoLabels={"Title":name,"Director":director,"Studio":studio,"Plot":plot})
                playlist.add(paths[i], listitem)
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

params=get_params()
mode=None
name=None
url=None
thumb=None
jsona=None
jsonf=None
jsono=None
jsonc=None
jsonn=None
director=None
studio=None
plot=None


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
        jsona=urllib.unquote_plus(params["jsona"])
except:
        pass
try:
        jsonf=urllib.unquote_plus(params["jsonf"])
except:
        pass
try:
        jsono=urllib.unquote_plus(params["jsono"])
except:
        pass
try:
        jsonc=urllib.unquote_plus(params["jsonc"])
except:
        pass
try:
        jsonn=urllib.unquote_plus(params["jsonn"])
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


if mode==None:
	name=''
	Roots()

elif mode==1:
	Channels(name)

elif mode==2:
	ListsA(name)

elif mode==3:
	ListsB(name)

elif mode==4:
	ListsC(name)

elif mode==5:
	ListsD(name,jsona,jsonf)

elif mode==6:
	SortsA(name)

elif mode==7:
	SortsB(name)

elif mode==8:
	SortsC(url,name)

elif mode==9:
	SortsD(url,name)

elif mode==10:
	SortsE(url,name)

elif mode==11:
	SortsF(url,name)

elif mode==12:
	SortsG(url,name)

elif mode==13:
	SortsH(url,name)

elif mode==14:
	SortsI(url,name)

elif mode==15:
	MovieList(name,jsona,jsonf,jsono,jsonc,jsonn)

elif mode==16:
	MovieId(name,url,director,studio,plot)

elif mode==17:
	MoviePlay(name,url,thumb,director,studio,plot)

xbmcplugin.setPluginCategory(int(sys.argv[1]), name )
xbmcplugin.endOfDirectory(int(sys.argv[1]))

    
