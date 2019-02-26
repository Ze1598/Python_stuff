from PIL import Image, ImageDraw, ImageFont
import math

# Define the size of the image
width, height = (246, 302)
# Open the flower background image
flower_bg = Image.open('flor_clean.png', 'r')
# Open the car background image
car_bg = Image.open('carro.png', 'r')

# List of names
boys = ['AFONSO', 'GUSTAVO', 'JOÃO', 'JOSÉ', 'LUCAS', 'MARTIM', 'MIGUEL', 'PEDRO', 'RAFAEL', 'TOMÁS TAVARES', 'TOMÁS TEIXEIRA', 'TOMÁS LOPES', 'ENZO', 'RUI', 'RUBEN']
girls = ['BIANCA', 'LARA', 'LEONOR FERNANDES', 'LEONOR SILVA', 'MARIA CLARA', 'MATILDE BRANDÃO', 'MATILDE MOREIRA', 'RITA', 'SOFIA','YARA', 'ALICE', 'LUANA','ISOLINA FERNANDA', 'MATILDE FARIA', 'CLÁUDIA', 'FABIANA', 'LARA GOUVEIA', 'LARA MENDES', 'MARIANA SANTOS', 'MARIANA MADEIRA', 'CAROLINA']


# Define font size to use
fnt_size = 24
# Load the font to be used
fnt = ImageFont.truetype("arial.ttf", fnt_size, encoding="unic")


# Loop through the names in the boys list to create their images
for name in boys:

	# Create a basic RGB white image of the desired size
	img = Image.new('RGB', (246,302), color='white')
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
			(x1,129), 
			name_sep[0],
			font=fnt,
			fill='black'
		)
		
		# Draw the second name at the set coordinates
		d.text(
			(x2,163), 
			name_sep[1],
			font=fnt,
			fill='black'
		)

	# If the name is composed of a single name
	else:
		d = ImageDraw.Draw(img)
		# Get the text dimensions
		w1, h1 = d.textsize(name_sep[0], font=fnt)
		# x-coordinate to draw the name
		x = (width-w1)/2

		d.text(
			(x,129), 
			name_sep[0],
			font=fnt,
			fill='black'
		)

	# After drawing the name, paste the overlaying car background image
	img.paste(car_bg, (0,0), mask=car_bg)

	# Save the resulting image as a .png (the file name is the name\
	# currently being used by the loop)
	img.save(f'created\\{name}.png')



# Loop through the names in the girls list to create their images
for name in girls:

	# Create a basic RGB white image of the desired size
	img = Image.new('RGB', (246,302), color='white')
	# Split the current name to know of how many names it's composed of
	name_sep = name.split() 

	# If the name is composed of two names
	if len(name_sep) != 1:
		d = ImageDraw.Draw(img)
		# Get the text dimensions of the first name
		w1, h1 = d.textsize(name_sep[0], font=fnt)
		# Get the text dimensions of the second name
		w2, h2 = d.textsize(name_sep[1], font=fnt)
		# x-coordinate to draw the first name
		x1 = (width-w1)/2
		# x-coordinate to draw the second name
		x2 = (width-w2)/2

		d.text(
			(x1,129), 
			name_sep[0],
			font=fnt,
			fill='black'
		)

		d.text(
			(x2,163), 
			name_sep[1],
			font=fnt,
			fill='black'
		)

	# If the name is composed of a single name, just\
	# center the name horizontally, the vertical\
	# position is fixed
	else:
		d = ImageDraw.Draw(img)
		# Get the text dimensions
		w1, h1 = d.textsize(name_sep[0], font=fnt)
		# x-coordinate to draw the name
		x = (width-w1)/2

		d.text(
			(x,146), 
			name_sep[0],
			font=fnt,
			fill='black'
		)

	# After drawing the name, paste the overlaying background image
	img.paste(flower_bg, (0, 0), mask=flower_bg)

	# Save the resulting image as a .png (the file name is the name\
	# currently being used by the loop)
	img.save(f'created\\{name}.png')