#This first file focuses on arrays: creation, indexing and element-wise operations

import numpy as np

print('Array vs List')
#A normal Python list
list1 = [1,2,3]
#Create a numpy array using the 'list1' list
arr1 = np.array(list1)
print('list1:', list1, 'arr1:', arr1) #[1, 2, 3] [1 2 3]
print('list1:', type(list1), 'arr1:', type(arr1)) #<class 'list'> <class 'numpy.ndarray'>
print(f'[(1,2), (3,4)] =>\n{np.array([(1,2), (3,4)])}')
#[[1 2]
# [3 4]]
print()

print('"np.array(object, dtype=<type \'float\'>"')
'''
Create an array.
'''
#np.array(object, dtype=<type 'float'>)
'''
    dtype: The desired data-type for the array. If not given,
then the type will be determined as the minimum type required to
hold the objects in the sequence. This argument can only be used to 
‘upcast’ the array. For downcasting, use the .astype(t) method.
'''
print('[1, 2, 3.0] =>', np.array([1, 2, 3.0])) #[ 1.  2.  3.]
print('[1, 2, 3.0], int =>', np.array([1, 2, 3.0], int)) #[1 2 3]
print('[1, 2, 3.0], str =>', np.array([1, 2, 3.0], str)) #['1' '2' '3.0']
print('[1, 2, 3.0], complex =>', np.array([1, 2, 3.0], complex)) #[ 1.+0.j  2.+0.j  3.+0.j]
print()

print('More than 1 dimension arrays')
#More than 1 dimension
print(f'[[1,2], [3,4]] =>\n{np.array([[1,2], [3,4]])}')
#[[1 2]
# [3 4]]
print()

#np.array(object, ndmin=0)
print('"np.array(object, ndmin=0)"')
'''
    ndmin: Specifies the minimum number of dimensions that
the resulting array should have. Ones will be pre-pended
to the shape as needed to meet this requirement.
'''
print('[1, 2, 3], ndmin=2 =>', np.array([1, 2, 3], ndmin=2)) #[[1 2 3]]
print('[1, 2, 3], ndmin=3 =>', np.array([1, 2, 3], ndmin=3)) #[[[1 2 3]]]
print('[[1, 2, 3]], ndmin=2 =>', np.array([[1, 2, 3]], ndmin=2)) #[[1 2 3]]
print()

print('Create an array using values from a .csv file')
print('"np.genfromtxt(file_name, dtype=<type \'float\'>, delimiter=None)"')
'''
Load data from a text file, with missing values handled as specified.
Each line past the first skip_header lines is split at the delimiter
character, and characters following the comments character are discarded.
'''
#np.genfromtxt(file_name, dtype=<type 'float'>, delimiter=None)
#In this sample the values are separated by a comma
csv_array = np.genfromtxt('numpy_array_examples_sample.csv', delimiter=',')
print('numpy_array_examples_sample.csv, delimiter="," =>', csv_array) #[ 34.   9.  12.  11.   7.]
csv_array2 = np.genfromtxt('numpy_array_examples_sample.csv', dtype=int, delimiter=',')
print('numpy_array_examples_sample.csv, dtype=int, delimiter="," =>', csv_array2) #[34  9 12 11  7]
print()

print('Element-wise operations')
'''
An element-wise operation allows you to quickly perform
an operation, such as addition, on each element in an array.
'''
#Example comparison of element-wise operations in lists vs arrays
list2 = [1,2,3]
arr2 = np.array(list2)
print('Original list2:', list2, 'Original arr2:', arr2)
print('list2+=3 =>', [i+3 for i in list2], 'arr2+=3 =>', arr2+3) #[4 5 6] [4 5 6]
print('arr2-=3', arr2-3) #[-2 -1  0]
print('sqrt(arr2) =>', np.sqrt(arr2)) #[ 1.          1.41421356  1.73205081]
print()


print('Element-wise operations logical operations')
arr3 = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7])
print('arr3 values bigger than 5 =>', arr3[arr3 > 5]) #[10  9  8  9  7]
print('arr3 values bigger than 5 and smaller than 11 =>', arr3[(arr3 > 5) & (arr3 < 11)]) #[10  9  8  9  7]
print('arr 3 values bigger than 5 or smaller than 3 =>', arr3[(arr3 > 5) | (arr3 < 3)]) #[10  2  2  9  8  9  7]
print()


print('Operations between arrays (must have the same length)')
print('np.array([1,2]) + np.array([3,4]) =>', np.array([1,2]) + np.array([3,4])) #[4 6]
print('Average of (np.array([1,2]) + np.array([3,4])) =>', (np.array([1,2]) + np.array([3,4]))/2) #[ 2.  3.]
print()


print('Extracting values from a 2D array using indexes')
#Arrays are also zero-indexed
#The 2D array: contains 3 rows and 5 columns (contains 3 lists with 5 elements each)
arr4 = np.array([[92, 94, 88, 91, 87], [79, 100, 86, 93, 91], [87, 85, 72, 90, 92]])
print(f'arr4:\n{arr4}')
#[[ 92  94  88  91  87]
# [ 79 100  86  93  91]
# [ 87  85  72  90  92]]
row_3_column1 = arr4[2, 0]
print('Row 3; Column 1: arr4[2, 0] =>', row_3_column1) #87
column_5 = arr4[:,4]
print('Column 5: arr4[:,4] =>', arr4[:,4]) #[87 91 92]
print()

print('Finding values in an array')
print('numpy.where(condition[, x, y])')
'''
Return elements, either from x or y, depending on condition.
If only condition is given, return condition.nonzero().
'''
#numpy.where(condition[, x, y])
'''
    condition: array_like, bool. When True, yield x, otherwise yield y.
    x,y: array_like, optional. Values from which to choose. x, y and 
condition need to be broadcastable to some shape.
'''
arr5 = np.array(list(range(1,11)))
print(f'arr5:\n{arr5}')
#arr5[arr5%2==0] would return the values corresponding to the indices\
#returned by np.where(arr5%2==0)
print('arr5 even numbers\' indices =>', np.where(arr5%2==0))
#(array([1, 3, 5, 7, 9], dtype=int32),)