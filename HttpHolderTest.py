# -*- coding: UTF-8 -*
'''
Created on 2014-04-24
Test case for HttpHolder
@author: RobinTang
'''
import unittest
from HttpHolder import HttpHolder



class HttpHolderTest(unittest.TestCase):
    '''
    Test Case of SinKVDB
    '''
    headers = {
           # Chrome User-Agent
           'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
           }
    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        # 准备HttpHolder实例
        self.http = HttpHolder(headers=HttpHolderTest.headers)
    
    def test0OpenBaidu(self):
        print 'html.len=%d bytes' % (len(self.http.open_html('http://www.baidu.com')))
    
    def test1TimeOut(self):
        try:
            self.http.open_html('http://www.baidu.com', timeout=2)
            print 'not time out'
        except:
            print 'time out'

    def test2Cookies(self):
        # Cookie方面的测试
        self.http.open_html('http://www.baidu.com')
        # get cookies
        cks = self.http.get_cookiesdict()
        print 'get cookies(self.http):'
        for k, v in cks.items():
            print '\t%s=%s' % (k, v)
        
        self.http2 = HttpHolder(headers=HttpHolderTest.headers)
        self.http2.set_cookiesdict(cks)
        self.http2.open_html('http://www.baidu.com')
        print 'get cookies(self.http2):'
        for k, v in self.http2.get_cookiesdict().items():
            print '\t%s=%s' % (k, v)
    
    def test3Url(self):
        # 这个请求会被重定向
        self.http.open('http://t.cn/8s954lJ')
        print 'redirect to: %s' % self.http.geturl()

    def test4Doc(self):
        # 文档对象
        doc = self.http.open('http://www.baidu.com')
        print 'response(%s):' % doc.code
        for k, v in doc.headers.dict.items():
            print '\t%s=%s' % (k, v)
        

if __name__ == '__main__':
    unittest.main()


