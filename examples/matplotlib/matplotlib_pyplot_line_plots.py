from matplotlib import pyplot as plt
import numpy as np

#y-values to be plotted in the graph
#The x-values will be the index of each value, i.e. (0,1), (1,3), (2,8) and (3,4)
y = [1, 3, 8, 4]
#Plot a graph with the y-values contained in the 'y' list, using black dashed lines
plt.plot(y, 'k--', linewidth=3)
#Name the y-axis "Y Axis Values"
plt.ylabel('Y Axis Values')
#Name the x-axis "X Axis Values"
plt.xlabel('X Axis Values')
#Name the graph
plt.title('First Graph')
#Plot the graph in a new window
plt.show()


#Coordinates for the new graph
coord = [('a',1), ('b',4), ('c',9), ('d',16)]
#Get a list with the x-values
y_coord = [i[1] for i in coord]
#Get a list with the y-values
x_coord = [i[0] for i in coord]
#Plot a graph with the three coordinates from 'coord', drawing only the coordinates, as red pentagons
plt.plot(x_coord, y_coord, 'rp')
#Name the graph
plt.title('Second Graph')
#Plot the graph in a new window
plt.show()


#The third graph uses the 'x_coord' x-values for both data series, with the first one using the y-values\
#from the first graph, and the second series uses the y-values from the second graph
#Plot the first data series using a black line
plt.plot(x_coord, y, 'k', label='Series 1')
#Plot the second data series using a red line
plt.plot(x_coord, y_coord, 'r', label='Series 2')
#Before plotting the graph, create a legend for it: drawn on the upper left corner, with drop shadow and
#blue background; it contains the titles(labels) for each series in the graph
legend = plt.legend(loc='upper left', shadow=True, fontsize='x-large')
'''
loc argument positional values:
Number Code 	String
0 	            best
1 	            upper right
2 	            upper left
3 	            lower left
4 	            lower right
5 	            right
6 	            center left
7 	            center right
8 	            lower center
9 	            upper center
10 	            center
'''
legend.get_frame().set_facecolor((0,0,1))
#Name the graph
plt.title('Third Graph')
#Plot the graph in a new window
plt.show()


#Sometimes, we want to display two lines side-by-side,\
#rather than in the same set of x and y-axes. When this\
#happens, each set of axes is called a subplot. 
#The picture or object that contains all of the subplots 
#is called a figure.
#matplotlib.plt.subplot(*args, **kwargs)
'''
Return a subplot axes positioned by the given grid definition.
Typical call signature: subplot(nrows, ncols, plot_number).
'''
'''
Where nrows and ncols are used to notionally split the figure
into nrows * ncols sub-axes, and plot_number is used to 
identify the particular subplot that this function is to 
create within the notional grid. 
plot_number starts at 1, increments across rows first and 
has a maximum of nrows * ncols.
In the case when nrows, ncols and plot_number are all less 
than 10, a convenience exists, such that a 3 digit number 
can be given instead, where the hundreds represent nrows, 
the tens represent ncols and the units represent plot_number.
'''
'''
For instance, subplot(211) produces a subaxes in a figure 
which represents the top plot (i.e. the first) in a 2 row 
by 1 column notional grid (no grid actually exists, but 
conceptually this is how the returned subplot has been 
positioned).
'''
plt.plot([1,2,3])
'''
Now create a subplot which represents the top plot of a grid
with 2 rows and 1 column. Since this subplot will overlap the
first, the plot (and its axes) previously created, will be removed
'''
plt.subplot(211)
plt.plot(range(12))
plt.subplot(212, facecolor='y') #Creates 2nd subplot with yellow background
'''
    facecolor: The background color of the subplot, which can be 
any valid color specifier.
'''
plt.show()
#If you do not want this behavior, use the add_subplot() method
#add_subplot(*args, **kwargs)
'''
Add a subplot.
    *args: Either a 3-digit integer or three separate 
integers describing the position of the subplot. If the 
three integers are I, J, and K, the subplot is the Ith 
plot on a grid with J rows and K columns.
    projection : [‘aitoff’ | ‘hammer’ | ‘lambert’ | 
‘mollweide’, ‘polar’ | ‘rectilinear’], optional. 
The projection type of the axes.
'''

#Source: matplotlib.org/2.1.0/gallery/subplots_axes_and_figures/subplot.py
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show()


#matplotlib.pyplot.subplots_adjust(*args, **kwargs)
'''
Adjust the subplot layout.
Call signature:
subplots_adjust(left=None, bottom=None, right=None, top=None,
                    wspace=None, hspace=None)
'''
'''
The parameter meanings (and suggested defaults) are:
    left  = 0.125:  the left side of the subplots of the figure
    right = 0.9:    the right side of the subplots of the figure
    bottom = 0.1:   the bottom of the subplots of the figure
    top = 0.9:      the top of the subplots of the figure
    wspace = 0.2:   the amount of width reserved for blank space between subplots,
expressed as a fraction of the average axis width
    hspace = 0.2:   the amount of height reserved for white space between subplots,
expressed as a fraction of the average axis height
'''
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

#Subplot 1
plt.subplot(211)
plt.plot(x, straight_line)

#Subplot 2
plt.subplot(223)
plt.plot(x, parabola)

#Subplot 3
plt.subplot(224)
plt.plot(x, cubic)

plt.subplots_adjust(wspace=0.35, bottom=0.2)

plt.show()

print('Subplots')
'''
Because our plots can have multiple subplots, we have to 
specify which one we want to modify. In order to do that, 
we call plt.subplot in a different way.

ax = plt.subplot(1, 1, 1)
ax is an axes object, and it lets us modify the axes belonging 
to a specific subplot. Even if we only have one subplot, when 
we want to modify the ticks, we will need to start by calling 
either ax = plt.subplot(1, 1, 1) or ax = plt.subplot() in order 
to get the axes object.

Suppose we wanted to set  x-ticks to be at 1, 2, and 4. We would 
use the following code:
'''
ax = plt.subplot()
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
ax.set_xticks([1, 2, 4])
'''
We can also modify the y-ticks by using ax.set_yticks.
When we change the x-ticks, their labels automatically change to match. 
But, if we want special labels (such as strings), we can use the command 
ax.set_xticklabels or ax.set_yticklabels. 

For example, we might want to have a y-axis with ticks at 0.1, 0.6, and 0.8, 
but label them 10%, 60%, and 80%, respectively. 
To do this, we use the following commands:
'''
ax = plt.subplot()
plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o')
ax.set_yticks([0.1, 0.6, 0.8])
ax.set_yticklabels(['10%', '60%', '80%'])

print('Close windows')
#matplotlib.pyplot.close(*args)
'''
Close a figure window.
'''
'''
close() by itself closes the current figure
close(h) where h is a Figure instance, closes that figure
close(num) closes figure number num
close(name) where name is a string, closes figure with that label
close('all') closes all the figure windows
'''