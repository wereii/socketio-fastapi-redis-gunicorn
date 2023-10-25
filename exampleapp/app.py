from fastapi import FastAPI
from exampleapp.siomanager import socketio_app, sio

app = FastAPI()


@app.get("/")
async def root():
    await sio.emit("hello", {"message": "Hello from FastAPI!"}, room="room")
    return {"message": "Hello sent."}


app.mount("/", socketio_app)
