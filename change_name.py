
import os
import re

file_path = 'F:/사진/동유럽/빈'       # must put your file route
file_names = os.listdir(file_path)     # collect all the names from route

for name in file_names:
    src = os.path.join(file_path, name)                      # src : temporary file name
    ext = src[-4:]                                                   # ext : extension name, if its length is different, you must change the number
    num_for_name = re.findall("\d+", src )                # extracting all the numbers from 
    new_name = "".join(num_for_name)                    # joining char list data to empty list
    new_name = new_name[:8] + '-' + new_name[8:]  # 8 digits for yyyy-mm-dd/ and rest is time
    new_name = new_name + ext                           # put this characters + extension
    new_name = os.path.join(file_path, new_name)    # define new name for each files in folder(in route)
    os.rename(src, new_name)                                # change name 
