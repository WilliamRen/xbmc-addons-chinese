import os,re,xbmcplugin,xbmcgui,xbmc,string,sys,xml.dom.minidom,urllib2
from mystocks_lib import *

class Main:
    def __init__( self ):
        params=get_params()
        url=None
        multiId=''
        
        try:
            url=urllib.unquote_plus(params["url"])
        except:
            pass
   
        res = urllib2.Request(url)
        rs = urllib2.urlopen(res).read()
        rs = rs[rs.find('"') +1:-2]
        curr = rs.split(',')
        
        for stockId in range(9):
            #print curr[stockId]
            multiId += curr[stockId] + ','
        multiId += curr[10]
        self.getStock(multiId)
            

            
    def getStock(self, id):
        res = urllib2.Request(r'http://hq.sinajs.cn/list=%s' % (id,))
        rs = urllib2.urlopen(res).read()
        match=re.compile('var hq_str_(.+?)";').findall(rs)
        if (len(match) > 0):
            for stock in match:
                stockid = stock[:8]
                stock = stock[stock.find('"') +1:]
                currstock = stock.split(',')
                print len(currstock[0].decode('gbk').encode('utf8') )
                if (len(currstock[0].decode('gbk').encode('utf8')) < 8):
                    sname=currstock[0].decode('gbk').encode('utf8') + "  "
                else:
                    sname = currstock[0].decode('gbk').encode('utf8') 
                stockname = "%-12s%12s%6s%12s%6s%12s%6s%12s%6s%12s%8s" % (sname ,"现价：".decode('gbk').encode('utf8') , 
                                            currstock[3] , "涨跌：".decode('gbk').encode('utf8') , str(float(currstock[3])-float(currstock[2])) ,
                                            "涨幅：".decode('gbk').encode('utf8') , str(round(((float(currstock[3]) - float(currstock[2])) / float(currstock[2]) * 100),2))+"％".decode('gbk').encode('utf8') ,
                                            "成交：".decode('gbk').encode('utf8') , str(int(round((float(currstock[8]) / 100),0))),
                                            "金额：".decode('gbk').encode('utf8') , str(int(round((float(currstock[9]) / 10000),0))),
                                            )
                addLink(stockname, stockid[2:], "show_graph", stockid[:2], folder=False)
            xbmcplugin.endOfDirectory(int(sys.argv[1]))