import sys
import os
import xbmc
import string
import tempfile,urllib2,urllib,struct,gzip,StringIO,md5,xml.dom.minidom
__scriptname__ = "ShooterSub"
__author__ = "rabbitgg"
__version__ = "0.20"


class CustomLoader:
    def __init__(self, listFile):
        self.listFile = listFile
        self.listXML = None
        self.node = []
        self.currfeed = []
        self.hasXML = self.loadList()

    def loadList(self):
        try:
            f = open(self.listFile)
        except IOError:
            print "XML File could not be opened"
            return False
        fl = f.read()
        f.close()
        try:
            self.listXML = xml.dom.minidom.parseString(fl)
        except:
            print "parse error"
            return False
        return True

    def getText(self, nodelist):
        rc = ""
        for node in nodelist.childNodes:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data.encode('utf8')
        return rc

    def getStockList(self):
        stocks = self.listXML.getElementsByTagName("customPath")
        for stock in stocks:
            node = stock.getElementsByTagName("hasPath")[0]
            self.currfeed.append(self.getText(node))
            node = stock.getElementsByTagName("pathName")[0]
            self.currfeed.append(self.getText(node))
            node = stock.getElementsByTagName("destCode")[0]
            self.currfeed.append(self.getText(node))

#if  not xbmc.getCondVisibility('videoplayer.isfullscreen') :
if  not xbmc.Player().isPlayingVideo():
    import xbmcgui
    dialog = xbmcgui.Dialog()
    selected = dialog.ok("ShooterSub", "请先播放一个视频再执行这个脚本，或从播放菜单中执行".decode('gbk').encode('utf8') ,"更多具体信息请访问： ".decode('gbk').encode('utf8'), "http://bbs.htpc1.com/forum-225-1.html".decode('gbk').encode('utf8') )
else:
    window = False
    skin = "main"
    skin1 = str(xbmc.getSkinDir().lower())
    skin1 = skin1.replace("-"," ")
    skin1 = skin1.replace("."," ")
    skin1 = skin1.replace("_"," ")
    if ( skin1.find( "eedia" ) > -1 ):
        skin = "MiniMeedia"
    if ( skin1.find( "tream" ) > -1 ):
        skin = "MediaStream"
    if ( skin1.find( "edux" ) > -1 ):
        skin = "MediaStream_Redux"
    if ( skin1.find( "aeon" ) > -1 ):
        skin = "Aeon"
    if ( skin1.find( "alaska" ) > -1 ):
        skin = "Aeon"
    if ( skin1.find( "confluence" ) > -1 ):
        skin = "confluence"	
   
    print "ShooterSub version [" +  __version__ +"]"
    print "Skin Folder: [ " + skin1 +" ]"
    print "ShooterSub skin XML: [ " + skin +" ]"
    
    if ( __name__ == "__main__" ):
        if not xbmc.getCondVisibility('Player.Paused') : xbmc.Player().pause()
        movieFullPath = xbmc.Player().getPlayingFile()
        pathSetting = CustomLoader(os.path.normpath(os.path.join(os.getcwd(),"customPath.xml")))
        
        hasPath = False
        pathName = '';
        destCode = 'gbk'
        
        if(pathSetting.hasXML == True):
            pathSetting.getStockList()
            hasPath = pathSetting.currfeed[0]
            pathName = pathSetting.currfeed[1]
            destCode = pathSetting.currfeed[2]
            
            
        try:
            file=open(movieFullPath,"rb")
        except IOError:
            print "File could not be opened"
            sys.exit(1)


        #statinfo = os.stat(movieFullPath)

        BlockSize = 4096
        NumOfSegments = 4

        #fileLength = statinfo.st_size
        fileLength = os.path.getsize(movieFullPath)
        #print fileLength
        offset = []
        offset.append(BlockSize)
        offset.append(fileLength / 3 * 2)
        offset.append(fileLength / 3)
        offset.append(fileLength - 8192)

        buff = []
        strHash = ''

        for i in range(0,NumOfSegments):
          file.seek(offset[i])
          buff = file.read(BlockSize)
          if (len(strHash) > 0):
             strHash += ";"
          m = md5.new()
          m.update(buff)
          strHash += m.hexdigest()
          #strHash += hashlib.new("md5", buff).hexdigest()

        #print strHash

        #print offset
        file.close()

        Boundary='----------------------------767a02e50d82'
        url = 'http://svplayer.shooter.cn/api/subapi.php'
        user_agent = 'SPlayer Build 580'
        ContentType = "multipart/form-data; boundary=----------------------------767a02e50d82"
        dataValue = 'Content-Disposition: form-data; name='

        headers = { 'User-Agent' : user_agent,
                    'Content-Type' : ContentType,
                    'Connection' : 'Keep-Alive',
                    'Expect' : '100-continue'}

        realData = '--' + Boundary + '\r\n' + dataValue + "\"pathinfo\"\r\n\r\n" + movieFullPath + '\r\n'
        realData += '--' + Boundary + '\r\n' + dataValue + "\"filehash\"\r\n\r\n" + strHash + '\r\n'
        realData += '--' + Boundary + '--\r\n'


        req = urllib2.Request(url, realData, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        #temp = open('E:\\temp','wb')
        #temp.write(the_page)
        #temp.close()
        if(len(the_page) > 2):
            # 字幕个数
            NumOfSub = ord(the_page[:1])
            #print NumOfSub
            fileLen = 0
            nowPos = 1
            for i in range(0, NumOfSub):
                # 包长度
                packLen = struct.unpack('!L',the_page[nowPos:nowPos+4])
                nowPos += 4
                # 描述长度
                desLen = struct.unpack('!L',the_page[nowPos:nowPos+4])
                nowPos += desLen[0] + 4
                subPack = ord(the_page[nowPos+4:nowPos+5])
                nowPos += 9
                # 扩展名长度
                #print repr(the_page[nowPos:nowPos+4])
                extLen = struct.unpack('!L',the_page[nowPos:nowPos+4])
                nowPos += 4
                # 文件扩展名
                fileExt = the_page[nowPos:nowPos+extLen[0]]
                nowPos += extLen[0]
                #print fileExt
                fileLen = struct.unpack('!L',the_page[nowPos:nowPos+4])
                nowPos += 4
                #print "描述长度是：%d,扩展名长度：%d,扩展名：%s,文件长度：%d" % (desLen[0],extLen[0],fileExt,fileLen[0])
                
                fileName = movieFullPath[:-4] + '.chs' + str(i) +'.' + fileExt
                #print fileName
                org_file = the_page[nowPos:nowPos+fileLen[0]]
                if(hasPath == 'True'):
                   zip_file = open(os.path.join(pathName,os.path.basename(fileName)),'wb')
                else:
                   zip_file = open(fileName,'wb')
                
                #处理压缩文件
                if ((ord(org_file[0]) == 31) and (ord(org_file[1]) == 139) and (ord(org_file[2]) == 8)) :
                    compressedstream = StringIO.StringIO(org_file)
                    f = gzip.GzipFile(fileobj=compressedstream)      
                    data = f.read()
                    #是UTF-16编码
                    if((ord(data[0]) == 255) and (ord(data[1]) == 254)):
                        temp_data = unicode(data[2:],'utf-16')
                        zip_file.write(temp_data.encode('gbk'))
                    else:
                        zip_file.write(data)
                else:
                    data = the_page[nowPos:nowPos+fileLen[0]]
                    #是UTF-16编码
                    if((ord(data[0]) == 255) and (ord(data[1]) == 254)):
                        temp_data = unicode(data[2:],'utf-16')
                        zip_file.write(temp_data.encode('gbk'))
                    else:
                        zip_file.write(data)
                    #zip_file.write(the_page[nowPos:nowPos+fileLen[0]])
                zip_file.close()
                nowPos += fileLen[0]
                
                if(subPack > 1):
                    extLen = struct.unpack('!L',the_page[nowPos+4:nowPos+8])
                    nowPos += 8
                   # 文件扩展名
                    fileExt = the_page[nowPos:nowPos+extLen[0]]
                    nowPos += extLen[0]
                    #print fileExt
                    fileLen = struct.unpack('!L',the_page[nowPos:nowPos+4])
                    nowPos += 4
                    fileName = movieFullPath[:-4] + '.chs' + str(i) +'.' + fileExt
                    #print fileName
                    org_file = the_page[nowPos:nowPos+fileLen[0]]
                    if(hasPath == 'True'):
                       zip_file = open(os.path.join(pathName,os.path.basename(fileName)),'wb')
                    else:
                       zip_file = open(fileName,'wb')
                       
                    #处理压缩文件
                    if ((ord(org_file[0]) == 31) and (ord(org_file[1]) == 139) and (ord(org_file[2]) == 8)) :
                        compressedstream = StringIO.StringIO(org_file)
                        f = gzip.GzipFile(fileobj=compressedstream)      
                        data = f.read()
                        #是UTF-16编码
                        if((ord(data[0]) == 255) and (ord(data[1]) == 254)):
                            temp_data = unicode(data[2:],'utf-16')
                            zip_file.write(temp_data.encode('gbk'))
                        else:
                            zip_file.write(data)
                    else:
                        data = the_page[nowPos:nowPos+fileLen[0]]
                        #是UTF-16编码
                        if((ord(data[0]) == 255) and (ord(data[1]) == 254)):
                            temp_data = unicode(data[2:],'utf-16')
                            zip_file.write(temp_data.encode('gbk'))
                        else:
                            zip_file.write(data)
                        #zip_file.write(the_page[nowPos:nowPos+fileLen[0]])
                    zip_file.close()
                    nowPos += fileLen[0]
                    
                if(hasPath == 'True'):
                   xbmc.Player().setSubtitles(os.path.join(pathName,os.path.basename(fileName)))
                else:
                   xbmc.Player().setSubtitles(fileName)
            #print "完成！共下载%d个字幕文件" % NumOfSub
            import xbmcgui
            dialog = xbmcgui.Dialog()
            selected = dialog.ok("ShooterSub",("完成！共下载%d个字幕文件".decode('gbk').encode('utf8') % NumOfSub))
            
            if xbmc.getCondVisibility('Player.Paused'): xbmc.Player().pause() # if Paused, un-pause
        else:
            import xbmcgui
            dialog = xbmcgui.Dialog()
            selected = dialog.ok("ShooterSub","对不起！没有找到字幕文件".decode('gbk').encode('utf8') )
            if xbmc.getCondVisibility('Player.Paused'): xbmc.Player().pause() # if Paused, un-pause