import os
import re
def lines(dirname):
	'''returns total number of lines of code in the files with extension .py by avoiding empty lines and comments '''
        count=0
        for dirpath,name,files in os.walk(dirname):
        	Files=(File for File in files if File.split('.')[-1]=='py')
                for i in Files:
                	a=os.path.join(dirpath,i)
                        f=open(a,'r')
                        for line in f.readlines():
                        	if len(line)!=1 and not re.match(r'^#',line):                                    	
					count+=1
        	f.close()
	return count
import sys
print(lines(sys.argv[1]))

