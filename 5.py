import os
import re
def lines(dirname):
	'''returns total number of lines of code in the files with extension .py'''
        count=0
        for dirpath,name,files in os.walk(dirname):
        	Files=(File for File in files if File.split('.')[-1]=='py')
		for i in Files:
			a=os.path.join(dirpath,i)
			for line in open(a):
				count+=1
 	return count
import sys
print(lines(sys.argv[1]))

