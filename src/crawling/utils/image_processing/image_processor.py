import io
import base64
import typing as t
import numpy as np
from PIL import Image


class ImageProcessor:
    def image_load(self, image_path: str)->Image:
        image_object = Image.open(image_path)
        return image_object

    def image_batch_size_set(self, image_width: int, image_height: int, height_threashold: int=1080)->t.Tuple[int, int]:
        """return image split batch size.

        Args:
            image_width (int): original image's width size
            image_height (int): original image's height size
            height_threashold (int, optional): 
                height threashold value. 
                if image_height over than height_threashold*2, 
                set split height size to height_threashold. 
                Defaults to 1080.

        Returns:
            t.Tuple[int, int]: width, height split size.
        """
        image_batch_width = image_width
        if image_height > height_threashold * 2:
            image_batch_height = height_threashold
        else:
            image_batch_height=  image_height

        return image_batch_width, image_batch_height

    def image_split(self, image_object: Image)->t.List[np.array]:
        image_numpy = np.array(image_object)
        print(image_numpy.shape)
        image_height, image_width, _ = image_numpy.shape
        image_batch_width, image_batch_height = self.image_batch_size_set(
            image_width=image_width,
            image_height=image_height
        )
        print(f"batch length size: {image_batch_height}")
        image_split_batches = []

        bat_height_start = 0
        while bat_height_start <= image_height:
            print(f"temp_bat_height_start: {bat_height_start}")
            image_split_batches.append(image_numpy[bat_height_start:bat_height_start+image_batch_height, :, :])
            bat_height_start += image_batch_height

        return image_split_batches
    
    def encode_image(self, image_path:str)->bytes:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.ead()).decode('utf-8')
        