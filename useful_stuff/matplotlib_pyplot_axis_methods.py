matplotlib.pyplot.axis(*v, **kwargs)

axis()
#Calling with no arguments returns the current 
#axes limits: [xmin, xmax, ymin, ymax]

axis(v)
#Sets the min and max of the x and y axes, 
#with v = [xmin, xmax, ymin, ymax]

axis('off')
#Turns off the axis lines and labels

axis('equal')
#Changes limits of x or y axis so that equal 
#increments of x and y have the same length

axis('scaled')
#Achieves the same result by changing the dimensions 
#of the plot box instead of the axis data limits

axis('tight')
#Changes x and y axis limits such that all data is
#shown. If all data is already shown, it will move it 
#to the center of the figure without modifying 
#(xmax - xmin) or (ymax - ymin)

axis('image')
#Is ‘scaled’ with the axis limits equal to the data limits

#If len(*v)==0, you can pass in xmin, xmax, ymin, ymax as 
#kwargs selectively to alter just those limits without 
#changing the others

axis('square')
#Changes the limit ranges (xmax-xmin) and (ymax-ymin) 
#of the x and y axes to be the same, and have the same 
#scaling, resulting in a square plot