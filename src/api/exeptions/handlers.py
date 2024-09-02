from fastapi import Request
from fastapi.responses import JSONResponse
from src.api.exeptions.custom_exceptions import InputUrlTypeException


async def input_url_type_exception_handler(request: Request, exception: InputUrlTypeException):
    return JSONResponse(
        status_code=401,
        content={"message": f"the url that you input to server, is not the http/s url: {exception.input_url}"}
    )