#encoding:utf-8
import pytesseract
from PIL import Image
import os

#去除噪点
def remove_noise(img, pass_factor):  
    for column in range(img.size[0]):  
        for line in range(img.size[1]):  
            value = remove_noise_by_pixel(img, column, line, pass_factor)  
            img.putpixel((column, line), value)  
    return img 

#灰色化
def gray_filter(img):
	return img.convert('L')

#去除纵向噪点
def remove_verital_bad(img,badsize):
	w,h = img.size
	null_pts = []
	for y in xrange(h):
		black_number = 0
		for x in xrange(w):
			p = x,y
			p_value = img.getpixel(p)
			if p_value != 255: #黑色点
				black_number += 1
		if black_number <= badsize:  #白色点大于
			null_pts.append(y)
	l = list(set(list(xrange(h))) ^ set(null_pts))
	l.sort()
	new_h = len(l)
	print new_h
	newImg = Image.new('L', (w,new_h))
	for y in xrange(new_h):
		for x in xrange(w):
			p = x,y
			old_p = (x,l[y])
			old_value = img.getpixel(old_p)
			newImg.putpixel(p,old_value)
	return newImg

#二值化处理，这个阈值为140
def binary_image(img):
	w,h = img.size
	for y in range(h):  
		for x in range(w):
			p = x,y
			p_value = img.getpixel(p)
			if p_value < 140:
				img.putpixel(p,0)
			else:
				img.putpixel(p,255)

#删除四周噪点
def remove_border_bad(img,badsize):
	img = remove_horizental_bad(img, badsize)
	img = remove_verital_bad(img, 0)
	return expand_image(img, 5)

#缩放
def resize_by_width(image, w_divide_h):  
    """按照宽度进行所需比例缩放"""   
    (x, y) = image.size   
    x_s = w_divide_h  
    y_s = int(y*float(x_s)/x)
    out = image.resize((x_s, y_s), Image.ANTIALIAS)   
    return out

#扩充图片
def expand_image(img,padding):
	w,h = img.size
	size = new_w,new_h = w+2*padding,h+2*padding
	newImg = Image.new('L', size)
	for x in xrange(new_w):
		for y in xrange(new_h):
			if x <= padding or x>= (new_w-padding) or y <= padding or y>=(new_h-padding):
				newImg.putpixel((x,y), 255)
			else:
				new_p = x-padding,y-padding 
				newImg.putpixel((x,y), img.getpixel(new_p))
	return newImg

#创建子图片
def create_sub_image(img,widthRange):
	box = widthRange[0],0,widthRange[1],img.size[1]
	return img.crop(box)

#合成图片
def combine_image(imglist):
	t_w = sum([obj.size[0] for obj in imglist])
	t_h = imglist[0].size[1]
	newImg = Image.new('L', (t_w,t_h))
	t_x = 0
	for img in imglist:
		idx = imglist.index(img)
		sub_w,sub_h = img.size
		for sub_x in xrange(sub_w):
			for sub_y in xrange(sub_h):
				x = sub_x + t_x
				y = sub_y
				newImg.putpixel((x,y), img.getpixel((sub_x,sub_y)))
		t_x += sub_w
	newImg.save("combine.jpg")
	print pytesseract.image_to_string(newImg)


#删除噪点
def remove_noise_points_verital(img,badsize):
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

#分色处理
def div_color_exec(img):
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

#删除噪点
def remove_noise_points_horizental(img,badsize):
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

imageName = 'codeimg.jpg'
#加载图片
img = Image.open(imageName)
#缩放
#img = resize_by_width(img, 100)
#转为灰色
img = gray_filter(img)
#二值化
binary_image(img)
#删除噪点
remove_noise_points_verital(img, 3)
#删除噪点
remove_noise_points_horizental(img, 4)
print pytesseract.image_to_string(img)
