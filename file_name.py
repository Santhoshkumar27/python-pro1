
import os
  
split_tup = os.path.splitext('myCaptain.py')
print(split_tup)
 
file_name = split_tup[0]
file_extension = split_tup[1]
  
print("File Name: ", file_name)
print("File Extension: ", file_extension)
