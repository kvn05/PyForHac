# pip install rembg pillow

from rembg import remove 
from PIL import Image

input_path = "F:/PythonGit/PyForHac/inpIMG.jpg"
output_path = "rmbgIMG.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

print('Background removed successfully!')
