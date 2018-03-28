#This second file focuses statistical uses for NumPy using arrays

import numpy as np

print('Mean or Arithmetic Mean')
'''
The arithmetic mean is the sum of the elements along 
the axis divided by the number of elements.
'''
print('numpy.mean(arr, axis=None, dtype=None, out=None)')
'''
Returns the average of the array elements. The average is 
taken over the flattened array by default, otherwise over the 
specified axis.
'''
#numpy.mean(arr, axis=None, dtype=None)
'''
    axis: None or int or tuple of ints, optional. Axis or axes
along which the means are computed. The default is to compute
the mean of the flattened array. axis = 0 calculates the means
of each column; axis = 1 calculates the means of each row.
    dtype:data-type, optional. Type to use in computing
the mean.
'''
arr1 = np.array([[1, 2], [3, 4]])
print(f'arr1:\n{arr1}')
print('np.mean(arr1)', np.mean(arr1)) #2.5
print('arr1 columns\' mean =>', np.mean(arr1, axis=0)) #[ 2.  3.]
print('arr1 rows\' mean =>', np.mean(arr1, axis=1)) #[ 1.5  3.5]
print()


print('Mean of Logical Statements')
'''
The mean of logical statements is the the percentage of 
elements in the array relative to the number of elements
in the array that satisfy the given condition.
'''
arr2 = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958,
                1974, 1987, 2006, 2013, 1978, 1951, 1998,
                1996, 1952])
print('arr2:', arr2)
print('Percentage of arr2 values bigger or equal than 1980 =>', np.mean(arr2 >= 1980)) #0.4375
print()


print('Sorting')
print('numpy.sort(arr, axis=-1, kind=\'quicksort\')')
'''
Return a sorted copy of an array.
'''
#numpy.sort(arr, axis=-1, kind='quicksort')
'''
    axis: int or None, optional. Axis along which to sort. 
If None, the array is flattened before sorting. The default is -1,
which sorts along the last axis.
    kind : {‘quicksort’, ‘mergesort’, ‘heapsort’}, optional. 
Sorting algorithm. Default is ‘quicksort’.
'''
arr3 = np.array([[1,4],[3,1]])
print(f'arr3:\n{arr3}')
print(f'Sort along arr3\'s last axis =>\n{np.sort(arr3)}') #[[1 4] [1 3]]
print(f'Sort flattened arr3 =>\n{np.sort(arr3, axis=None)}') #[1 1 3 4]
print(f'Sort along arr3\'s first axis =>\n{np.sort(arr3, axis=0)}') #[[1 1] [3 4]]
print()


print('Median')
'''
Given an array V of length N, the median of V is the middle 
value of a sorted copy of V: V_sorted[(N-1)/2],
when N is odd; and the average of the two middle values of 
V_sorted when N is even.
'''
print('numpy.median(arr, axis=None, overwrite_input=False)')
'''
Compute the median along the specified axis. Returns the median 
of the array elements.
'''
#numpy.median(arr, axis=None, overwrite_input=False)
'''
    axis: {int, sequence of int, None}, optional. Axis or axes 
along which the medians are computed. The default is to compute
the median along a flattened version of the array.
    overwrite_input: bool, optional. If True, then allow the 
use of the input array arr for calculations. arr will be 
modified by the call to the function. This will save memory when 
you do not need to preserve the contents of the input array. 
Default is False. If overwrite_input is True and arr is not 
already an ndarray, an error will be raised.
'''
arr4 = np.array([[10, 7, 4], [3, 2, 1]])
print(f'arr4:\n{arr4}')
print('arr4\'s median =>', np.median(arr4))
print('arr4 columns\' median =>', np.median(arr4, axis=0))
print('arr4 rows\' median =>', np.median(arr4, axis=1))
arr5 = np.array([[10, 7, 4], [3, 2, 1]])
print(f'arr5:\n{arr5}')
print('Overwrite arr5 with the median of its rows =>', np.median(arr5, axis=1, overwrite_input=True))
print()


print('Percentiles')
'''
What if we wanted to find a point at which 40% 
of the samples are below, and 60% of the samples are above?
This type of point is called a percentile. The Nth 
percentile is defined as the point N% of samples 
lie below it. So the point where 40% of samples are 
below is called the 40th percentile. Percentiles are 
useful measurements because they can tell us where a 
particular value is situated within the greater dataset.
'''
'''
Given an array V of length N, the q-th percentile of V 
is the value q/100 of the way from the minimum to the maximum 
in a sorted copy of V.
'''
'''
The 25th percentile is called the first quartile
The 50th percentile is called the median
The 75th percentile is called the third quartile
'''
'''
The minimum, first quartile, median, third quartile, 
and maximum of a dataset are called a five-number summary. 
This set of numbers is a great thing to compute when we 
get a new dataset.
'''
'''
The difference between the first and third quartile is a 
value called the interquartile range. The interquartile 
range gives us an idea of how spread out our data is. 
The smaller the interquartile range value, the less 
variance in our dataset. The greater the value, the 
larger the variance. 
'''
print('numpy.percentile(arr, q, axis=None, overwrite_input=False, keepdims=False)')
'''
Returns the qth percentile(s) of the array elements.
'''
#numpy.percentile(arr, q, axis=None, overwrite_input=False, keepdims=False)
'''
    q: float in range of [0,100] (or sequence of floats). Percentile 
to compute, which must be between 0 and 100 inclusive.
    axis: {int, sequence of int, None}, optional. Axis or axes 
along which the medians are computed. The default is to compute
the median along a flattened version of the array.
    overwrite_input: bool, optional. If True, then allow the 
use of the input array arr for calculations. arr will be 
modified by the call to the function. This will save memory when 
you do not need to preserve the contents of the input array. 
Default is False. If overwrite_input is True and arr is not 
already an ndarray, an error will be raised.
    keepdims: bool, optional. If this is set to True, 
the axes which are reduced are left in the result as
dimensions with size one. With this option, the result will 
broadcast correctly against the original array.
'''
arr6 = np.array([[10, 7, 4], [3, 2, 1]])
print(f'arr6:\n{arr6}')
print('arr6\'s 50th percentile =>', np.percentile(arr6, 50))
print('arr6 columns\' 50th percentile =>', np.percentile(arr6, 50, axis=0))
print('arr6 rows\' 50th percentile =>', np.percentile(arr6, 50, axis=1))
print(f'arr6 rows\'s 50th percentile with dimensions kept =>\n{np.percentile(arr6, 50, axis=1, keepdims=True)}')
print()


print('Standard Deviation')
'''
Similar to the interquartile range, the standard deviation
tells us the spread of the data. The larger the standard 
deviation, the more spread out our data is from the center. 
The smaller the standard deviation, the more the data is 
clustered around the mean. 
'''
'''
The standard deviation is the square root of the average 
of the squared deviations from the mean, i.e., 
std = sqrt(mean(abs(x - x.mean())**2)).
'''
'''
Given a normal distribution with a mean of 50
and a standard deviation of 10, when we say "within one 
standard deviation of the mean", mathematically it means:
about 68% of our dataset is expected to be between 40 and 60.
No matter what mean and standard deviation we choose, 
68% of our samples will fall between +/- 1 standard deviation 
of the mean.
Actually:
    68% of the samples will fall between +/- 1 standard deviation of the mean
    95% of the samples will fall between +/- 2 standard deviations of the mean
    99.7% of the samples will fall between +/- 3 standard deviations of the mean
'''
print('numpy.std(a, axis=None, dtype=None, keepdims=<class numpy._globals._NoValue>)')
'''
Returns the standard deviation, a measure of the spread of 
a distribution, of the array elements. 
'''
#numpy.std(a, axis=None, dtype=None, keepdims=<class numpy._globals._NoValue>)
'''
    axis: None or int or tuple of ints, optional. Axis or axes 
along which the standard deviation is computed. The default is 
to compute the standard deviation of the flattened array.
    dtype:dtype, optional. Type to use in computing the standard 
deviation.
    keepdims: bool, optional. If this is set to True, the axes 
which are reduced are left in the result as dimensions with 
size one. With this option, the result will broadcast correctly 
against the original array.
'''
arr7 = np.array([[1, 2], [3, 4]])
print(f'arr7:\n{arr7}')
print('arr7\'s standard deviation =>', np.std(arr7))
print('arr7 columns\' standard deviation =>', np.std(arr7, axis=0))
print('arr7 rows\' standard deviation =>', np.std(arr7, axis=1))
print()