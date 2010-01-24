import xml.dom.minidom,urllib,urllib2,re,xbmcplugin,xbmcgui,os,xbmc,string,sys
from mystocks_lib import *
from threading import Timer

class stockDetail( xbmcgui.WindowXMLDialog ):
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
        self.t =None
    #                                     controlID
    #0：”大秦铁路”，股票名字；
    #1：”27.55″，今日开盘价；                41
    #2：”27.25″，昨日收盘价；                41
    #3：”26.91″，当前价格；                  40
    #4：”27.55″，今日最高价；                43
    #5：”26.20″，今日最低价；                44
    #6：”26.91″，竞买价，即“买一”报价；
    #7：”26.92″，竞卖价，即“卖一”报价；
    #8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
    #9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万；
    #10：”4695″，“买一”申请4695股，即47手；
    #11：”26.91″，“买一”报价；
    #12：”57590″，“买二”
    #13：”26.90″，“买二”
    #14：”14700″，“买三”
    #15：”26.89″，“买三”
    #16：”14300″，“买四”
    #17：”26.88″，“买四”
    #18：”15100″，“买五”
    #19：”26.87″，“买五”
    #20：”3100″，“卖一”申报3100股，即31手；
    #21：”26.92″，“卖一”报价
    #(22, 23), (24, 25), (26,27), (28, 29)分别为“卖二”至“卖四的情况”
    #30：”2008-01-11″，日期；
    #31：”15:05:32″，时间；
    #
    def getCurr( self ):
        re = urllib2.Request(r'http://hq.sinajs.cn/list=%s' % (self.stockid,))
        rs = urllib2.urlopen(re).read()
        rs = rs[rs.find('"') +1:-2]
        curr = rs.split(',')
        
        zd = round(((float(curr[3]) - float(curr[2])) / float(curr[2]) * 100),2)
        zdj = round((float(curr[3]) - float(curr[2])),2)
        
        
        if(float(curr[3]) > float(curr[2])):
             self.getControl( 40 ).setLabel("[COLOR=FFFF0000][B]" + str(round(float(curr[3]),2)) + "[/B][/COLOR]")   #当前价格
             self.getControl( 39 ).setLabel("[COLOR=FFFF0000]" + str(zd) + "％[/COLOR]")                                     #涨跌幅
             self.getControl( 38 ).setLabel("[COLOR=FFFF0000]" + str(zdj) + "[/COLOR]") 
        elif (float(curr[3]) < float(curr[2])):
             self.getControl( 40 ).setLabel("[COLOR=FF00FF00][B]" + str(round(float(curr[3]),2)) + "[/B][/COLOR]") 
             self.getControl( 39 ).setLabel("[COLOR=FF00FF00]" + str(zd) + "％[/COLOR]")                                     #涨跌幅
             self.getControl( 38 ).setLabel("[COLOR=FF00FF00]" + str(zdj) + "[/COLOR]")  
        else:
              self.getControl( 40 ).setLabel( str(round(float(curr[3]),2)) ) 
              self.getControl( 39 ).setLabel("%s％" % str(zd))                                     #涨跌幅
              self.getControl( 38 ).setLabel("%s" % str(zdj))   
        
        self.getControl( 41 ).setLabel(curr[2])                                            #昨收
        
        if(float(curr[1]) > float(curr[2])):
             self.getControl( 42 ).setLabel("[COLOR=FFFF0000]"+curr[1]+"[/COLOR]")             #今开
        elif (float(curr[1]) < float(curr[2])):
             self.getControl( 42 ).setLabel("[COLOR=FF00FF00]"+curr[1]+"[/COLOR]")
        else:
             self.getControl( 42 ).setLabel(curr[1])
             
        if(float(curr[4]) > float(curr[2])):
             self.getControl( 43 ).setLabel("[COLOR=FFFF0000]"+curr[4]+"[/COLOR]")             #今日最高价
        elif (float(curr[4]) < float(curr[2])):
             self.getControl( 43 ).setLabel("[COLOR=FF00FF00]"+curr[4]+"[/COLOR]")
        else:
             self.getControl( 43 ).setLabel(curr[1])
             
        if(float(curr[5]) > float(curr[2])):
             self.getControl( 44 ).setLabel("[COLOR=FFFF0000]"+curr[5]+"[/COLOR]")             #今日最低价
        elif (float(curr[5]) < float(curr[2])):
             self.getControl( 44 ).setLabel("[COLOR=FF00FF00]"+curr[5]+"[/COLOR]")
        else:
             self.getControl( 44 ).setLabel(curr[5])
             
        self.getControl( 45 ).setLabel(str(int(round((float(curr[8]) / 100),0))))                  #成交的股票数
        self.getControl( 46 ).setLabel(str(int(round((float(curr[9]) / 10000),0))))                #成交金额
        
        self.getControl( 51 ).setLabel("%s/%s" % (curr[11],str(int(round((float(curr[10]) / 100),0)))))  #买一
        self.getControl( 61 ).setLabel("%s/%s" % (curr[21],str(int(round((float(curr[20]) / 100),0)))))  #卖一
        self.getControl( 52 ).setLabel("%s/%s" % (curr[13],str(int(round((float(curr[12]) / 100),0)))))  #买二
        self.getControl( 62 ).setLabel("%s/%s" % (curr[23],str(int(round((float(curr[22]) / 100),0)))))  #卖二
        self.getControl( 53 ).setLabel("%s/%s" % (curr[15],str(int(round((float(curr[14]) / 100),0)))))  #买三
        self.getControl( 63 ).setLabel("%s/%s" % (curr[25],str(int(round((float(curr[24]) / 100),0)))))  #卖三 
        self.getControl( 54 ).setLabel("%s/%s" % (curr[17],str(int(round((float(curr[16]) / 100),0)))))  #买四
        self.getControl( 64 ).setLabel("%s/%s" % (curr[27],str(int(round((float(curr[26]) / 100),0)))))  #卖四 
        self.getControl( 55 ).setLabel("%s/%s" % (curr[19],str(int(round((float(curr[18]) / 100),0)))))  #买五
        self.getControl( 65 ).setLabel("%s/%s" % (curr[29],str(int(round((float(curr[28]) / 100),0)))))  #卖五 
    
    def refresh(self):
        xbmcgui.lock()
        self.getCurr()
        xbmcgui.unlock()
        #print "hello world"
        self.t = Timer(30.0,self.refresh)
        self.t.start()
    #
    # onInit handler
    #
    def onInit( self ):
        xbmcgui.lock()
        self.getControl( 4 ).setLabel("[B]" +self.title + "[/B]")
        if (self.isZX=="yes"):
            self.getControl( 23 ).setLabel("自选移出")
        self.getCurr()
        #self.getControl( 30 ).setText(self.cont)
        xbmcgui.unlock()
        self.setFocus( self.getControl ( 22 ) ) 
        self.t=Timer(30.0, self.refresh)
        self.t.start()
    #
    # onFocus handler
    #
    def onFocus( self, controlId ):
        pass

    #
    # onAction handler
    #
    def onAction( self, action ):
        #
        # Exit
        #
        if ( action in self.ACTION_EXIT_SCRIPT ):
            # Close window...
            self.t.cancel()
            self.close()
            
        
    #
    # onClick handler
    #
    def onClick( self, controlId ):
        if(controlId == 22):
            self.t.cancel()
            self.close()
            u=sys.argv[0]+"?url="+urllib.quote_plus(self.stockid[2:])+"&mode=show_graph&shsz="+urllib.quote_plus(self.stockid[0:2])+"&name="+urllib.quote_plus(self.title)
            if(self.isZX == "yes"):
               u = u +  "&zx=yes"
            #print u
            xbmc.executebuiltin('XBMC.RunPlugin(%s)' % u)
        if controlId == 23:
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
           
        stockdetail = stockDetail( "stock_detail.xml", os.getcwd(), "default", info=name, id=stockId, isZX=zx)
           
        stockdetail.doModal()
        del stockdetail