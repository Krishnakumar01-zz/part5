class reverse_iter:
	'''Class implements yhe reverse iteration of a list'''
	def __init__(self,List):
		self.List=List
		self.n=len(List)
		self.i=0
	def __iter__(self):
		return self
	def  next(self):
		if self.n >self.i:
			self.n-=1
			return self.List[self.n]
		else:
			raise StopIteration
it=reverse_iter([1,2,3,4])
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
