import numpy as np
import matplotlib.pyplot as plt
from requests import get
from PIL import Image
from io import BytesIO

def plot_image(url):
	'''
	Plot an image in a 2D graph given the image URL.

	Parameters:
	-----------
	url : string
		The image's URL.

	Returns:
	-------
	None
	'''
	# "Download" the image
	# Make a GET request for the image
	img_req = get(url)
	# Then save the image as a BytesIO object, that is, a\
	# stream of data (a bytes object)
	get_img = Image.open(BytesIO(img_req.content))
	# Plot the image in a graph using imshow()
	plt.imshow(np.array(get_img))
	# Show the plotted graph
	plt.show()


if __name__ == "__main__":
	img_url = input("Enter the URL of the image to be ploted: ")
	plot_image(img_url)