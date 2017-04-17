from sys import argv

script, txtfile = argv

f= open(txtfile)
print f.read()

print "lets print it again"
print f.seek(20)
print f.read()