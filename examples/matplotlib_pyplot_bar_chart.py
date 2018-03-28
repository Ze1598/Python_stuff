from matplotlib import pyplot as plt
import numpy as np

print('Bar Chart')
#matplotlib.pyplot.bar(*args, **kwargs)
'''
Make a bar plot.
'''
'''
Call signatures:
bar(x, height, *, align='center', **kwargs)
bar(x, height, width, *, align='center', **kwargs)
bar(x, height, width, bottom, *, align='center', **kwargs)
'''
'''
Make a bar plot with rectangles bounded by
(x - width / 2, x + width / 2, bottom, bottom + height)
(left, right, bottom and top edges) by default. x, height, width, 
and bottom can be either scalars or sequences.
The align and orientation kwargs control the interpretation of 
x and bottom.
The align keyword-only argument controls if x is interpreted as 
the center or the left edge of the rectangle.
'''
'''
    x: sequence of scalars. The x coordinates of the bars.
    height: scalar or sequence of scalars. The height(s) 
of the bars.
    width: scalar or array-like, optional. The width(s) of 
the bars. Defaults to 0.8.
    bottom: scalar or array-like, optional. The y 
coordinate(s) of the bars. Defaults to None.
    align: {‘center’, ‘edge’}, optional. Defaults to 'center'.
align controls if x is the bar center (default) or left edge.
If ‘center’, interpret the x argument as the coordinates of 
the centers of the bars. If ‘edge’, aligns bars by their left edges.
To align the bars on the right edge pass a negative width and 
align='edge'.
    It also takes other optional stylistic parameters such 
as color, edgecolor, linewidth, etc.
'''
#Since the plotted graphs are center-aligned by default, we won't\
#be using the 'align' kwarg in these examples
print('bar(x, height, align=\'center\')')
#Values for each bar (y-axis values)
bar_heights = [20, 33, 54, 15, 22, 87, 70, 99, 43, 61]
#Values for each bar (x-axis values); strings in this case
bar_names = ['Bar '+str(i) for i in range(len(bar_heights))]
#Plot the bar chart, center-aligned
plt.bar(bar_names, bar_heights)
#Title the chart and label the axis
plt.title('Bar Chart')
plt.xlabel('Bars')
plt.ylabel('Bar Heights')
plt.show()
print()


print('Side-by-side Bar Chart')
'''
Make a bar chart that contains more than one data set, to facilitate
its comparion.
'''
'''
Use matplotlib.pyplot.bar() once again, simply call the function for each
data set you want to plot before show()ing the graph.
'''
'''
By default, the first dataset's bars are blue and the second's are orange.
'''
x_labels = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
dataset2_1 =  [91, 76, 56, 66, 52, 27]
dataset2_2 = [65, 82, 36, 68, 38, 40]
#Bar width (for both datasets)
width = 0.8
#Distance between bars of the same dataset
bar_dist = 2

#Set the x values for each bar of the first dataset
dataset2_1_xValues = [bar_dist*i + width*1 for i in range(len(x_labels))]
#Plot the first dataset
plt.bar(dataset2_1_xValues, dataset2_1)

#Set the x values for each bar of the second dataset
dataset2_2_xValues = [bar_dist*i + width*2 for i in range(len(x_labels))]
#Plot the second dataset
plt.bar(dataset2_2_xValues, dataset2_2)

#Label the graph and axis
plt.title('Side-by-Side Bar Chart')
plt.xlabel('Bars')
plt.ylabel('Heights')

plt.show()
print()


print('Stacked Bars Chart')
#bar(x, height, bottom=dataset, align='center')
'''
Useful to compare two sets of data while preserving the total between
the two.
Example: compare how many hours you've spent playing games and reading
books, while preserving the total number of hours spent with these two
activities.
'''
print('bar(x, height, bottom=dataset, align=\'center\')')
'''
    bottom: scalar or array-like, optional. The dataset being plotted
will be stacked on top of the given dataset.
'''
dataset3_1 =  [91, 76, 56, 66, 52, 27]
dataset3_2 = [65, 82, 36, 68, 38, 40]

#Plot the bar chart for dataset3_1
plt.bar(range(len(dataset3_1)), dataset3_1)
#Plot the bar chart for dataset3_2 and stack it on top of
#dataset3_1's chart
plt.bar(range(len(dataset3_2)), dataset3_2, bottom=dataset3_1)

#Label the graph and axis and create a legend for the charts
plt.title('Stacked Bar Chart')
plt.xlabel('Bars')
plt.ylabel('Heights')
plt.legend(['dataset3_1', 'dataset3_2'])

plt.show()
print()



print('Bar Chart with Errorbars')
#bar(x, height, bottom=dataset, yerr=array, align='center')
'''
A bar chart with the errorbars drawn for each bar.
'''
print('bar(x, height, bottom=dataset, yerr=array, capsize=int, align=\'center\')')
'''
    yerr: scalar or array-like, optional. If not None, will be used to 
generate errorbar(s) on the bar chart. Defaults to None.
    capsize : scalar, optional. Determines the length in points of 
the error bar caps.
'''
#Create a dataset, containing the numbers from 1 to 10, inclusive
dataset4 = np.arange(1, 11)
print(f'Dataset4:\n{dataset4}')
#Calculate the dataset's mean and standard deviation
dataset4_mean = np.mean(dataset4)
dataset4_std = np.std(dataset4)
print('Mean => ', dataset4_mean, 'Std. Dev. =>', dataset4_std)
#yerr could be an array of length equal to dataset4, so that each bar would\
#have the error bars would have different size
plt.bar(np.arange(1, len(dataset4)+1), dataset4, yerr=dataset4_std, capsize=7)
#Label the graph and axis
plt.title('Bar Chart with Errorbars')
plt.xlabel('Bars')
plt.ylabel('Heights')

plt.show()