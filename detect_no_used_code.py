#encoding=utf-8
import os
import sys
import re
 
class ProgressBar:
  def __init__(self, count = 0, total = 0, width = 50):
    self.count = count
    self.total = total
    self.width = width
  
  def update(self):
    self.count += 1
    self.draw()

  def draw(self):
    sys.stdout.write(' ' * (self.width + 9) + '\r')
    sys.stdout.flush()
    progress = self.width * self.count / self.total
    f_c = float(self.count)
    f_t = float(self.total)
    p_i = int(f_c/f_t * 100) 
    sys.stdout.write('{0:3}%: '.format(p_i))
    sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
    if progress == self.width:
      sys.stdout.write('\n')
    sys.stdout.flush()

class swiftFile:
	def __init__(self):
		self.names = set()
		self.callNames = set()
		self.fp = None

#参数个数
def get_args_count():
	return len(sys.argv)
#主目录
def get_root_path():
	arg_count = get_args_count()
	if arg_count == 2:
		return arg_count[1]
	return "."
#项目目录
def proj_path(root_path):
	for fn in os.listdir(root_path):
		if fn.endswith('.xcodeproj'):
			return root_path + '/' +fn.split('.')[0]
	return None
#图片判定
def	is_image(name):
	return name.endswith('.jpg') or name.endswith('.png')
#源代码
def is_source(name):
	return name.endswith('.swift')
#filterPath
def is_filter(fp):
	return fp.endswith('.launchimage') or fp.endswith('.appiconset')

def class_names(content):
	return set(re.findall('class *([^ ]*?) *:',content,re.S))

def protocol_names(content):
	return set(re.findall('protocol *([^ ]*?) *:',content,re.S))

def enum_names(content):
	return set(re.findall('enum *([^ ]*?) *:',content,re.S))

def struct_names(content):
	return set(re.findall('struct *([^ ]*?) *:',content,re.S))

def callNames(content):
	return set(re.findall('[A-Z][a-zA-Z0-9_]+',content,re.S))

#遍历项目
swiftFiles = []
def walk_path(parent_dir):
	for fn in os.listdir(parent_dir):
		if is_filter(parent_dir):
			continue
		fp = os.path.join(parent_dir,fn)
		if os.path.isfile(fp):
			if is_source(fp):
				sf = swiftFile()
				sf.fp = fp
				content = read_file(fp)
				sf.names |= class_names(content)
				sf.names |= enum_names(content)
				sf.names |= protocol_names(content)
				sf.names |= struct_names(content)
				sf.callNames = callNames(content)
				swiftFiles.append(sf)
		else:
			walk_path(fp)


#读取文件
def read_file(fp):
	with open(fp) as f:
		return f.read()
	return None

#主函数
def main():
	pj_path = proj_path(get_root_path())
	if pj_path == None:
		print("文件夹不符合规范")
		return
	walk_path(pj_path)
	pb = ProgressBar(total = len(swiftFiles))
	use = []
	for sf in swiftFiles:
		#print sf.fp
		pb.update()
		isUse = False #是否有用
		for osf in swiftFiles:
			if osf.fp == sf.fp:
				continue
			if osf.fp.endswith('AfterClassViewController.swfit'):
				print osf.callNames
			if len(sf.names & osf.callNames) > 0:
				isUse = True
				break
		if isUse:
			use.append(sf)
	
	def f_filter(name):
		if name.find('AppDelegate.swift') != -1:
			return False
		if name.find('main.swift') != -1:
			return False
		return True

	lines = [sf.fp+"\n" for sf in (set(swiftFiles) - set(use)) if sf.fp.find('+') == -1]
	lines = filter(f_filter,lines)
	with open("maybeUnusedClass.txt","w") as f:
		f.writelines(lines)

if __name__ == '__main__':
    main()