def read_lines_for_text_file(file_name):
	file_obj = open(file_name,'r')
	try:
		ls = file_obj.readlines()
	except Exception,e:
		ls = None
	finally:
		file_obj.close()
	return ls