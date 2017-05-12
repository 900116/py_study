#encoding=utf-8
import net_study
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
songid = "428591384"
content = net_study.post("http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s?csrf_token=" % songid,{"params":"CZuYwkHNOcloK8cXJ1ibS0pvvfy/BkH81WipMcyzTCVqLggk+waC2w5+cr5jr4T1cinlmsM3vqie7UP+e0l5cwy1AHaCPkVHmUwe505MxFlra1UBcNAt4iuj0Dl+XhO5IvBMj7KHJebsw6stK4lh9F/psyaQDZxcEf+HBT1UEHMybNRkw2McMABEMqdtUlX9","encSecKey":"52c07c7dec0edf386eeb995e7846db76f96561e5ffa3830a2451f8b04223bca871f293ce0b03e8197ab0bee21e56aef37621c0abd21d082ae58428aa104861949153974e1547bc2978b27d3c645774590df123d42806bbf40084e1ccd9ac52de279cfe10caf26b28aacc6053975d7ba67cd92204ba703f1f79924eba51cbe3fc"})
content = content.decode('utf-8')
content = json.loads(content)
hotComments = content["hotComments"]
for x in hotComments:
	print "作者："+x["user"]["nickname"]
	print "内容："+x["content"]
	print "\n"