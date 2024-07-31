#import cv2
#import numpy as np
def custom_erode(image, kernel):

  # Pad the image with zeros to handle boundary conditions
  pad_width = int((len(kernel[0]) - 1) / 2)
  padded_image = []
  for row in range(-pad_width, len(image) + pad_width):
    padded_row = []
    for col in range(-pad_width, len(image[0]) + pad_width):
      if 0 <= row < len(image) and 0 <= col < len(image[0]):
        padded_row.append(image[row][col])
      else:
        padded_row.append(0)
    padded_image.append(padded_row)

  # Perform erosion by iterating through each pixel
  eroded_image = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
  for row in range(pad_width, len(padded_image) - pad_width):
    for col in range(pad_width, len(padded_image[0]) - pad_width):
      is_eroded = True
      for i in range(-pad_width, pad_width + 1):
        for j in range(-pad_width, pad_width + 1):
          if kernel[i + pad_width][j + pad_width] == 1 and padded_image[row + i][col + j] == 0:
            is_eroded = False
            break
      if is_eroded:
        eroded_image[row - pad_width][col - pad_width] = padded_image[row][col]

  return eroded_image


#######################################################################################################################
###################################           For Try                 #################################################

""" # Read the image
image = cv2.imread("Erosion.png", cv2.IMREAD_GRAYSCALE)
image = image.tolist()  # Convert to 2D list

# Define a simple kernel (replace with your desired kernel)
kernel = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]

# Perform custom erosion
eroded_image = custom_erode(image, kernel)

# The code below saves image as eroded. But we don't have to use numpy so I couldn't save an existing image without them.
# But it seems codes running well when I try to get result with using numpy
eroded_image_cv2 = np.array(eroded_image, dtype=np.uint8)  # Convert back for saving with cv2
cv2.imwrite("Eroded_Custom.png", eroded_image_cv2)  """