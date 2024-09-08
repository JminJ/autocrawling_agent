import typing as t

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser


chat_model = ChatOpenAI(model="gpt-4o")

def gen_prompt(param_dict:t.Dict):
    system_message = "You are a helpful assistant that kindly explains images and answers questions provided by the user."

    human_messages = [
        {
            "type" : "text",
            "text" : f"{param_dict['question']}\n ##IMPORTANT\n1. results are must following order of screenshot images.\n2. results must have to same content compare to screenshot inner content.",
        }
    ]
    image_url = param_dict["image_url"]
    for url in image_url:
        human_messages.append(
            {
                "type" : "image_url",
                "image_url" : {
                    "url" : f"data:image/jpeg;base64,{url}",
                }
            }
        )
    return [SystemMessage(content=system_message), HumanMessage(content=human_messages)]

auto_crawling_chain = gen_prompt | chat_model | StrOutputParser()
