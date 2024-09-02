import os
import typing as t
import re
import logging
from fastapi import APIRouter
import traceback

from src.api.models import CrawlingRequest
from src.api.exeptions.custom_exceptions import InputUrlTypeException
from src.crawling.utils.image_scrap.image_scraper import take_screenshot
from src.crawling.utils.image_scrap.image_saver import image_batch_save
from src.crawling.utils.image_scrap.byte_to_image_converter import byte_to_image
from src.crawling.utils.image_processing.image_processor import ImageProcessor
from src.crawling.openai_autocrawling_chain import auto_crawling_chain


router = APIRouter(prefix="/v1")
image_processor = ImageProcessor()

async def task_screenshot_split_save(webpage_url:str, screenshot_save_base_dir:str)->t.Union[str, bool]:
    try:
        screenshot_result = await take_screenshot(webpage_url)
        screenshot_image =  byte_to_image(byte_object=screenshot_result)
        print(screenshot_image)
        screenshot_image_batch = image_processor.image_split(image_object=screenshot_image)
        # generate save dir for temp screenshot image batch
        screenshot_save_dir_path = os.path.join(screenshot_save_base_dir, webpage_url.replace("/", "-"))
        if not os.path.isdir(screenshot_save_dir_path):
            print(f"generating dir: {screenshot_save_dir_path}")
            os.mkdir(screenshot_save_dir_path)
        image_batch_save(image_split_batches=screenshot_image_batch, save_dir_path=screenshot_save_dir_path)
        return screenshot_save_dir_path

    except Exception as E:
        print("===== take screenshot split save error occured ====")
        print(traceback.format_exc())
        print(E)

        return False

def load_batch_image(screenshot_batch_save_path:str)->t.List[bytes]:
    logging.info(screenshot_batch_save_path)
    screenshot_image_paths = [
        os.path.join(screenshot_batch_save_path, image_name) 
        for image_name in os.listdir(screenshot_batch_save_path)
    ]
    screenshot_image_loads = [image_processor.encode_image(path) for path in screenshot_image_paths]
    return screenshot_image_loads

def is_url_checker(input_url:str)->bool:
    """re input url checker

    Args:
        input_url (str): request input url

    Returns:
        bool
    """
    url_regex = re.compile(
        r'^(https?|ftp):\/\/'               # 스킴(scheme): http, https, ftp
        r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,6}' # 도메인 이름 또는 IP 주소
        r'|'
        r'localhost|'                       # 로컬 호스트
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # IPv4 주소
        r'(:\d+)?'                          # 선택적 포트 번호
        r'(\/[-A-Za-z0-9+&@#\/%=~_|]*)*'    # 선택적 경로
        r'(\?[A-Za-z0-9+&@#\/%=~_|]*)?'     # 선택적 쿼리 문자열
        r'(#[-A-Za-z0-9_]*)?$',             # 선택적 프래그먼트
        re.IGNORECASE
    )
    if url_regex.match(input_url):
        return True
    return False

@router.post("/crawling")
async def autocrawling_operation(input: CrawlingRequest):
    screenshot_save_base_dir = "/Users/jeongminju/Documents/GITHUB/autocrawling_agent/screenshots"
    input_dict = input.model_dump()
    if not is_url_checker(input_url=input_dict["webpage_url"]):
        raise InputUrlTypeException(input_url=input_dict["webpage_url"])

    result = await task_screenshot_split_save(
        webpage_url=input_dict["webpage_url"],
        screenshot_save_base_dir=screenshot_save_base_dir
    )
    print(result)
    if not result:
        pass
    
    gen_prompt_input = {
        "question": input_dict["question"],
        "image_url": load_batch_image(screenshot_batch_save_path=result)
    }
    autocrawling_chain_result = auto_crawling_chain.invoke(input=gen_prompt_input)
    print(autocrawling_chain_result)
    


    
