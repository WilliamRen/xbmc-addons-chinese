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
    #0����������·������Ʊ���֣�
    #1����27.55�壬���տ��̼ۣ�                41
    #2����27.25�壬�������̼ۣ�                41
    #3����26.91�壬��ǰ�۸�                  40
    #4����27.55�壬������߼ۣ�                43
    #5����26.20�壬������ͼۣ�                44
    #6����26.91�壬����ۣ�������һ�����ۣ�
    #7����26.92�壬�����ۣ�������һ�����ۣ�
    #8����22114263�壬�ɽ��Ĺ�Ʊ�������ڹ�Ʊ������һ�ٹ�Ϊ������λ��������ʹ��ʱ��ͨ���Ѹ�ֵ����һ�٣�
    #9����589824680�壬�ɽ�����λΪ��Ԫ����Ϊ��һĿ��Ȼ��ͨ���ԡ���Ԫ��Ϊ�ɽ����ĵ�λ������ͨ���Ѹ�ֵ����һ��
    #10����4695�壬����һ������4695�ɣ���47�֣�
    #11����26.91�壬����һ�����ۣ�
    #12����57590�壬�������
    #13����26.90�壬�������
    #14����14700�壬��������
    #15����26.89�壬��������
    #16����14300�壬�����ġ�
    #17����26.88�壬�����ġ�
    #18����15100�壬�����塱
    #19����26.87�壬�����塱
    #20����3100�壬����һ���걨3100�ɣ���31�֣�
    #21����26.92�壬����һ������
    #(22, 23), (24, 25), (26,27), (28, 29)�ֱ�Ϊ���������������ĵ������
    #30����2008-01-11�壬���ڣ�
    #31����15:05:32�壬ʱ�䣻
    #
    def getCurr( self ):
        re = urllib2.Request(r'http://hq.sinajs.cn/list=%s' % (self.stockid,))
        rs = urllib2.urlopen(re).read()
        rs = rs[rs.find('"') +1:-2]
        curr = rs.split(',')
        
        zd = round(((float(curr[3]) - float(curr[2])) / float(curr[2]) * 100),2)
        zdj = round((float(curr[3]) - float(curr[2])),2)
        
        
        if(float(curr[3]) > float(curr[2])):
             self.getControl( 40 ).setLabel("[COLOR=FFFF0000][B]" + str(round(float(curr[3]),2)) + "[/B][/COLOR]")   #��ǰ�۸�
             self.getControl( 39 ).setLabel("[COLOR=FFFF0000]" + str(zd) + "��[/COLOR]")                                     #�ǵ���
             self.getControl( 38 ).setLabel("[COLOR=FFFF0000]" + str(zdj) + "[/COLOR]") 
        elif (float(curr[3]) < float(curr[2])):
             self.getControl( 40 ).setLabel("[COLOR=FF00FF00][B]" + str(round(float(curr[3]),2)) + "[/B][/COLOR]") 
             self.getControl( 39 ).setLabel("[COLOR=FF00FF00]" + str(zd) + "��[/COLOR]")                                     #�ǵ���
             self.getControl( 38 ).setLabel("[COLOR=FF00FF00]" + str(zdj) + "[/COLOR]")  
        else:
              self.getControl( 40 ).setLabel( str(round(float(curr[3]),2)) ) 
              self.getControl( 39 ).setLabel("%s��" % str(zd))                                     #�ǵ���
              self.getControl( 38 ).setLabel("%s" % str(zdj))   
        
        self.getControl( 41 ).setLabel(curr[2])                                            #����
        
        if(float(curr[1]) > float(curr[2])):
             self.getControl( 42 ).setLabel("[COLOR=FFFF0000]"+curr[1]+"[/COLOR]")             #��
        elif (float(curr[1]) < float(curr[2])):
             self.getControl( 42 ).setLabel("[COLOR=FF00FF00]"+curr[1]+"[/COLOR]")
        else:
             self.getControl( 42 ).setLabel(curr[1])
             
        if(float(curr[4]) > float(curr[2])):
             self.getControl( 43 ).setLabel("[COLOR=FFFF0000]"+curr[4]+"[/COLOR]")             #������߼�
        elif (float(curr[4]) < float(curr[2])):
             self.getControl( 43 ).setLabel("[COLOR=FF00FF00]"+curr[4]+"[/COLOR]")
        else:
             self.getControl( 43 ).setLabel(curr[1])
             
        if(float(curr[5]) > float(curr[2])):
             self.getControl( 44 ).setLabel("[COLOR=FFFF0000]"+curr[5]+"[/COLOR]")             #������ͼ�
        elif (float(curr[5]) < float(curr[2])):
             self.getControl( 44 ).setLabel("[COLOR=FF00FF00]"+curr[5]+"[/COLOR]")
        else:
             self.getControl( 44 ).setLabel(curr[5])
             
        self.getControl( 45 ).setLabel(str(int(round((float(curr[8]) / 100),0))))                  #�ɽ��Ĺ�Ʊ��
        self.getControl( 46 ).setLabel(str(int(round((float(curr[9]) / 10000),0))))                #�ɽ����
        
        self.getControl( 51 ).setLabel("%s/%s" % (curr[11],str(int(round((float(curr[10]) / 100),0)))))  #��һ
        self.getControl( 61 ).setLabel("%s/%s" % (curr[21],str(int(round((float(curr[20]) / 100),0)))))  #��һ
        self.getControl( 52 ).setLabel("%s/%s" % (curr[13],str(int(round((float(curr[12]) / 100),0)))))  #���
        self.getControl( 62 ).setLabel("%s/%s" % (curr[23],str(int(round((float(curr[22]) / 100),0)))))  #����
        self.getControl( 53 ).setLabel("%s/%s" % (curr[15],str(int(round((float(curr[14]) / 100),0)))))  #����
        self.getControl( 63 ).setLabel("%s/%s" % (curr[25],str(int(round((float(curr[24]) / 100),0)))))  #���� 
        self.getControl( 54 ).setLabel("%s/%s" % (curr[17],str(int(round((float(curr[16]) / 100),0)))))  #����
        self.getControl( 64 ).setLabel("%s/%s" % (curr[27],str(int(round((float(curr[26]) / 100),0)))))  #���� 
        self.getControl( 55 ).setLabel("%s/%s" % (curr[19],str(int(round((float(curr[18]) / 100),0)))))  #����
        self.getControl( 65 ).setLabel("%s/%s" % (curr[29],str(int(round((float(curr[28]) / 100),0)))))  #���� 
    
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
            self.getControl( 23 ).setLabel("��ѡ�Ƴ�")
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