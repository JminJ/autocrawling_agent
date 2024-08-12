import typing as t
from icecream import ic
from utils.image_processing.image_processor import ImageProcessor

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser


chat_model = ChatOpenAI(model="gpt-4o")

def gen_prompt(param_dict:t.Dict):
    system_message = "You are a helpful assistant that kindly explains images and answers questions provided by the user."

    human_messages = [
        {
            "type" : "text",
            "text" : f"{param_dict['question']}",
        },
        {
            "type" : "image_url",
            "image_url" : {
                "url" : f"{param_dict['image_url']}",
            }
        }
    ]
    return [SystemMessage(content=system_message), HumanMessage(content=human_messages)]

auto_crawling_chain = gen_prompt | chat_model | StrOutputParser()
