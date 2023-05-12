import os
import cv2
import numpy as np
from utility.convert import bit16_dicom_to_bit16_png, bit16_to_bit8_png

class Preprocessing:

  def __init__(self, image, src_path, dist_path):
    self.src_path = src_path
    self.dist_path = dist_path
    self.image = image
    self.format = self.get_format() # .png, .dcm,...
    self.dtype = None if self.format == '.dcm' else self.image.dtype # uint8, uint16
  
  def get_format(self):
    ext = "." + os.path.splitext(self.src_path)[1].upper()[1:]
    return ext.lower()
  
  def process_image(self):
    if self.format == '.dcm':
      [self.image, self.format] = bit16_dicom_to_bit16_png(self.image)
      self.image = np.fliplr(self.image) if 'R' in self.src_path else self.image
      self.image = cut_and_resize_image(self.image)
      dist_path = os.path.splitext(self.dist_path)[0] + self.format
      cv2.imwrite(dist_path, self.image)

    elif self.dtype == 'uint16':
      [self.image, self.format] = bit16_to_bit8_png(self.image)
      self.image = cut_and_resize_image(self.image)
      cv2.imwrite(self.dist_path, self.image)

    elif self.dtype == 'uint8':
      self.image = cut_and_resize_image(self.image)
      cv2.imwrite(self.dist_path, self.image)
      
    else:
      print("Weird datatype: " + self.dtype)

def cut_and_resize_image(image, SIZE=512):
  max_x = 0
  max_y = 0
  img = image.tolist()
  cut_threshold = int(0.20 * image.shape[1])

  for i in range(image.shape[0]):
    for j in range(image.shape[1]-1, 0, -1):
      if img[i][j] != 0 and j > max_x:
        max_x = j
        break
  
  for i in range(cut_threshold,image.shape[1]):
    for j in range(image.shape[0]-1, 0, -1):
      if img[j][i] != 0 and j > max_y: # j, i ker so koordinate y,x
        max_y = j
        break

  size = (SIZE,SIZE) if SIZE else (image.shape[1], image.shape[0])
  squared_image = cv2.resize(image[0:max_y,0:max_x], size)

  return squared_image

def is_grayscale(image):
  return image.ndim == 2






