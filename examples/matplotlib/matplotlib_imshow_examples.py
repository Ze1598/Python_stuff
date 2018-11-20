import numpy as np
import matplotlib.pyplot as plt

'''
    Plot a mathematical function, with a sample of 5000 points
'''
# 5000-number-long array with numbers between -25 and 25
points = np.arange(-25, 25, 0.01)

# Arrays [x,y] as a grid of coordinates
x, y = np.meshgrid(points, points)

# sqrt(x**2 + y**2)
z = np.sqrt(x**2 + y**2)

# Plot the expression (points are colored in a blue tint)
plt.imshow(z, cmap=plt.cm.Blues)
# Add a colorbar to the graph
plt.colorbar()
# Define the graph title
plt.title('Graphical visualization of $\sqrt{x^2 + y^2}$ (5000 points)')
# Show the plotted graph
plt.show()




'''
    Plot an array of 50 colored points.
'''
# 2D array of 50x50 size
points = np.random.rand(150, 150)
# Plot the points with a red-tint
plt.imshow(points, cmap=plt.cm.Reds)
plt.colorbar()
plt.title('Colored Points')
plt.show()