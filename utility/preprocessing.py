import os
import cv2

class Preprocessing:

  def __init__(self, image, file_path):
    self.image = image # image/matrix with 8-bit or 16-bit values
    self.file_path = file_path 
    self.dtype = self.image.dtype # uint8, uint16
    self.format = self.get_format() # PNG, DICOM,...
    self.modified_image = None # preprocessed image/matrix 

  def get_image(self):
    return self.image
  
  def get_modified_image(self):
    return self.modified_image
  
  def get_format(self):
    return os.path.splitext(self.file_path)[1].upper()[1:]
  
  def get_extracted_breast_from_mammogram(self):
    self.modified_image = extract_breast_from_mammogram(self.image)
  
  def process_image(self):
    if self.dtype == 'uint8':
      # TO-DO
      pass
    elif self.dtype == 'uint16':
      # TO-DO
      pass
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





