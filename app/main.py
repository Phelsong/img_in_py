import os
import src.Classes.src_img as src_img
#==============================
dev_image = "images/python_logo.png" 
path_to_file = os.path.dirname(__file__) + f'../{dev_image}'
w_img = src_img(path_to_file)
#============================================================================

def main(): 
    return w_img.show()
    
if (__name__ == '__main__'):
    main()

