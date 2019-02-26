from PIL import Image, ImageDraw, ImageFont
import math

# Define the size of the image
width, height = (208, 567)
# Open the image to be used
center_img = Image.open('picture.png', 'r')

# List of names
boys = ['AFONSO', 'GUSTAVO', 'JOÃO', 'JOSÉ', 'LUCAS', 'MARTIM', 'MIGUEL', 'PEDRO', 'RAFAEL', 'TOMÁS TAVARES', 'TOMÁS TEIXEIRA', 'TOMÁS LOPES', 'ENZO', 'RUI', 'RUBEN']
girls = ['BIANCA', 'LEONOR FERNANDES', 'LEONOR SILVA', 'MARIA CLARA', 'MATILDE BRANDÃO', 'MATILDE MOREIRA', 'RITA', 'SOFIA','YARA', 'ALICE', 'LUANA','ISOLINA FERNANDA', 'MATILDE FARIA', 'CLÁUDIA', 'FABIANA', 'LARA GOUVEIA', 'LARA MENDES', 'MARIANA SANTOS', 'MARIANA MADEIRA', 'CAROLINA']
# Make a single list of both lists of names
names = boys+girls


# Define font size to use
fnt_size = 32
# Load the font to be used
fnt = ImageFont.truetype("arial.ttf", fnt_size, encoding="unic")


# Loop through the list of names to create an image for each name
for name in names:
	# Create a basic RGB image of the desired size and background color
	img = Image.new('RGB', (208,567), color=(249, 249, 249))

	# Split the current name to know of how many names it's composed of
	name_sep = name.split()

	# If the name is composed of two names, they'll be drawn\
	# higher than if it it was a single name
	if len(name_sep) != 1:
		d = ImageDraw.Draw(img)
		# Get the text dimensions of the first name
		w1, h1 = d.textsize(name_sep[0], font=fnt)
		# Get the text dimensions of the second name
		w2, h2 = d.textsize(name_sep[1], font=fnt)
		# x-coordinate to draw the first name (horizontally centered)
		x1 = (width-w1)/2
		# x-coordinate to draw the second name (horizontally centered)
		x2 = (width-w2)/2

		# Draw the first name at the set coordinates
		d.text(
			(x1,393), 
			name_sep[0],
			font=fnt,
			fill='black'
		)

		# Draw the second name at the set coordinates
		d.text(
			(x2,430), 
			name_sep[1],
			font=fnt,
			fill='black'
		)

	# If the name is composed of a single name
	else:
		d = ImageDraw.Draw(img)
		# Get the text dimensions
		w1, h1 = d.textsize(name_sep[0], font=fnt)
		# x-coordinate to draw the name (horizontally centered)
		x = (width-w1)/2
		# Draw the name
		d.text(
			(x,410), 
			name_sep[0],
			font=fnt,
			fill='black'
		)

	# Text to be added at the top of the image
	header_text = "1º ANO"
	d = ImageDraw.Draw(img)
	d_w, d_h = d.textsize(header_text, font=fnt)
	# Center the text horizontally
	d_x = (width-d_w)/2
	# Draw the text
	d.text(
		(d_x,50), 
		header_text,
		font=fnt,
		fill='black'
	)

	# After drawing the text, add the loaded image at the set coordinates
	img.paste(center_img, (0,135), mask=center_img)

	# Save the resulting image as a .png (the file name is the name\
	# currently being used by the loop)
	img.save(f'created\\{name}.png')