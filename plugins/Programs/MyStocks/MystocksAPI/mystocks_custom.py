import xml.dom.minidom,xbmcplugin,xbmcgui,os,xbmc,string,sys
from mystocks_lib import *

       
class Main:
    def __init__(self):
        stockList = CustomLoader("%s\\%s" % (os.getcwd(),"customStocks.xml"))
        if(stockList.hasXML == True):
            stockList.getStockList()
            for feed in range(len(stockList.currfeed)/3):
                name = stockList.currfeed[feed*3+0]
                id = stockList.currfeed[feed*3+1]
                shsz = stockList.currfeed[feed*3+2]
                addLink(name, id, "show_graph", shsz, folder=False,isZX=True)
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
