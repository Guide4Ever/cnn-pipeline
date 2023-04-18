import os
import cv2
from convert import bit16_dicom_to_bit16_png, bit16_to_bit8_png

class Preprocessing:

  def __init__(self, image, src_path, dist_path):
    self.src_path = src_path
    self.dist_path = dist_path
    self.image = image
    self.dtype = self.image.dtype # uint8, uint16
    self.format = self.get_format() # PNG, DICOM,...
  
  def get_format(self):
    return os.path.splitext(self.src_path)[1].upper()[1:]
  
  def process_image(self):
    if self.format == 'DICOM':
      self.image = bit16_dicom_to_bit16_png(self.image) 
      self.image = bit16_to_bit8_png(self.image)
      self.image = extract_breast_from_mammogram(self.image)
      self.image = resize_image(self.image)
      cv2.imwrite(self.dist_path, self.image)

    elif self.dtype == 'uint16':
      self.image = bit16_to_bit8_png(self.image)
      self.image = extract_breast_from_mammogram(self.image)
      self.image = resize_image(self.image)
      cv2.imwrite(self.dist_path, self.image)
    elif self.dtype == 'uint8':
      self.image = extract_breast_from_mammogram(self.image)
      self.image = resize_image(self.image)
      cv2.imwrite(self.dist_path, self.image)
    else:
      print("Weird datatype: " + self.dtype)

def extract_breast_from_mammogram(image):

  # Crop the image to remove any black space on the right side
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
  contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  x, y, w, h = cv2.boundingRect(contours[0])
  image = image[y:y+h, x:x+w]

  # Convert to grayscale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply thresholding to binarize the image
  _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

  # Find contours in the image
  contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Find the contour with the largest area (the breast)
  largest_contour = max(contours, key=cv2.contourArea)

  # Create a mask from the largest contour
  mask = cv2.drawContours(image.copy(), [largest_contour], -1, (255, 255, 255), -1)

  # Apply the mask to the original image to extract the breast
  breast_only = cv2.bitwise_and(image, mask)

  return breast_only

def resize_image(path, SIZE):
  image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
  size = (SIZE,SIZE) if size else (image.shape[1], image.shape[0])
  squared_image = cv2.resize(image[:], size)

  return squared_image







