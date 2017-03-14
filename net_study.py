#encoding=utf-8
import urllib
import urllib2
import re

def web_easy_content_filter(url,pattern):
	content = get(url,headers=about_header())
	return re.findall(pattern, content,re.S)


def web_custom_request(req,timeout = 5,log = False,proxy_url=None):
	user_proxy(proxy_url)
	try:
		response = urllib2.urlopen(req,timeout=timeout)
	except urllib2.HTTPError, e:
		if hasattr(e,"reason"):
			print "页面访问失败[HTTPError %d]" % e.code+"，原因:"+str(e.reason)
		return None
	except urllib2.URLError,e:
		if hasattr(e,"reason"):
			print "页面访问失败，原因："+str(e.reason)
		return None
	except Exception,e:
		if hasattr(e,"reason"):
			print "页面访问失败，原因："+str(e.reason)
		return None
	content = response.read()
	if log:
		print url
		print params
		print content
	response.close()
	return content


def post(url,params=None,timeout = 5,log = False,headers = {},proxy_url=None):
	data = None
	if params != None:
		data = urllib.urlencode(params)
	request = urllib2.Request(url,data,headers=headers)
	return web_custom_request(request,timeout,log,proxy_url)

def get(url,params=None,timeout = 5,log = False,headers = {},proxy_url=None):
	if params != None:
		data = urllib.urlencode(params)
	else:
		data = ''
	url = url + "?" + data
	request = urllib2.Request(url,headers=headers)
	return web_custom_request(request,timeout,log,proxy_url)


def web_api(url,params=None,method = 'get',timeout = 5,log = False,headers = {},proxy_url=None):
	if method is 'get':
		return get(url, params,timeout,log,headers,proxy_url)
	elif method is 'post':
		return post(url, params,timeout,log,headers,proxy_url)
	else:
		raise NotImplementedError("the method not implement")

#关于header
def about_header():
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	referer = 'http://www.zhihu.com/articles'
	content_type = 'application/xml'
	accept_encoding = 'gzip,deflate'
	accept_language = 'zh-cn'
	connection = 'keep-alive'
	headers = {'User-Agent' : user_agent,'Referer':referer,'Content-Type':content_type,'Accept-Encoding':accept_encoding,
	'Accept-Language':accept_language,'Connection':connection}
	return headers

#关于Proxy(代理)
#urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy
#假如一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问
#所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理
def user_proxy(proxy_url):
	proxy_handler = urllib2.ProxyHandler({'http':proxy_url})
	null_proxy_handler = urllib2.ProxyHandler({})
	if proxy_url != None:
		opener = urllib2.build_opener(proxy_handler)
	else:
		opener = urllib2.build_opener(null_proxy_handler)
	urllib2.install_opener(opener)

#关于Debuglog
# import urllib2
# httpHandler = urllib2.HTTPHandler(debuglevel=1)
# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHandler, httpsHandler)
# urllib2.install_opener(opener)
# response = urllib2.urlopen('http://www.baidu.com')

if __name__ == "__main__":
	web_api("http://blog.stackoverflow.com",method='get',log=True)
