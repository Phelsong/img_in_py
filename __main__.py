"""the App Engine"""
import os
from src.classes.src_img import SrcImg

# ================py.sr==============
DEV_IMAGE = "images/python_logo.png"
path_to_file = os.path.dirname(__file__) + f"\\{DEV_IMAGE}"
w_img = SrcImg(path_to_file)
# ============================================================================


def main():
    """the main function"""
    print(w_img.properties)


# !!
if  __name__ == "__main__":
    main()
# !!
