import cv2
import os
from utility.preprocessing import Preprocessing
import pydicom


#def filter_images():
#  source_dir = 'data\INbreast_mammograms'
#  dest_dir = 'data\INbreast_mammograms_MLO'
#  copy_files_containing_mlo(source_dir, dest_dir, OVERWRITE_IMAGES=False)
#  pass

#def example_tryout():
#  img_8bit = bit16_dicom_to_bit16_png()
#  breast_only = extract_breast_from_mammogram(img_8bit)
#  cv2.imshow('Breast Only', breast_only)
#  cv2.waitKey(0)
#  cv2.destroyAllWindows()


def main():
  src_dir = 'data\INbreast_mammograms_MLO'
  dst_dir = 'data\INbreast_mammograms_MLO_proc'

  for file_name in os.listdir(src_dir):
    image= pydicom.dcmread(os.path.join(src_dir, file_name))
    obj = Preprocessing(image=image, src_path=os.path.join(src_dir, file_name), dist_path=os.path.join(dst_dir, file_name))
    obj.process_image()
if __name__ == '__main__':
  main()