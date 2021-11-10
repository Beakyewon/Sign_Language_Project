import os
import sys

def reset_file():
		file = open('../../../../OneDrive/Desktop/pyflask/static/output.txt', 'r')  # open file handle for read
# use r'', you don't need to replace '\' with '/'
		result = open('../../../../OneDrive/Desktop/pyflask/static/output.txt', 'w')  # open file handle for write
		
		for line in file:
			line = line.strip('\r\n')  # it's always a good behave to strip what you read from files
			line = "Hi"  # if match, replace line
			result.write(line + '\n')  # write every line
		
		file.close()  # don't forget to close file handle
		result.close()

reset_txt()
