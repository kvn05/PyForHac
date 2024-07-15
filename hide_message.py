#pip install stegano
from stegano import lsb

# hide secret message in image
secret = lsb.hide('image.png', 'Buhh! here is your secret message')

#save image with hidden message
secret.save('secret_img.png')

#reveal hidden secret message in image
print(lsb.reveal('secret_img.png'))

#Output -> Buhh! here is your secret message