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
#遍历项目
imageFiles = []
sourceFiles = []
def walk_path(parent_dir):
	for fn in os.listdir(parent_dir):
		if is_filter(parent_dir):
			continue
		fp = os.path.join(parent_dir,fn)
		if os.path.isfile(fp):
			iname = (os.path.split(fp)[1]).split('.')[0]
			if is_image(fp):
				if iname.endswith('@2x'):
					iname = iname[:-3]
				imageFiles.append((iname,fp))
			if is_source(fp):
				sourceFiles.append(fp)
		else:
			walk_path(fp)
#读取文件
def read_file(fp):
	with open(fp) as f:
		return f.read()
	return None

#存储数据
def save():
	with open('unusedImageNames.txt','w') as f:
		f.writelines([iname+"\n" for iname,fp in imageFiles])
	with open('unusedImagePaths.txt','w') as f:
		f.writelines([fp+"\n" for iname,fp in imageFiles])

#主函数
def main():
	pj_path = proj_path(get_root_path())
	if pj_path == None:
		print("文件夹不符合规范")
		return
	walk_path(pj_path)
	i = 1
	p = ProgressBar(total = len(sourceFiles))
	for fp in sourceFiles:
		content = read_file(fp)
		p.update()
 		i += 1
		for iname,tfp in imageFiles[:]:
			regex = '[\"\']'+iname+'(@2x)?(.jpg|.png)?[\"\']'
			res = re.findall(regex,content,re.S)
			if len(res) > 0:
				imageFiles.remove((iname,tfp))
	save()

if __name__ == '__main__':
    main()