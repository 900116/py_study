#encoding:utf-8
import pytesseract
from PIL import Image
from PIL import ImageGrab
import os

def combine_pics(img_file_list,horizental=False,bgcolor=(255,255,255)):
	img_count = len(img_file_list)
	img_list = [Image.open(i) for i in img_file_list]
	w_list = [i.size[0] for i in img_list]
	h_list = [i.size[1] for i in img_list]
	w = max(w_list)
	h = max(h_list)
	t_w,t_h = w,h
	if horizental:
		t_w = sum(w_list)
	else:
		t_h = sum(h_list)
	out = Image.new('RGB', (t_w,t_h))

	#填充背景色
	for x in range(t_w):
		for y in range(t_h):
			out.putpixel((x,y), bgcolor)

	for img in img_list:
		idx = img_list.index(img)
		begin_y = sum(h_list[:idx])
		begin_x = sum(w_list[:idx])
		sub_w,sub_h = img.size
		for sub_x in xrange(sub_w):
			for sub_y in xrange(sub_h):
				x = sub_x + (horizental and begin_x or 0)
				y = sub_y + (horizental and 0 or begin_y)
				pixel = img.getpixel((sub_x,sub_y))
				out.putpixel((x,y), pixel)
	return out

img_file_list = [str(x)+".jpg" for x in range(1,5)]
combine_pics(img_file_list).save("final.jpg")