import numpy as np
import matplotlib.pyplot as plt

# Return 256 evenly spaced numbers over the (-pi,pi) range.
# pi is the last sample
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

# Call the cosine and sine mathematical functions on the\
# created array
cosine = np.cos(x)
sine = np.sin(x)

# Plot the cosine array in a blue line with a width value of 2.5
plt.plot(x, cosine, color='blue', linewidth=2.5, label='Cosine')

# Plot the sine array in an orange line with a width value of 2.5
plt.plot(x, sine, color='orange', linewidth=2.5, label='Sine')

# Add a legend to the upper left corner
plt.legend(loc='upper left')

# Get an axis object (Get Current Axis)
axis = plt.gca()

axis.spines['right'].set_color('none')

axis.spines['bottom'].set_position(('data', 0))
axis.yaxis.set_ticks_position('left')

axis.spines['left'].set_position(('data', 0))

axis.spines['top'].set_color('none')
axis.xaxis.set_ticks_position('bottom')

# Define the limits for x axis
plt.xlim(-5.0, 5.0)
# Define values for the x axis ticks
plt.xticks(np.linspace(-4.5, 4.5, 9, endpoint=True))

# Define the limits for y axis
plt.ylim(-1.25, 1.25)
# Define values for the y axis ticks
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

plt.show()