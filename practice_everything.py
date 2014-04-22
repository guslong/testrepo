print "Let's practice everything"
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
this is 
a 
long 
poem 
on several
lines.
"""

print '----'
print poem
print '====='

five = 4 - 5 + 2 - 8
print 'this should be a number: ', five
print 'this is another way of printing it: %d' % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point = 10000

beans, jars, crates = secret_formula(start_point)

print 'With a starting point of %d' % start_point
print 'We have %d beans, %d jars, %d crates.' %(beans, jars, crates)
