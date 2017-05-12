class Animal:
	def say():
		pass

class Dog(Animal):
	def say():
		print "wang wang"
		
class Cat(Animal):
	def say():
		print "Miao,Miao"

dog = Dog()
dog.say()
cat = Cat()
cat.say()

		