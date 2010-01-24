import os,re,xbmcplugin,xbmcgui,xbmc,string,sys
from mystocks_lib import *

class Main:
    def __init__( self ):
        addDir(u'我的自选'.encode('utf8'),url='',mode='show_info',shsz='',folder=True)
        addDir(u'大盘指数'.encode('utf8'),url='',mode='show_dp',shsz='',folder=True)
        addDir(u'股票搜索'.encode('utf8'),url='',mode='show_search',shsz='',folder=True)
        addDir(u'股票排行'.encode('utf8'),url='',mode='show_ph',shsz='',folder=True)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))