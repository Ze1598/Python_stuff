a = [[1,[2],3], ['a','b','c']] #depth 3
b = [[1,[2,3]], [['a',['b']],'c']] #depth 4

def recursive_flat(lst):
    #will be a flat version of the input lists
    flat_lst = []
    #loop through 'lst'
    for item in lst:
        #if 'item' is a list
        if type(item) is list:
            #then recursively extend() it to 'flat_lst' until item is a flat list
            flat_lst.extend(recursive_flat(item))
        #if 'item' is not a list then simply append it to 'flat_lst'
        else:
            flat_lst.append(item)
    return flat_lst
    
print(recursive_flat(a))
#[1, 2, 3, 'a', 'b', 'c']
print(recursive_flat(b))
#[1, 2, 3, 'a', 'b', 'c']

