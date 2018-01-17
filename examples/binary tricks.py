a = '7'
b = '1'
print('int(a) + int(b):',int(a) + int(b)) #8
print()

c = '7'
d = 1
print('(bin(int(c) + d):',(bin(int(c) + d))) #0b1000
print()

e = format(0b111,'b')
print('e:',e) #111
print('type(e):',type(e)) #str
print()

f = 7
print('type(str(bin(f))+\'1\':)',type(str(bin(f))+'1')) #str
print('type(f):', type(f)) #int
print('f:',f) #7
print()

g = '0b100'
print('g:',int(g,2)) #4