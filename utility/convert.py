import cv2
import numpy as np
import pydicom
from pydicom import FileDataset

PNG_FORMAT = '.png'

def bit16_dicom_to_bit16_png(image):
  png_16bit = image.pixel_array.astype(np.uint16)
  png_16bit = cv2.normalize(png_16bit, None, 0, 65535, cv2.NORM_MINMAX, cv2.CV_16UC1)
  return [png_16bit, PNG_FORMAT]

def bit16_to_bit8_png(image):
  png_8bit = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
  return [png_8bit, PNG_FORMAT]