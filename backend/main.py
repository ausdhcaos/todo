from fastapi import FastAPI

from routes import user, todo
import settings

app = FastAPI()

app.include_router(router=user.router)
app.include_router(router=todo.router)


@app.get("/ping", include_in_schema=False)
async def ping() -> str:
    return "Pong " + settings.ENV
