import sys
import os
import xbmc
import xbmcgui
import xbmcplugin
import urllib
import re
from mystocks_lib import *

class Main:
    def __init__( self ):
        addDir(u'上证涨幅'.encode('utf8'),url=r'http://hq.sinajs.cn/list=stock_sh_up',mode='show_co_detail',shsz='',folder=True)
        addDir(u'上证跌幅'.encode('utf8'),url=r'http://hq.sinajs.cn/list=stock_sh_down',mode='show_co_detail',shsz='',folder=True)
        addDir(u'深证涨幅'.encode('utf8'),url=r'http://hq.sinajs.cn/list=stock_sz_up',mode='show_co_detail',shsz='',folder=True)
        addDir(u'深证跌幅'.encode('utf8'),url=r'http://hq.sinajs.cn/list=stock_sz_down',mode='show_co_detail',shsz='',folder=True)
        addDir(u'上证振幅'.encode('utf8'),url=r'http://hq.sinajs.cn/list=stock_sh_range',mode='show_co_detail',shsz='',folder=True)
        addDir(u'深证振幅'.encode('utf8'),url=r'http://hq.sinajs.cn/list=stock_sz_range',mode='show_co_detail',shsz='',folder=True)
        addDir(u'上证成交量'.encode('utf8'),url=r'http://hq.sinajs.cn/list=stock_sh_volume',mode='show_co_detail',shsz='',folder=True)
        addDir(u'上证成交额'.encode('utf8'),url=r'http://hq.sinajs.cn/list=stock_sh_amount',mode='show_co_detail',shsz='',folder=True)
        addDir(u'深证成交量'.encode('utf8'),url=r'http://hq.sinajs.cn/list=stock_sz_volume',mode='show_co_detail',shsz='',folder=True)
        addDir(u'深证成交额'.encode('utf8'),url=r'http://hq.sinajs.cn/list=stock_sz_amount',mode='show_co_detail',shsz='',folder=True)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))