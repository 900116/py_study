#encoding=utf-8
import gh_file
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class cityData(object):
	def __init__(self,name,code):
		super(cityData, self).__init__()
		self.name = name
		self.code = code

class qu(cityData):
	def __init__(self,name,code):
		super(qu, self).__init__(name,code)

class shi(cityData):
	def __init__(self,name,code):
		super(shi, self).__init__(name,code)
		self.quls = list()
	def addQu(self,q):
		self.quls.append(q)

class sheng(cityData):
	def __init__(self,name,code):
		super(sheng, self).__init__(name,code)
		self.shils = list()
	def addShi(self,s):
		self.shils.append(s)
		

ls = gh_file.read_lines_for_text_file('city_data.txt')
citylist = list()
lastSheng = None
lastShi = None
import re
for line in ls:
	line = line.replace('　','')
	ll = line.split()
	print ll
	code = ll[0]
	name = ll[1]
	if not lastSheng or (code[:2] != lastSheng.code[:2]):
		se = sheng(name, code) 
		citylist.append(se)
		lastSheng  = se
	elif not lastShi or (code[:4] != lastShi.code[:4]):
		# if name == "市辖区":
		# 	name = lastSheng.name
		si = shi(name, code)
		lastSheng.addShi(si)
		lastShi = si
	else:
		# if name == "市辖区":
		# 	continue
		q = qu(name, code)
		lastShi.addQu(q)

basestr = '<?xml version="1.0" encoding="UTF-8"?> \n\
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n\
<plist version="1.0">\n\
<array>\n'
for se in citylist:
	basestr += '	<dict>\n\
		<key>code</key>\n\
		<string>%s</string>\n\
		<key>name</key>\n\
		<string>%s</string>\n\
		<key>shilist</key>\n\
		<array>\n' % (se.code,se.name)

	for si in se.shils:
		basestr += '			<dict>\n\
				<key>code</key>\n\
				<string>%s</string>\n\
				<key>name</key>\n\
				<string>%s</string>\n\
				<key>qulist</key>\n\
				<array>\n' % (si.code,si.name)

		for q in si.quls:
			basestr+='					<dict>\n\
						<key>code</key>\n\
						<string>%s</string>\n\
						<key>name</key>\n\
						<string>%s</string>\n\
					</dict>\n' % (q.code,q.name)

		basestr += '				</array>\n\
			</dict>\n'

	basestr += '		</array>\n\
	</dict>\n'

basestr += '</array>\n\
</plist>\n'

file_obj = open('cityData.plist','w')
file_obj.write(basestr)
file_obj.close()