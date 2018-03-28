from matplotlib import pyplot as plt

print('Creating Figure objects')
#matplotlib.pyplot.figure(num=None, figsize=None, facecolor=None, edgecolor=None)

'''
Creates a new figure.
Returns: a Figure object.
If you are creating many figures, make sure you explicitly call 
matplotlib.pyplot.close() on the figures you are not using, 
because this will enable pylab to properly clean up the memory.
'''
'''
    num: nteger or string, optional, default: none. If not provided, 
a new figure will be created, and the figure number will be 
incremented. The figure objects holds this number in a number 
attribute. If num is provided, and a figure with this id already 
exists, make it active, and returns a reference to it. If this 
figure does not exists, create it and returns it. If num is a string, 
the window title will be set to this figure’s num.
    figsize: tuple of integers (width, height in inches), optional. 
If not provided, defaults to rc figure.figsize (None).
    facecolor: the background color.
    edgecolor: the border color.
'''
plt.figure(figsize=(10,8))
plt.plot(list(range(20,-1,-1)))
plt.savefig('matplotlib_figure_example.png', format='png')
plt.show()


#matplotlib.pyplot.savefig(fname, format=None, transparent=False)
'''
Save the current figure.
Should be called before plt.show() otherwise the figure won't be
saved properly.
'''
'''
    fname: A string containing a path to a filename, or a Python file-like 
object, or possibly some backend-dependent object such as PdfPages. If 
format is None and fname is a string, the output format is deduced from the 
extension of the filename. If the filename has no extension, the value 
of the rc parameter savefig.format is used. If fname is not a string, 
remember to specify format to ensure that the correct backend is used.
    format: One of the file extensions supported by the active backend. 
Most backends support png, pdf, ps, eps and svg.
    transparent: If True, the axes patches will all be transparent; 
the figure patch will also be transparent unless facecolor and/or 
edgecolor are specified via kwargs. This is useful, for example, 
for displaying a plot on top of a colored background on a web page. 
The transparency of these patches will be restored to their original 
values upon exit of this function.
'''


'''
Alternatively, an instance of the figure can be saved to a variable using
plt.gcf() (Get Current Figure) and then call plt.savefig() at any point.
'''