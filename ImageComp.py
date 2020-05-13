
from PIL import Image, ImageDraw, ImageFont
import os

print('*** Program Started ***')

image_font_path = 'C:/imageCompression'
image_path_input = 'C:/imageCompression'
image_path_output = 'C:/imageCompression/output'

image_name_input = '/image0.jpg'

im = Image.open(image_path_input + image_name_input)
print('Input file size   : ', im.size )
print('Input file name   : ', image_name_input )
print('Input Image Size  : ', os.path.getsize (image_path_input  + image_name_input))

# image_name_output = '05_compress_image_01_output.png'
image_name_output = 'image0.jpg'

im.save(image_path_output + image_name_output ,optimize=True,quality=50)

print('Output file size  : ', im.size )
print('Output file name  : ', image_name_output)
print('Output Image Size : ', os.path.getsize (image_path_output + image_name_output))

print('*** Program Ended ***')