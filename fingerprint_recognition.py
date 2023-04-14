import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the fingerprint image in grayscale
image_path = './images/fingerprint2.jpg'
# image_path = './fingerprint2.jpg'

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply a binary threshold to create a black and white image
_, thresholded_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define the structuring element for the morphological operations (here, a 3x3 square)
structuring_element = np.ones((3, 3), np.uint8)

# Perform erosion
eroded_image = cv2.erode(thresholded_image, structuring_element, iterations=1)

# Perform dilation
dilated_image = cv2.dilate(thresholded_image, structuring_element, iterations=1)

# Perform opening (erosion followed by dilation)
opened_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_OPEN, structuring_element)

# Perform closing (dilation followed by erosion)
closed_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_CLOSE, structuring_element)

# Display the original and processed images in matplotlib
fig, axes = plt.subplots(1, 5, figsize=(12, 12))
axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image')
axes[1].imshow(eroded_image, cmap='gray')
axes[1].set_title('Eroded Image')
axes[2].imshow(dilated_image, cmap='gray')
axes[2].set_title('Dilated Image')
axes[3].imshow(opened_image, cmap='gray')
axes[3].set_title('Opened Image')
axes[4].imshow(closed_image, cmap='gray')
axes[4].set_title('Closed Image')

# Remove axis ticks
for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])

# Save the image as output
plt.savefig('output_image2.png', bbox_inches='tight', dpi=300)

# Show the image
plt.show()