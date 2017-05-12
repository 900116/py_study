def read_lines_for_text_file(file_name):
	file_obj = open(file_name,'r')
	try:
		ls = file_obj.readlines()
	except Exception,e:
		ls = None
	finally:
		file_obj.close()
	return ls

def read_content_for_text_file(file_name):
	file_obj = open(file_name,'r')
	try:
		content = file_obj.read()
	except Exception,e:
		content = None
	finally:
		file_obj.close()
	return content