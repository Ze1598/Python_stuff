from matplotlib import pyplot as plt
import numpy as np
from random import choice

print('matplotlib.pyplot.fill_between(x, y1, y2=0, where=None, alpha=float)')
'''
Make filled polygons between two curves.
Create a PolyCollection filling the regions between y1 and y2 where where==True.
'''
#matplotlib.pyplot.fill_between(x, y1, y2=0, where=None, alpha=float)
'''
    x: array. An N-length array of the x data.
    y1: array. An N-length array (or scalar) of the y data (lower bound).
    y2: array. An N-length array (or scalar) of the y data (upper bound).
    where: array, optional. If None, default to fill between everywhere. 
If not None, it is an N-length numpy boolean array and the fill will only 
happen over the regions where where==True.
'''
#The y-values for the dataset
dataset = np.array([3, 22, 43, 35, 10, 2, 17])
#The x-values for the dataset
dataset_xValues = np.arange(len(dataset))
#Lower bounds for the fill
y_lower = np.array([i-2 for i in dataset])
#Upper bounds for the fill
y_upper = np.array([i+2 for i in dataset])
#Create a numpy array with Boolean values; True will make that region be\
#filled, False does not
where_choice = np.array([choice((True, False)) for i in range(len(dataset))])
print(where_choice)

#First fill the desired area, everything in two vertical units distance of\
#the plotted dataset with 30% of transparency (0 <= alpha <= 1)
plt.fill_between(dataset_xValues, y_lower, y_upper, alpha=0.3)
#Plot the dataset as usual
plt.plot(dataset_xValues, dataset)
#Finally show the graphic in a new window
plt.show()


#Fill the areas where where==True, with 30% transparencery
plt.fill_between(dataset_xValues, y_lower, y_upper, where=where_choice, alpha=0.3)
#Plot the dataset as usual
plt.plot(dataset_xValues, dataset)
#Finally show the graphic in a new window
plt.show()