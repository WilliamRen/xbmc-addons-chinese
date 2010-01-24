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
        addLink(u"上证指数".encode('utf8'),"000001","show_graph","sh",folder=False)
        addLink(u"深证成指".encode('utf8'),"399001","show_graph","sz",folder=False)
        addLink(u"中小板指".encode('utf8'),"399005","show_graph","sz",folder=False)
        addLink(u"上证B指".encode('utf8'),"000003","show_graph","sh",folder=False)
        addLink(u"深证B指".encode('utf8'),"399108","show_graph","sz",folder=False)
        addLink(u"沪深300".encode('utf8'),"399300","show_graph","sz",folder=False)
        addLink(u"上证180".encode('utf8'),"000010","show_graph","sh",folder=False)
        addLink(u"深证100".encode('utf8'),"399004","show_graph","sz",folder=False)
        addLink(u"上证基金".encode('utf8'),"000011","show_graph","sh",folder=False)
        addLink(u"深证基金".encode('utf8'),"399305","show_graph","sz",folder=False)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))