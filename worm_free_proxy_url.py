#encdoing=utf-8
import net_study

url = "http://www.xicidaili.com/nt"
pattern = "<tr class=\".*?>.*?<img.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<a.*?>(.*?)</a>.*?<td.*?>(.*?)</td>.*?<td>(.*?)</td>.*?<td.*?<td.*?<td>(.*?)</td>.*?<td>(.*?)</td>"
result = net_study.web_easy_content_filter(url, pattern)
for ip,port,addr,isAppear,type_v,live_days,time in result:
	print ip,port,addr,isAppear,type_v,live_days,time


