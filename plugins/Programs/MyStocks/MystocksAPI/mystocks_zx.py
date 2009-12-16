import os,re,xbmcplugin,xbmcgui,xbmc,string,sys,xml.dom.minidom
from mystocks_lib import *

class Main:
    def __init__( self ):
        params=get_params()
        
        name=None
        shsz=None
        url=None
        zx=None
        
        try:
            name=urllib.unquote_plus(params["name"])
        except:
            pass
            
        try:
            shsz=urllib.unquote_plus(params["shsz"])
        except:
            pass
        
        try:
            url=urllib.unquote_plus(params["url"])
        except:
            pass
            
        try:
            zx=urllib.unquote_plus(params["zx"])
        except:
            pass
         
        name = name.strip() 
        if (" " in name):
           orgname = name.split(" ")
           name=orgname[0]
        
        if(zx == "yes"):
          stockList = CustomLoader("%s\\%s" % (os.getcwd(),"customStocks.xml"))
          stockList.getStockList()
          stockList.delNode(url)
        else:
          stockList = CustomLoader("%s\\%s" % (os.getcwd(),"customStocks.xml"))
          stockList.newXML(url,name,shsz)