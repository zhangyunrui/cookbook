class Date:
	__slots__ = ['year', 'month', 'day']
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

# 当你定义 __slots__ 后，Python就会为实例使用一种更加紧凑的内部表示。 
# 实例通过一个很小的固定大小的数组来构建，而不是为每个实例定义一个字典，这跟元组或列表很类似。
# 定义了slots后的类不再支持一些普通类特性了，比如多继承。
# 关于 __slots__ 的一个常见误区是它可以作为一个封装工具来防止用户给实例增加新的属性。


