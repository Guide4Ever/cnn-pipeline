import cv2
from utility.preprocessing import extract_breast_from_mammogram
from utility.convert import bit16_dicom_to_bit8_png


def main():
  img_8bit = bit16_dicom_to_bit8_png()
  breast_only = extract_breast_from_mammogram(img_8bit)
  cv2.imshow('Breast Only', breast_only)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  return 0

if __name__ == '__main__':
  main()