#coding=utf-8 
# 中文注释
import os
def rename(filepath,trans_func):
	_dir,_filename = os.path.split(filepath)
	_filename = trans_func(_filename)
	os.rename(filepath, os.path.join(_dir,_filename))

def list_all_file(rootDir,format_suffix,trans_func):
	for f in os.listdir(rootDir):
		all_path = os.path.join(rootDir,f)
		if os.path.isfile(all_path):
			if all_path.endswith("."+format_suffix):
				rename(all_path,trans_func)
		else:
			list_all_file(all_path,format_suffix,trans_func)

list_all_file(os.path.expanduser("~/Desktop/python/"),"py",lambda filename:'py_'+filename)