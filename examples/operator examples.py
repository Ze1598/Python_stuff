def test(x, y, z):
	print(x, y, z)
 
testDict = {'x': 1, 'y': 2, 'z': 3} 
testList = [10, 20, 30]
 
test(*testDict)
test(**testDict)
test(*testList)