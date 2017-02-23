#coding=utf-8 
# 中文注释
import os
def rename(filepath,trans_func):
	"""
	重命名
	:param filepath:全路径 
	:param trans_func:名称替换的函数
	"""
	_dir,_filename = os.path.split(filepath)
	_filename = trans_func(_filename)
	os.rename(filepath, os.path.join(_dir,_filename))

def list_all_file(rootDir,format_suffix,trans_func):
	"""
	遍历文件夹下所有文件，并且重命名	
	:param rootDir:根目录 
	:param format_suffix:文件格式
	:param trans_func:名称替换的函数
	"""
	for f in os.listdir(rootDir):
		all_path = os.path.join(rootDir,f)
		if os.path.isfile(all_path):
			if os.path.splitext(all_path)[1] != ("."+format_suffix):
				rename(all_path,trans_func)
		else:
			list_all_file(all_path,format_suffix,trans_func)

if __name__ == "__main__":
	list_all_file(os.path.expanduser("~/Desktop/python/"),"py",lambda filename:'py_'+filename)