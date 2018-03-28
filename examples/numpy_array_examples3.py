#This third file focuses on basic statistics using numpy

import numpy as np
from matplotlib import pyplot as plt

'''
Histograms and their datasets can be classified based on the
shape of the graphed values. One way to classify a dataset
is by counting the number of distinct peaks present in 
the graph. Peaks represent concentrations of data.
    A unimodal dataset has only one distinct peak.
    A bimodal dataset has two distinct peaks. This often 
happens when the data contains two different populations.
    A multimodal dataset has more than two peaks. 
'''
'''
We can further classify unimodal distributions by describing 
where most of the numbers are relative to the peak.
The type of distribution affects the position of the mean 
and median. In heavily skewed distributions, the mean 
becomes a less useful measurement.
    A symmetric dataset has equal amounts of data on both 
sides of the peak. Both sides should look about the same.
    A skew-right dataset has a long tail on the right of the 
peak, but most of the data is on the left.
    A skew-left dataset has a long tail on the left of the 
peak, but most of the data is on the right.

'''
print('Histograms')
'''
Histograms represent visually the answers to questions such as:
    Do some values occur more often than others?
    What is the range of the dataset (i.e., the min and the max values)?
    Are there a lot of outliers?
'''
dataset1 = np.array([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5])
'''
    Value 	Number of Samples
    1 	            3
    2 	            5
    3 	            2
    4 	            4
    5 	            1
'''
'''
Suppose we had a larger dataset with values ranging from 0 
to 50. We might not want to know exactly how many 0's, 1's, 2's, 
etc. we have. Instead, we might want to know how many values 
fall between 0 and 5, 6 and 10, 11 and 15, etc. These groupings
are called bins. All bins in a histogram are always the same size. 
The width of each bin is the distance between the minimum and maximum 
values of each bin. In our example, the width of each bin would be 5.
'''
print('matplotlib.pyplot.hist(x, bins=None, range=None)')
'''
Plot a histogram.
'''
#matplotlib.pyplot.hist(x, bins=None, range=None)
'''
    x:(n,) array or sequence of (n,) arrays. Input values, this takes 
either a single array or a sequency of arrays which are not required 
to be of the same length.
    bins: integer or array_like or ‘auto’, optional. If an integer 
is given, bins + 1 bin edges are returned, consistently with 
numpy.histogram().
    range:tuple or None, optional. The lower and upper range of the 
bins. Lower and upper outliers are ignored. If not provided, range is 
(x.min(), x.max()). Range has no effect if bins is a sequence.
If bins is a sequence or range is specified, autoscaling is based on 
the specified bin range instead of the range of x. Default is None.
'''
#Plot an histogram for dataset1 with 4 bins of width 1:\
#[1,2[, [2, 3[, [3,4[, [4,5[
plt.hist(dataset1, bins=4, width=1)
#Name the graph and the axis
plt.suptitle('Histograms')
plt.xlabel('Values')
plt.ylabel('Frequency')
#Display the histogram in a new window
plt.show()
print()


print('Normal Distribution')
'''
The most common distribution in statistics is known as 
the normal distribution, which is a symmetric, unimodal distribution.
Lots of things follow a normal distribution: the heights of a large 
group of people; blood pressure measurements for a group of healthy
people; errors in measurements.
Normal distributions are defined by their mean and standard deviation. 
'''
'''
The mean sets the "middle" of the distribution, and the standard 
deviation sets the "width" of the distribution. A larger standard 
deviation leads to a wider distribution. A smaller standard deviation 
leads to a skinnier distribution.
Each set of data has the same "shape", but with slight differences 
depending on their mean and standard deviation. 
'''
print('numpy.random.normal(loc=0.0, scale=1.0, size=None)')
'''
Draw random samples from a normal (Gaussian) distribution.
Returns: ndarray or scalar. The drawn samples from the 
parameterized normal distribution.
'''
#numpy.random.normal(loc=0.0, scale=1.0, size=None)
'''
    loc: float or array_like of floats. The mean (“centre”) 
of the distribution.
    scale: float or array_like of floats. standard deviation 
(spread or “width”) of the distribution.
    size: int or tuple of ints, optional. Output shape. 
If the given shape is, e.g., (m, n, k), then m * n * k samples 
are drawn. If size is None (default), a single value is returned 
if loc and scale are both scalars. Otherwise, 
np.broadcast(loc, scale).size samples are drawn.
'''
mu, sigma = 30, 7 #Mean and Standard Deviation
norm_dist = np.random.normal(mu, sigma, 50)
print('Normal distribution with: mean=30, std_dev=7, size=50 =>',norm_dist)
#Plot an histogram for this normal distribution
plt.hist(norm_dist, bins=10, range=(9, 51))
#Name the graph and the axis
plt.suptitle('Normal Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')
#Show the histogram in a new window
plt.show()
print()


print('Binomial Distribution')
'''
The binomial distribution is important because it allows us
to know how likely a certain outcome is, even when it's not 
the expected one.
'''
print('numpy.random.binomial(n, p, size=None)')
'''
Draw samples from a binomial distribution. Samples are drawn 
from a binomial distribution with specified parameters, 
n trials and p probability of success where n an 
integer >= 0 and p is in the interval [0,1]. n may be input 
as a float, but it is truncated to an integer in use.
'''
'''
Returns an ndarray or scalar. Drawn samples from the parameterized 
binomial distribution, where each sample is equal to the number 
of successes over the n trials.
'''
#numpy.random.binomial(n, p, size=None)
'''
    n: int or array_like of ints. Parameter of the 
distribution, >= 0. Floats are also accepted, but they 
will be truncated to integers.
    p: float or array_like of floats. Parameter of the 
distribution, >= 0 and <=1.
    size: int or tuple of ints, optional. Output shape. 
If the given shape is, e.g., (m, n, k), then m * n * k 
samples are drawn. If size is None (default), a single 
value is returned if n and p are both scalars. Otherwise, 
np.broadcast(n, p).size samples are drawn.
'''
n, p = 10, 0.5  #Number of trials, Probability of success for each trial
bin_dist = np.random.binomial(n, p, 50)
print('Binomial distribution for 10 trials with 0.5 chance of success, repeated 50 times =>', bin_dist)
#Plot an histogram for the binomial distribution
plt.hist(bin_dist, bins=10, range=(0, 10))
#Name the graph and the axis
plt.suptitle('Binomial Distribution')
plt.xlabel('Number of successes per trial')
plt.ylabel('Frequency')
#Show the histogram in a new window
plt.show()
print()
