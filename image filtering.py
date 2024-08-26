import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image
import urllib.request
import io

# Load the image from the given URL
image_url = 'https://github.com/AnudipAE/DANLC/blob/master/dog.jpg?raw=true'
with urllib.request.urlopen(image_url) as url:
    image_file = io.BytesIO(url.read())

# Open the image and convert it to a NumPy array
original_image = np.array(Image.open(image_file))

# Convert the image to grayscale for filtering
gray_image = np.dot(original_image[..., :3], [0.2989, 0.587, 0.114])

# Apply Sobel filter along x-axis and y-axis
sobel_x = ndimage.sobel(gray_image, axis=0)
sobel_y = ndimage.sobel(gray_image, axis=1)

# Combine the two directional gradients
sobel_filtered_image = np.hypot(sobel_x, sobel_y)

# Display the original and filtered images
plt.figure(figsize=(12, 8))

# Original Image
plt.subplot(2, 1, 1)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')

# Sobel Filtered Image
plt.subplot(2, 1, 2)
plt.imshow(sobel_filtered_image, cmap='nipy_spectral')
plt.title('Filtered Image (Sobel Filter)')
plt.axis('off')

plt.show()
