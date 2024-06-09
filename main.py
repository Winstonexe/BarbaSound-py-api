from routers.api import router
from uvicorn import run
from fastapi import FastAPI

app = FastAPI()
app.include_router(router=router)


if __name__ == "__main__":
    run("main:app", reload=True)