#encoding=utf-8
import net_study

def getHeader():
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0'
	referer = 'http://172.16.16.241:3100/upyunLog/view/index.html'
	content_type = 'application/json;charset=utf-8'
	accept_encoding = 'gzip, deflate'
	accept_language = 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
	connection = 'keep-alive'
	content_length = '86'
	headers = {'User-Agent' : user_agent,'Referer':referer,'Content-Type':content_type,'Accept-Encoding':accept_encoding,
	'Accept-Language':accept_language,'Connection':connection,'Content_Length':content_length}
	return headers

def create_req(uid,time,prefix):
	req_url = "http://172.16.16.241:3100/upyunLog/api/readNormalLogList"
	startTime = "2017-%sT02:22:00.000Z" % time
	print startTime
	pathComponent = "%s%s"%(prefix,uid) 
	print pathComponent
	params = {"startTime":startTime,"clientType":"IGS","pathComponent":pathComponent}
	content = net_study.post(req_url,params=params,headers=getHeader())
	print content

create_req("376537","05-26","S_")