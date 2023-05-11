import cv2
import numpy as np
import pydicom
from pydicom import FileDataset

def bit16_dicom_to_bit16_png(image):
  png_16bit = image.pixel_array.astype(np.uint16)
  format = '.png'
  return [png_16bit,format]

def bit16_to_bit8_png(image):
  png_8bit = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
  format = '.png'
  return [png_8bit,format]