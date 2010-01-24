import sys
import os
import xbmc
import xbmcgui
import xbmcplugin
import urllib2
import re
from mystocks_lib import *

class Main:
    def __init__( self ):
        keyboard = xbmc.Keyboard('')
        keyboard.doModal()
        if (keyboard.isConfirmed()):
          self._search(keyboard.getText())
        

    def _search( self, inText):
        req = urllib2.Request('http://biz.finance.sina.com.cn/suggest/lookup_n.php?country=stock&q=' + inText)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match0=re.sub('\r','',link)
        match0=re.sub('\n','',match0)
        print sys.getdefaultencoding()
        match=re.compile('<title>检索结果_新浪财经_新浪网</title>').findall(match0)
        if (len(match) > 0):
            match=re.compile('<div>沪深股市</div>(.+?)<div class="clear"></div>').findall(match0)
            try:
                match2=re.compile('target="_blank">(.+?)</a></label>').findall(match[0])
                if (len(match2) > 0):
                    for info in match2:
                        re_v = info.split(' ')
                        if(len(re_v[0]) == 8):
                            addLink(re_v[1].decode('gbk').encode('utf8'), re_v[0][2:], "show_graph", re_v[0][:2], folder=False)
                    xbmcplugin.endOfDirectory(int(sys.argv[1]))
            except:
                ok = xbmcgui.Dialog().ok('股票搜索', '对不起，没有找到相关股票。')
                u=sys.argv[0]+"?url=&mode=&shsz=&name="
                xbmc.executebuiltin('XBMC.RunPlugin(%s)' % u)
        else:
            match=re.compile('var fullcode="(.+?)";').findall(match0)
            if(len(match) > 0):
                stockId = match[0]
                match=re.compile('var stockname="(.+?)";').findall(match0)
                stockName = match[0]
                addLink(stockName.decode('gbk').encode('utf8'), stockId[2:], "show_graph", stockId[:2], folder=False)
                xbmcplugin.endOfDirectory(int(sys.argv[1]))
            else:
                ok = xbmcgui.Dialog().ok('股票搜索', '对不起，没有找到相关股票。')
                u=sys.argv[0]+"?url=&mode=&shsz=&name="
                xbmc.executebuiltin('XBMC.RunPlugin(%s)' % u)