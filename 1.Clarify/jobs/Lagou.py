import urllib2
from urllib import urlencode,quote
class Lagou:
     
    @staticmethod
    def getPage(keywords,position,n=1):
        url = 'http://www.lagou.com/jobs/list_'+keywords+'?&spc=1&pl=&gj=&xl=&yx=&gx=&st=&labelWords=&lc=&workAddress=&requestId=&'
        fullUrl = url +'&'+ urlencode({'city':position,'kd':keywords,'pn':n})
        return urllib2.urlopen(fullUrl).read()
        
    
        
         
