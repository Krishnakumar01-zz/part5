def izip(a,b):
	'''implementation of itertools.izip function'''
	c=[]
	for i in range(len(a)):
		c.append((a[i],b[i]))
	return iter(c)

for x,y in izip(['a','b','c'],[1,2,3]):
	print(x,y)	
