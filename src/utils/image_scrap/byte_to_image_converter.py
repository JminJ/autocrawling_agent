import io
from PIL import Image


def byte_to_image(byte_object:bytes):
    image_stream = io.BytesIO(byte_object)
    image = Image.open(image_stream)

    return image