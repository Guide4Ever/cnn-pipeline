import cv2
import numpy as np
import pydicom

def dicom_to_png(dicom_file, png_file):
  
  dicom_image = pydicom.dcmread(dicom_file)
  pixel_data = dicom_image.pixel_array.astype(np.uint16)
  pixel_data = cv2.normalize(pixel_data, None, 0, 65535, cv2.NORM_MINMAX)
  cv2.imwrite(png_file, pixel_data)

def convert_16bit_to_8bit_png(input_file, output_file):

  image = cv2.imread(input_file, cv2.IMREAD_UNCHANGED)
  image_8bit = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
  cv2.imwrite(output_file, image_8bit)