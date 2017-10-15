def split(n,filename):
	'''return multiple files by splitting a file each having n number of lines'''
	f=open(filename,'r')
	m=f.readlines()
	a=len(m)
	k=1
	j=0
	for i in range(a/n):
		new=open(filename.split('.')[0]+'_'+str(i)+'.txt','w')
		while j < k*n:
			new.write(m[j])
			j+=1
		k+=1

import sys
split(int(sys.argv[1]),sys.argv[2])
