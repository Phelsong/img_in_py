import os
import Classes.src_img as src_img
#==============================
path_to_file = os.path.join(os.path.dirname(__file__))
w_img = src_img(path_to_file)
#============================================================================

def main(): 
    return w_img.show()
    
if (__name__ == '__main__'):
    main()

