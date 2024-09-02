import os
import typing as t
import numpy as np
from PIL import Image
import traceback


def image_save(image_object:Image, save_dir_path:str):
    """Save image object that screenshot result.

    Args:
        image_object (Image)
        save_dir_path (str)
    """
    try:
        image_object.save(os.path.join(save_dir_path, "original_image.jpg"))
    except Exception as E:
        print(f"Error occured!:\n{traceback.format_exc()}")

def image_batch_save(image_split_batches:t.List[np.array], save_dir_path:str):
    try:
        print(f"len of image length: {len(image_split_batches)}")
        for i in range(len(image_split_batches)):
            temp_split_file_name = f"chunking_{i}.jpg"
            temp_split_image_object = Image.fromarray(image_split_batches[i])
            temp_split_image_object.save(os.path.join(save_dir_path, temp_split_file_name))
    except Exception as E:
        print(f"Error occured! in {i} step:\n{traceback.format_exc()}")
        