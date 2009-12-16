import xml.dom.minidom,urllib,urllib2,re,xbmcplugin,xbmcgui,os,xbmc,string,sys
from mystocks_lib import *

class stockGraph( xbmcgui.WindowXMLDialog ):
    # Constants
    ACTION_EXIT_SCRIPT = ( 9, 10, )

    #
    # Init
    #
    def __init__( self, *args, **kwargs ):
        
        # Show dialog window...
        xbmcgui.WindowXML.__init__( self )
        
        # File parameter
        self.title = kwargs[ "info" ]
        self.stockid = kwargs[ "id" ]
        self.isZX = kwargs["isZX"]
        

    #
    # onInit handler
    #
    def onInit( self ):
        xbmcgui.lock()
        self.getControl( 4 ).setLabel("[B]" +self.title + "[/B]")
        if(self.isZX=="yes"):
           self.getControl( 25 ).setLabel("×ÔÑ¡ÒÆ³ö")
        self.setFocus(self.getControl( 20 ))
        self.showMin()
        #self.getControl( 30 ).setText(self.cont)
        xbmcgui.unlock()
    
    #
    # onFocus handler
    #
    def onFocus( self, controlId ):
        if(controlId == 30010):
            self.setFocus(self.getControl( 20 ))
    #
    # onAction handler
    #
    def onAction( self, action ):
        #
        # Exit
        #
        if ( action in self.ACTION_EXIT_SCRIPT ):
           
            # Close window...
            self.close()
        #if ( action == 4 ):
        #   xbmc.executebuiltin('XBMC.PageDown(61)')
        #if ( action == 3 ):
        #    xbmc.executebuiltin('XBMC.PageUp(61)')
            
    def tr_image(self, url,mode):
        re = urllib2.Request(r'http://image.sinajs.cn/newchart/%s/n/%s.gif' % (mode, url,))
        rs = urllib2.urlopen(re).read()
        path = os.path.join(os.getcwd() , "some.png")
        f = open( path, "wb" )
        f.write(rs)
        f.close()
    
    def showMin(self):
        self.tr_image(self.stockid,"min")
        path = os.path.join(os.getcwd() , "some.png")
        self.getControl(100).setImage("")
        self.getControl( 100 ).setImage(path)
     
    def showDaily(self):
        self.tr_image(self.stockid,"daily")
        path = os.path.join(os.getcwd() , "some.png")
        self.getControl(100).setImage("")
        self.getControl( 100 ).setImage(path)
    
    def showWeekly(self):
        self.tr_image(self.stockid,"weekly")
        path = os.path.join(os.getcwd() , "some.png")
        self.getControl(100).setImage("")
        self.getControl( 100 ).setImage(path)
        
    def showMonthly(self):
        self.tr_image(self.stockid,"monthly")
        path = os.path.join(os.getcwd() , "some.png")
        self.getControl(100).setImage("")
        self.getControl( 100 ).setImage(path)
        
    #
    # onClick handler
    #
    def onClick( self, controlId ):
        if controlId == 20:
            self.showMin()
        if controlId == 21:
            self.showDaily()
        if controlId == 22:
            self.showWeekly()
        if controlId == 23:
            self.showMonthly()
        if controlId == 24:
            self.close()
            u=sys.argv[0]+"?url="+urllib.quote_plus(self.stockid[2:])+"&mode=show_detail&shsz="+urllib.quote_plus(self.stockid[0:2])+"&name="+urllib.quote_plus(self.title)
            if (self.isZX == "yes"):
               u += "&zx=yes"
            xbmc.executebuiltin('XBMC.RunPlugin(%s)' % u)
        if controlId == 25:
            if (self.isZX == "yes"):
                stockList = CustomLoader("%s\\%s" % (os.getcwd(),"customStocks.xml"))
                stockList.getStockList()
                stockList.delNode(self.stockid[2:])
            else:
                stockList = CustomLoader("%s\\%s" % (os.getcwd(),"customStocks.xml"))
                stockList.newXML(self.stockid[2:],self.title,self.stockid[0:2])

class Main:
    def __init__(self):
    
        params=get_params()
        
        name=None
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
        
        stockId = shsz + url
        name = name.strip()
        if (" " in name):
           orgname = name.split(" ")
           name=orgname[0]
        stockgraph = stockGraph( "stock_graph.xml", os.getcwd(), "default", info=name, id=stockId, isZX=zx)
        
        stockgraph.doModal()
        del stockgraph