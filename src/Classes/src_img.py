from PIL import Image


class src_img:
    """
    class for accessing the values and attributes of a src image object.
    --
    Loads an image from a file.
    Returns a dictionary containing the image properties.
    """

    def __init__(self, path_to_file):
        self.img = self.load_image(path_to_file)
        self.properties = self.image_properties(self.img)
        self.show = self.img.show()

    # ==================================
    def load_image(path_to_file):
        with open(path_to_file, "rb") as file:
            image = Image.open(file)
            return image

    # ==================================
    def image_properties(image):
        width, height = image.size
        return {"image": image, "width": width, "height": height}


# =============================================================================
