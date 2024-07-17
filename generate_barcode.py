# pip install python-barcode

import barcode 
from barcode.writer import ImageWriter

# Prompt the user to enter a number to generate a barcode
number = input("Enter the code to generate barcode : ")

# Get the barcode class for the 'upc' format (Universal Product Code)
barcode_format = barcode.get_barcode_class('upc')

# Create a barcode object using the provided number and the ImageWriter for saving as an image
my_barcode = barcode_format(number, writer=ImageWriter())
my_barcode.save("generated_barcode")

from PIL import Image

Image.open('generated_barcode.png')

