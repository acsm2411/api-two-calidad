from fastapi import FastAPI, status, Response
import requests
from prometheus_fastapi_instrumentator import Instrumentator
import logging.config
from pydantic import BaseModel

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)

app = FastAPI()

class ResponseData(BaseModel):
    encryptedToken: str = ""
    internalId: str

Instrumentator().instrument(app).expose(app)

@app.get("/authUsers/{internalId}")
def read_root(internalId: str):
    logger.debug("internalId recibido: " + internalId)
    
    url = 'https://63016ffbe71700618a3866e4.mockapi.io/users'
    responseData = ResponseData(internalId= internalId)
    
    requestResult = requests.get(url + "?internalId=" + internalId, timeout=5)
    
    if(len(requestResult.json()) >= 1):
        responseData.encryptedToken = requestResult.json()[0]["encryptedToken"]
        return Response(content= responseData.json())
    else:
        return Response(status_code= status.HTTP_204_NO_CONTENT)
