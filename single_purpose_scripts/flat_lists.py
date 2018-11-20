'''
Transform a n-dimensions list into a 1-dimension list
'''

def flattenArrayN(arr):
    # The 1-dimension list to be returned
    arr_ = []
    
    # Loop through the items in the input list
    for i in arr:
    	
    	# If the item is a list, add (extend) the contents\
    	# of that sublist to the 1D list recursively (that\
    	# is, we then loop through the contents of this sublist\
    	# and repeat the process until we find just an object\
    	# that is not a list)
        if isinstance(i, list):
        	arr_.extend(flattenArrayN(i))
        
        # If i is not a list, we append it to the 1D list
        else:
            arr_.append(i)

    return arr_