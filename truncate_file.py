from sys import argv
import os.path

script, filename = argv
#confirm file exists
if not os.path.isfile(filename):
	print 'file does not exist'
	exit(0)
	
	
print 'We\'re going to erase %r.' % filename
print 'Hit CTRL-C to abort.'
print 'Otherwise hit RETURN to erase'

raw_input('?')

print 'Opening the file....'
target = open(filename, 'w')
#confirm that file is empty
if os.path.getsize(filename) == 0:
	print 'File is already empty'
else:
	print 'Truncating the file...'
	target.truncate()
	