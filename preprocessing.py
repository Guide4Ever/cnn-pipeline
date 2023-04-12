"""
8-bit, 16-bit

"""

class Preprocessing:

  def __init__(self, image):
    self.image = image
    self.dtype = self.identify_datatype() #no self pass??
    self.mod_image = self.modify_image()

  def get_image(self):
    return self.image
  
  def get_modImage(self):
    return 

  def identify_datatype(self):
    return self.image.dtype
  
  def modify_image(self):
    return 0
