from matplotlib import pyplot as plt
import numpy as np
from random import randint

print('Pie Chart')
# matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None,
# autopct=None, pctdistance=0.6, labeldistance=1.1, startangle=None, 
# radius=None, counterclock=True, center=(0, 0), frame=False, 
# rotatelabels=False)
'''
Plot a pie chart.
Make a pie chart of array x. The fractional area of each wedge is 
given by x/sum(x). 
If sum(x) <= 1, then the values of x give the fractional area directly 
and the array will not be normalized. The wedges are plotted counterclockwise, 
by default starting from the x-axis.
'''
print('matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, labeldistance=1.1, startangle=None, radius=None, counterclock=True, center=(0, 0), frame=False, rotatelabels=False)')
'''
    x: array-like. The input array used to make the pie chart.
    explode: array-like, optional, defaults to None. If not 
None, is a len(x) array which specifies the fraction of the 
radius with which to offset each wedge.
    labels: list, optional, defaults to None. A sequence of 
strings providing the labels for each wedge.
    colors: array-like, optional, defaults to None. A sequence 
of matplotlib color args through which the pie chart will cycle. 
If None, will use the colors in the currently active cycle.
    autopct : None (default), string, or function, optional. 
If not None, is a string or function used to label the wedges 
with their numeric value. The label will be placed inside the 
wedge. If it is a format string, the label will be of the
fmt%pct format. If it is a function, it will be called.
    pctdistance : float, optional, defaults to 0.6. The ratio 
between the center of each pie slice and the start of the text 
generated by autopct. Ignored if autopct is None.
    labeldistance: float, optional, defaults to 1.1. The radial 
distance at which the pie labels are drawn.
    startangle: float, optional, defaults to None. If not None, 
rotates the start of the pie chart by angle degrees counterclockwise 
from the x-axis.
    radius: float, optional, defaults to None. The radius of the pie, 
if radius is None it will be set to 1.
    counterclock:  bool, optional, defaults to True. Specify the 
direction, clockwise or counterclockwise.
    center: list of float, optional, defaults to (0, 0). Center 
position of the chart. Takes value (0, 0) or is a sequence of 2 scalars.
    frame: bool, optional, defaults to False. Plot axes frame with the 
chart if true.
    rotatelabels: bool, optional, defaults to False. Rotate each label 
to the angle of the corresponding slice if true.
'''
'''
autopct common formats:
    '%0.2f' — 2 decimal places, like 4.08.
    '%0.2f%%' — 2 decimal places, but with a percent sign at the end, 
like 4.08%. Two consecutive percent signs are needed, otherwise it
will be escaped in the string without being displayed.
    '%d%%' — rounded to the nearest int and with a percent sign at the 
end, like 4%.
'''

print()
print('Basic Pie Chart with labels')
dataset1 = np.array([randint(1,50) for i in range(10)])
ds1_labels = np.array(['Wedge'+str(i) for i in range(len(dataset1))])
print(f'dataset1:\n{dataset1}\nds1_labels:\n{ds1_labels}')
print('plt.pie(dataset1, labels=ds1_labels)')
plt.pie(dataset1, labels=ds1_labels)
plt.title('Pie Chart')
# Changes limits of x or y axis so that equal increments of x and y\
# have the same length; a circle is circular
plt.axis('equal')
plt.show()
print()

print('Pie Chart with legend')
dataset2 = np.array([randint(1,50) for i in range(5)])
ds2_labels = np.array(['Wedge'+str(i) for i in range(len(dataset2))])
print(f'dataset2:\n{dataset2}\nds2_labels:\n{ds2_labels}')
print('plt.pie(dataset2, counterclock=False)')
plt.pie(dataset2, counterclock=False)
plt.title('Pie Chart')
# Create a legend for the chart using the ds2_labels array
plt.legend(ds2_labels, loc='upper left')
plt.show()
print()

print('Pie Chart with wedge percentages')
dataset3 = np.array([randint(1,50) for i in range(10)])
ds3_labels = np.array(['Wedge'+str(i) for i in range(len(dataset3))])
print(f'dataset3:\n{dataset3}\nds3_labels:\n{ds3_labels}')
print('plt.pie(dataset3, labels=ds3_labels, autopct="%0.2f%%")')
# Display the percentage each slice occupies. In this case, the\
# values are displayed with 2 decimal places, along with the\
# percent sign
plt.pie(dataset3, labels=ds3_labels, autopct='%0.2f%%')
# plt.pie(dataset3, labels=ds3_labels, autopct='%0.2f%%', pctdistance=0.7)
plt.title('Pie Chart')
plt.show()