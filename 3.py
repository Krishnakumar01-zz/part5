import os
def findfiles(dirname):
	'''returns the path to each file in the given directory'''
	for dirpath,dirs,files in os.walk(dirname):
		path=os.path.join('home/krishnakumar/python/part5',dirpath)
		for f in files:
			yield os.path.join(path,f)

import sys
for i in findfiles(sys.argv[1]):
	print(i)
