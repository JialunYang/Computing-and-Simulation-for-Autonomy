import cv2
import matploblib.pyplot as plt
import numpy as np

# Read the image.
img = cv2.imread('you_image.jpg')

# Visualize before
plt.axis('off')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# Apply bilateral filter
imgb = cv2.bilateralFilter(img, 9, 75, 75)

# Visualize after
plt.axis('off')
plt.imshow(cv2.cvtColor(imgb, cv2.COLOR_BGR2RGB))

# Save the output.
cv2.imwrite('bilateral.jpg', bilateral)