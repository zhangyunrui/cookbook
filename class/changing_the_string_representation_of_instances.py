class Pair:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return 'Pair({0.x!r}, {0.y!r})'.format(self)
	def __str__(self):
		return '({0.x!s}, {0.y!s})'.format(self)

class basePair:
	def __init__(self, x, y):
		self.x = x
		self.y = y

# !r 格式化代码指明输出使用 __repr__() 来代替默认的 __str__() 。


