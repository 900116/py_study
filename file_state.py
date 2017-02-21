#encoding=utf-8
import os
import stat
s = os.stat("net_study.py")
file_mode = s.st_mode
print s
print "文件模式:"+str(file_mode)
print "是否是文件夹:" + str(stat.S_ISDIR(file_mode))
print "是否是文件:" + str(stat.S_ISREG(file_mode))
#R同组的人 OTH其他组的人  USR	 拥有者  
can_read = file_mode & stat.S_IRUSR > 0
can_write = file_mode & stat.S_IWUSR > 0  
can_execute = file_mode & stat.S_IXUSR > 0
print "文件是否可读: " + str(can_read)
print "文件是否可写: " + str(can_write)
print "文件是否可运行: " + str(can_execute)
print "文件访问时间：" + str(s.st_atime)
print "文件修改时间：" + str(s.st_mtime)
print "文件状态更新时间：" + str(s.st_ctime)
print "文件大小：" + str(s.st_size)

#文件缓冲 f = open('demo2.txt', 'w', buffering=2048,encoding='utf-8')   全缓冲为大于1的证书
#无缓冲为0 行缓冲为1

#文件映射内存
import mmap
f = open('test.txt','w')
f.write("I Believe I Can Fly")
f.close()

f = open('test.txt','r+b')
#获取文件描述
f_fileno = f.fileno()
m = mmap.mmap(f_fileno, 0,access=mmap.ACCESS_WRITE)
type(m)
print m[0]
print m[10:20]
m[0] = 'X'

#临时文件
from tempfile import TemporaryFile,NamedTemporaryFile
f = TemporaryFile()
f.write('abcdef'*100000)
f.seek(0)
print f.read(100)
ntf = NamedTemporaryFile(delete=True)
print ntf.name