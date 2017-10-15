class f_operations:
	'''class implements some few file operations which outputs the lines in files with more than 40 characters'''
	
	def __init__(self,filenames):
		self.filenames=filenames
	
	def readfiles(self):
		for f in self.filenames:
			for line in open(f):
				yield line
	
	def length(self,lines):
		self.lines=lines
		return (line for line in self.lines if len(line)>40)
	
	def printlines(self,lines):
		self.lines=lines
		for line in self.lines:
			print(line)


import sys
a=f_operations(sys.argv[1:])
lines=a.readfiles()
lines=a.length(lines)
a.printlines(lines)
