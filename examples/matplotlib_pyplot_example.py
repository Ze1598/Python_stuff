from matplotlib import pyplot

#y-values to be plotted in the graph
#The x-values will be the index of each value, i.e. (0,1), (1,3), (2,8) and (3,4)
y = [1, 3, 8, 4]
#Plot a graph with the y-values contained in the 'y' list, using black dashed lines
pyplot.plot(y, 'k--', linewidth=3)
#Name the y-axis "Y Axis Values"
pyplot.ylabel('Y Axis Values')
#Name the x-axis "X Axis Values"
pyplot.xlabel('X Axis Values')
#Plot the graph in a new window
pyplot.show()

'''The second window will show once the first is closed'''

#Coordinates for the new graph
coord = [('a',1), ('b',4), ('c',9), ('d',16)]
#Get a list with the x-values
y_coord = [i[1] for i in coord]
#Get a list with the y-values
x_coord = [i[0] for i in coord]
#Plot a graph with the three coordinates from 'coord', drawing only the coordinates, as red pentagons
pyplot.plot(x_coord, y_coord, 'rp')
#Plot the graph in a new window
pyplot.show()

'''The third window will show once the second is closed'''

#The third uses a the 'x_coord' x-values for both data series, with the first one using the y-values\
#from the first graph, and the second series uses the y-values from the second graph
#Plot the first data series using a black line
pyplot.plot(x_coord, y, 'k', label='Series 1')
#Plot the second data series using a red line
pyplot.plot(x_coord, y_coord, 'r', label='Series 2')
#Before plotting the graph, create a legend for it: drawn on the upper left corner, with drop shadow and
#blue background; it contains the titles(labels) for each series in the graph
legend = pyplot.legend(loc='upper left', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor((0,0,1))
#Plot the graph in a new window
pyplot.show()