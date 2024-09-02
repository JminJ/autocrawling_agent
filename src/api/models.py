from pydantic import BaseModel


class CrawlingRequest(BaseModel):
    question: str
    webpage_url: str

class CrawlingResponse(BaseModel):
    pass