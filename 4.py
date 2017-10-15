import os
def extension(dirname):
	'''returns number of files with extension .py'''
	count=0
	for dirpath,name,files in os.walk(dirname):
		Files=(File for File in files if File.split('.')[-1]=='py')
		for i in Files:
			count+=1
	return count

import sys
print extension(sys.argv[1])
