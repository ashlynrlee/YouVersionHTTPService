#Server/votdRouter.py

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from datetime import datetime
from typing import Optional

from Server.votdService import votdGet
from Server.errors import InvalidDayError, MissingVersionError, UpstreamError

dayOfYear = datetime.now().timetuple().tm_yday
defaultVersion = 3034 #default version is BSB

router=APIRouter()

@router.get("/votd") #this funtion will run when HTTP GET hits /votd
def votdEndpoint(day: Optional[int] = None, version: Optional[int] = None):
    if day is None:
        day=dayOfYear
    if version is None:
        version = defaultVersion
    try: 
        result = votdGet(day,version)
        return JSONResponse(status_code=200, content=result)
    except InvalidDayError as e:
        return JSONResponse(status_code=400,content={ "error": {"code": "INVALID_DAY","message": str(e)}})
    except UpstreamError as e:
        return JSONResponse(status_code=502, content={"error": {"code": "UPSTREAM_FAILURE", "message": str(e)}})





