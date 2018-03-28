from matplotlib import pyplot as plt
import numpy as np
from random import randint

print('Histogram')
# matplotlib.pyplot.hist(x, bins=None, range=None, histtype='bar', orientation='vertical', ec='color')
'''
Plot a histogram.
Compute and draw the histogram of x. The return value is 
a tuple (n, bins, patches) or ([n0, n1, …], bins, 
[patches0, patches1,…]) if the input contains multiple data.
Multiple data can be provided via x as a list of datasets 
of potentially different length ([x0, x1, …]), or as a 2D 
ndarray in which each column is a dataset. Note that the 
ndarray form is transposed relative to the list form.
'''
'''
A histogram tells us how many values in a dataset fall 
between different sets of numbers (i.e., how many 
numbers fall between 0 and 10? Between 10 and 20? Between 
20 and 30?). Each of these questions represents a bin, 
for instance, our first bin might be between 0 and 10.
All bins in a histogram are always the same size. The 
width of each bin is the distance between the minimum 
and maximum values of each bin. In our example, the 
width of each bin would be 10. Each bin is represented 
by a different rectangle whose height is the number of 
elements from the dataset that fall within that bin.
'''
print('matplotlib.pyplot.hist(x, bins=None, range=None, histtype=\'bar\', orientation=\'vertical\', ec=\'color\')')
'''
    x: (n,) array or sequence of (n,) arrays. Input values, 
this takes either a single array or a sequence of arrays 
which are not required to be of the same length.
    bins: integer or array_like or ‘auto’, optional. If an 
integer is given, bins + 1 bin edges are returned, 
consistently with numpy.histogram() for numpy version >= 1.3.
Unequally spaced bins are supported if bins is a sequence.
    range: tuple or None, optional; Defaults to None. 
The lower and upper range of the bins. Lower and upper 
outliers are ignored. If not provided, range is 
(x.min(), x.max()). Range has no effect if bins is a 
sequence. If bins is a sequence or range is specified, 
autoscaling is based on the specified bin range 
instead of the range of x.
    histtype : {‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}, optional.
The type of histogram to draw.
        ‘bar’ is a traditional bar-type histogram. If multiple data 
are given the bars are aranged side by side.
        ‘barstacked’ is a bar-type histogram where multiple data are 
stacked on top of each other.
        ‘step’ generates a lineplot that is by default unfilled.
        ‘stepfilled’ generates a lineplot that is by default filled.
    orientation : {‘horizontal’, ‘vertical’}, optional;
defaults to 'vertical'. If 'horizontal', the axis' values are
swapped, i.e., the bins values are represented in the y-axis
and the frequencies on the x-axis.
    ec: string with a color's name, optional. Outlines the
histogram's bins using this color.
'''

print()
print('Basic Histogram')
dataset1 = np.array([randint(10,100) for i in range(50)])
print(f'dataset1:\n{dataset1}\nNumber of samples: {len(dataset1)}')
print('plt.hist(dataset1)')
plt.hist(dataset1)
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequencies')
plt.show()

print('Basic Histogram with custom number of bins')
dataset2 = np.array([randint(10,100) for i in range(100)])
print(f'dataset2:\n{dataset2}\nNumber of samples: {len(dataset2)}')
print('plt.hist(dataset2, bins=20)')
plt.hist(dataset1, bins=20)
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequencies')
plt.show()

print()
print('Histogram with outlined bins')
dataset3 = np.array([randint(10,100) for i in range(50)])
print(f'dataset3:\n{dataset3}\nNumber of samples: {len(dataset3)}')
print('plt.hist(dataset3, ec=\'back\')')
plt.hist(dataset3, ec='black')
plt.title('Histogram with Outlined Bins')
plt.xlabel('Values')
plt.ylabel('Frequencies')
plt.show()

print()
print('Horizontal-oriented Histogram')
dataset4 = np.array([randint(10,100) for i in range(50)])
print(f'dataset4:\n{dataset4}\nNumber of samples: {len(dataset4)}')
print('plt.hist(dataset4, orientation=\'horizontal\', ec=\'black\')')
plt.hist(dataset4, orientation='horizontal', ec='black')
plt.title('Horizontal-oriented Histogram')
plt.xlabel('Frequencies')
plt.ylabel('Values')
plt.show()

print()
print('Multiple Histograms in the same plot')
# Plotted in blue
dataset5 = np.array([randint(10,100) for i in range(50)])
print(f'dataset5:\n{dataset5}\nNumber of samples: {len(dataset5)}')
print('plt.hist(dataset5, histype=\'step\', ec=\'black\')')
plt.hist(dataset5, ec='black')
print()
# Plotted in orange
dataset6 = np.array([randint(10,100) for i in range(50)])
print(f'dataset6:\n{dataset6}\nNumber of samples: {len(dataset6)}')
print('plt.hist(dataset6, ec=\'black\')')
plt.hist(dataset6, alpha=0.5, ec='black')
plt.title('Multiple Histograms')
plt.xlabel('Frequencies')
plt.ylabel('Values')
plt.show()