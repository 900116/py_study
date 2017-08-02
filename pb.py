
#encoding=utf-8
import sys, time
 
class ProgressBar:
  def __init__(self, count = 0, total = 0, width = 100):
    self.count = count
    self.total = total
    self.width = width
  
  def update(self,addCount = 1):
    self.count += addCount
    self.draw()

  def draw(self):
    sys.stdout.write(' ' * (self.width + 9) + '\r')
    sys.stdout.flush()
    progress = self.width * self.count / self.total
    f_c = float(self.count)
    f_t = float(self.total)
    p_i = int(f_c/f_t * 100) 
    sys.stdout.write('{0:3}%: '.format(p_i))
    sys.stdout.write('▍' * progress + '▏' * (self.width - progress) + '\r')
    if progress == self.width:
      sys.stdout.write('\n')
    sys.stdout.flush()
 
bar = ProgressBar(total = 100)
for i in range(100):
  bar.update(1)
  time.sleep(0.3)