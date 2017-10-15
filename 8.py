def peep(it):
	'''returns the first element and an equivalent iterator for a given iterator'''
	it1=list(it)
	a=it1[0]
	i=it1[:]
	return a,iter(i)



it=iter(range(5))
x,it1=peep(it)
print(x,list(it1))	
