f = open('archivo1.txt','r+b')
print f

print f.read()

print f.readline()

for line in f:	
	print line

f.write("Agregango Texto al archivo\n")

print f.read()

f.close()
