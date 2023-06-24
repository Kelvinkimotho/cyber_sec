import os
#file path to the image
flag_image_file_path='/home/kali/Desktop/flag/flag.png'
#using  'binwalk tool to extract contents hidden in the image'
os.system(f"binwalk -e {flag_image_file_path}")
#
print("************Done!!!!!***********")
