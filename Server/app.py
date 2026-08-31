from fastapi import FastAPI
from Server.votdRouter import router

app = FastAPI()
app.include_router(router)