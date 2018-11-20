from PIL import Image, ImageFilter
import os

# Create an Image object from an existing image
image1 = Image.open('sample_graph.png')

# Open the image using the default installed software (e.g. Windows Photos)
image1.show()

# Save an Image object as an image
image1.save('sample_graph__.png')

# Rotate an image
image1.rotate(90).save('sample_graph_rotated.png')

# Make a picture black and white
image1.convert(mode='L').save('sample_graph_bw.png')

# Apply a Gaussian blur to the image
image1.filter(ImageFilter.GaussianBlur(radius=5)).save('sample_graph_blur.png')

# For each .jpg in the folder, save those .jpg as .png on the "PNGs" folder

# Loop through the contents of the current directory
for f in os.listdir('.'):
    # If the file is a JPEG image
    if f.endswith('.jpg'):
        # Create an Image object using that image
        i = Image.open(f)
        # Split the name of the image to extract the filename\
        # and the file extension
        fn, fext = os.path.splitext(f)
        # Save the file as a .png on the "PNGs" folder
        i.save(f'PNGs/{fn}.png')

# For each image JPEG or PNG image in the folder, save it as\
# a .png image in the "resized" folder, resized to the chosen\
# dimensions

# Loop through the contents of the current directory
for f in os.listdir('.'):
    # If the file is a JPEG or PNG image
    if f.endswith('.jpg') or f.endswith('.png'):
        # Create an Image object using that image
        i = Image.open(f)
        # Split the name of the image to extract the filename\
        # and the file extension
        fn, fext = os.path.splitext(f)
        # Resize the image to 300x300
        i.thumbnail((300, 300))
        # Save the file as a .png on the "resized" folder
        i.save(f'resized/{fn}_resized.png')