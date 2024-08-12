from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_openai.chat_models import ChatOpenAI


def autocrawling_invoke(screenshot_image, task:str="", model_name:str="gpt-4o")->str:
    llms = ChatOpenAI(model=model_name)
    autocrawling_prompt_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content="You are scan image for below taskes. Like extract text from webpage image or analysis webpage image, ... etc."),
            AIMessage(content="Yes. I'm image analysis Agent. What is task that i have to do?"),
            HumanMessage(
                content=[
                    {
                        "type": "text",
                        "text": "My firm give to me webpage analysis task: {task}, Here is website screenshot image."
                    }, 
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{screenshot_image}"
                        }
                    }
                ]
            )
        ]
    )
    chain = autocrawling_prompt_template | llms
    invoke_result = chain.invoke(input={"task": task})

    return invoke_result
