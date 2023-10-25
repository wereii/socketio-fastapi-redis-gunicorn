### Setup

You will need running redis server listening on localhost (or add url of remote one in exampleapp/siomanager.py)

Server:

```sh
pip install -r requirements.txt
# start local redis
./run.sh
```

Client:

```sh
python sio-client.py
```