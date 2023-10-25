import asyncio

import socketio

import logging

logging.basicConfig(level=logging.DEBUG)

sio = socketio.AsyncClient(logger=True, engineio_logger=True)


@sio.on("connect")
async def connect(*args, **kwargs):
    print("Connected!", args, kwargs)
    # await emit_events()


@sio.on("connect_error")
async def connect_error(*args, **kwargs):
    print("The connection failed!", args, kwargs)


@sio.on("disconnect")
async def disconnect(*args, **kwargs):
    print("I'm disconnected!", args, kwargs)


@sio.on("*")
async def on_any_event(event, data):
    print(f"{sio.sid} - UNHANDLED EVENT", event, data)


@sio.on("hello")
async def on_hello_event(data):
    print(f"{sio.sid} - HELLO EVENT", data)


# async def emit_events():
#     await sio.emit(
#         "subscribe_room",
#         {"room": "1"},
#         callback=lambda *x: print("sub_room cb:", x),
#     )


async def main():
    await sio.connect("http://127.0.0.1:8000")
    try:
        await sio.wait()
    except asyncio.CancelledError:
        pass


if __name__ == "__main__":
    asyncio.run(main())
