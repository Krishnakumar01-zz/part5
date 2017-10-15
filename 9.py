import itertools
def my_enumerate(it):
	'''implements enumerate function iteratively'''
	it1=list(it)
	a=[]
	for i in range(len(it1)):
		a.append(i)
	return itertools.izip(a,it1)	


it=iter(['a','b','c'])
for i,c in my_enumerate(it):
	print(i,c)
