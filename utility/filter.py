import os
import shutil
"""
copy_files_containing_mlo(source_dir, dest_dir, OVERWRITE=False):
  OVERWRITE = if true, then it does not delete the folder but rather goes into it and replaces the already existing file
"""

def copy_files_containing_mlo(source_dir, dest_dir, OVERWRITE_IMAGES=False):

  if OVERWRITE_IMAGES:
    os.mkdir(dest_dir) if not os.path.exists(dest_dir) else None
  else:
    shutil.rmtree(dest_dir, ignore_errors=True) if os.path.exists(dest_dir) else None
    os.mkdir(dest_dir)

  for file_name in os.listdir(source_dir):
    if "ML" in file_name:
      src_file = os.path.join(source_dir, file_name)
      dst_file = os.path.join(dest_dir, file_name)
      shutil.copy2(src_file, dst_file)