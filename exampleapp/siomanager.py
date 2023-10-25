import socketio

sio = socketio.AsyncServer(
    client_manager=socketio.AsyncRedisManager(),
    async_mode="asgi",
    logger=True,
    engineio_logger=True,
    cors_allowed_origins="*",
)
socketio_app = socketio.ASGIApp(socketio_server=sio)


@sio.on("connect")
async def connect(sid, *args, **kwargs):
    # print("Client Connected", sid)
    await sio.enter_room(sid, "room")


# @sio.on("disconnect")
# async def disconnect(sid, *args, **kwargs):
#     print("disconnect ", sid)
#     await sio.leave_room(sid, "room")

