''' crop funtion(s)'''
from PIL import Image
# ==============================

def crop_image(image, crop_left=0, crop_top=0, crop_right=0, crop_bottom=0):
    ''' crop an image by a specified amount of pixels'''
    image = image.resize((crop_left, crop_top, crop_right, crop_bottom), Image.ANTIALIAS)
    return
