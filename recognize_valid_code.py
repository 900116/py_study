#encoding:utf-8
import pytesseract
from PIL import Image
import os

#缩放
def resize_by_width(image, except_width):
	"""
	缩放图片，根据期望宽度，等比例缩放	
	:param image:图片 
	:param except_width:期望宽度
	:returns: 处理后的图片
	"""
	x,y = image.size
	except_height = int(y*float(except_width)/x)
	out = image.resize((except_width, except_height), Image.ANTIALIAS)
	return out

#扩充图片
def expand_image(img,padding):
	"""
	给图片添加空白部分
	
	:param image:图片 
	:param padding:四周空白像素
	:returns: 处理后的图片
	"""
	w,h = img.size
	size = new_w,new_h = w+2*padding,h+2*padding
	out = Image.new('L', size)
	for x in xrange(new_w):
		for y in xrange(new_h):
			if x <= padding or x>= (new_w-padding) or y <= padding or y>=(new_h-padding):
				out.putpixel((x,y), 255)
			else:
				new_p = x-padding,y-padding 
				out.putpixel((x,y), img.getpixel(new_p))
	return out

#裁剪图片
def create_sub_image(img,widthRange):
	"""
	裁剪图片
	
	:param image:图片 
	:param widthRange: min_x,max_x的元组,表示x的范围
	:returns: 处理后的图片
	"""
	box = widthRange[0],0,widthRange[1],img.size[1]
	return img.crop(box)

#合成图片
def combine_image(imglist):
	"""
	合成图片，将多张图片合成一张，左右拼接
	
	:param imglist:图片列表
	:returns: 合成的图片
	"""
	t_w = sum([obj.size[0] for obj in imglist])
	t_h = imglist[0].size[1]
	out = Image.new('L', (t_w,t_h))
	t_x = 0
	for img in imglist:
		idx = imglist.index(img)
		sub_w,sub_h = img.size
		for sub_x in xrange(sub_w):
			for sub_y in xrange(sub_h):
				x = sub_x + t_x
				y = sub_y
				out.putpixel((x,y), img.getpixel((sub_x,sub_y)))
		t_x += sub_w
	return out

#灰色化
def gray_filter(img):
	"""
	灰色处理
	
	:param image:图片 
	:returns: 处理后的图片
	"""
	return img.convert('L')

#二值化处理，这个阈值为140
def binary_image(img):
	"""
	二值化处理，这个阈值为140
	:param image:图片 
	"""
	w,h = img.size
	for y in range(h):  
		for x in range(w):
			p = x,y
			p_value = img.getpixel(p)
			if p_value < 140: #小于阈值则绘制成黑色的点(有效区域)，否则为白色
				img.putpixel(p,0)
			else:
				img.putpixel(p,255)

#分色处理(另一种降噪方法)
def div_color_exec(img):
	"""
	分色处理 将图片按照不同的颜色处理成多张图片
	然后将这些图片二值处理并消除噪点，最后将这些图片的黑色区域(有效区域)合并
	:param image:图片 
	"""
	imglist = []
	w,h = img.size
	l = []
	for x in xrange(w):
		for y in xrange(h):
			l.append(img.getpixel((x,y)))

	dic = dict()
	l2 = []
	for value in l:
		if value not in l2:
			dic[value] = 1
			l2.append(value)
		else:
			count = dic[value]
			count+=1
			dic[value] = count

	l = []
	for value in dic.keys():
		count = dic[value]
		if count > 100 and count < w*h/2:
			l.append(value)
	print l
	for i in l:
		subimg = img.copy()
		youxiao_count = 0
		for x in xrange(w):
			for y in xrange(h):
				p_value = img.getpixel((x,y))
				if p_value == i:
					youxiao_count+=1
					subimg.putpixel((x,y),0)
				else:
					subimg.putpixel((x,y),255)
		remove_noise_points_verital(subimg, 2)
		remove_noise_points_horizental(subimg, 2)
		subimg.save("%d.jpg" % i)
		imglist.append(subimg)

	for x in xrange(w):
		for y in xrange(h):
			temp = 255
			for subimg in imglist:
				p_value = subimg.getpixel((x,y))
				# print value
				if p_value == 0:
					temp = 0
					break
			img.putpixel((x,y),temp)

#删除垂直噪点
def remove_noise_points_verital(img,badsize):
	"""
	删除垂直噪点
	连续区域高度小于等于噪点尺寸，则认为是噪点，并清除(绘制成白色)
	:param image:图片
	:param badsize:噪点尺寸 
	"""
	w,h = img.size
	for x in xrange(w):
		black_numbers = []
		last_is_black = True #上一个是否黑点
		for y in xrange(h):
			p = x,y
		 	p_value = img.getpixel(p)
		 	if p_value != 255: #当前为黑点
		 		black_numbers.append((x,y)) 
		 	else:#白点，黑点数量小于噪点数量
		 		if len(black_numbers) < badsize:
		 			for p in black_numbers:
		 				img.putpixel(p,255) 
		 		black_numbers = []	

#删除水平噪点
def remove_noise_points_horizental(img,badsize):
	"""
	删除谁捧噪点
	连续区域宽度小于等于噪点尺寸，则认为是噪点，并清除(绘制成白色)
	:param image:图片 
	:param badsize:噪点尺寸
	"""
	w,h = img.size
	for y in xrange(h):
		black_numbers = []
		last_is_black = True
		for x in xrange(w):
			p = x,y
		 	p_value = img.getpixel(p)
		 	if p_value != 255: #黑点
		 		black_numbers.append((x,y)) 
		 	else:#白点，黑点数量小于噪点数量
		 		if len(black_numbers) < badsize:
		 			for p in black_numbers:
		 				img.putpixel(p,255) 
		 		black_numbers = []	

#拆分图片
def divid_image(img,badsize):
	"""
	拆分图片，将图片按照水平连续区域拆成多张图片
	:param image:图片 
	:param badsize:噪点尺寸
	"""
	w,h = img.size
	min_x = max_x = 0
	i = 0
	imglist = []
	last_black_is_zero = True
	for x in xrange(w):
		black_number = 0
		for y in xrange(h):
			p = x,y
		 	p_value = img.getpixel(p)
		 	if p_value != 255: #黑色点
				black_number += 1
		#上一个是0
		if last_black_is_zero:
			#当前不是0
			if black_number > badsize:
				min_x = x
				last_black_is_zero = False
		#上一个不是0
		else:
			#当前是0
			if black_number <= badsize:
				max_x = x-1
				print min_x,max_x
				subimg = create_sub_image(img,(min_x,max_x))
				subimg = remove_verital_bad(img, 0)
				subimg.save("test_%d.jpg" % i)
				imglist.append(subimg)
				i+=1
				last_black_is_zero = True
	return imglist

#'chi_sim'
def recongnize_image(imageName,except_width = -1,h_badsize = 0,v_badsize = 0,language="eng"):
	"""
	图片识别方法
	:param imageName:图片名称
	:param except_width:期望宽度，默认为-1，表示不进行缩放
	:param h_badsize:水平噪点大小
	:param v_badsize:竖直噪点大小
	:param language:语言设定，默认为英文，如果为简体中文设置'chi_sim' 
	:returns:是别的文本
	"""
	#加载图片
	img = Image.open(imageName)
	#缩放
	if except_width != -1:
		img = resize_by_width(img, except_width)
	#转为灰色
	img = gray_filter(img)
	#二值化
	binary_image(img)
	#删除噪点
	if h_badsize != 0:
		remove_noise_points_verital(img, v_badsize)
	#删除噪点
	if v_badsize != 0:
		remove_noise_points_horizental(img, h_badsize)
	result = pytesseract.image_to_string(img,language)
	result = result.replace(' ','')
	return result

def test_1():
	print recongnize_image("test.jpg",h_badsize=4,v_badsize=3)

def test_2():
	print recongnize_image("test2.jpg",language="chi_sim")

def test_3():
	print recongnize_image("test3.jpg",language="chi_sim") 

def test_4():
	print recongnize_image("test4.jpg",language="chi_sim") 

if __name__ == "__main__":
	test_1()
	test_2()
	test_3()
	test_4()
