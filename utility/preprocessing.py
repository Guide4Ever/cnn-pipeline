import os

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
  
  def process_image(self):
    if self.dtype == 'uint8':
      # TO-DO
      pass
    elif self.dtype == 'uint16':
      # TO-DO
      pass
    else:
      print("Weird datatype: " + self.dtype)
