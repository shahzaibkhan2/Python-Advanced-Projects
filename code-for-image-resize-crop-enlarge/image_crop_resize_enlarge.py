# Import PIL module
from PIL import Image

# Load the image
image = Image.open('sample.jpg')

# Resize the image
resized_image = image.resize((500, 500))

# Crop the image
width, height = image.size
left = (width - 500) / 2
top = (height - 500) / 2
right = (width + 500) / 2
bottom = (height + 500) / 2
cropped_image = image.crop((left, top, right, bottom))

# Enlarge the image
enlarged_image = image.resize((width * 2, height * 2))

# Save the images
resized_image.save('resized.jpg')
cropped_image.save('cropped.jpg')
enlarged_image.save('enlarged.jpg')
