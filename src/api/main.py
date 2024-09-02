from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv

from src.crawling.openai_autocrawling_chain import auto_crawling_chain
from src.crawling.utils.image_scrap.image_saver import image_batch_save
from src.crawling.utils.image_processing.image_processor import ImageProcessor
from src.api.router.crawling_router import router
from src.api.exeptions.custom_exceptions import InputUrlTypeException
from src.api.exeptions.handlers import input_url_type_exception_handler

load_dotenv(find_dotenv())
image_processor = ImageProcessor()
app = FastAPI()
    
app.add_exception_handler(InputUrlTypeException, input_url_type_exception_handler)
app.include_router(router)