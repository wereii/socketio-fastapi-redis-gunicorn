import multiprocessing

bind = "0.0.0.0:8000"
#workers = multiprocessing.cpu_count() + 1
workers = 8
worker_class = "uvicorn.workers.UvicornWorker"

# backlog=2048 # default
keepalive = 120

preload_app = True
reuse_port = True

forwarded_allow_ips = "*"
proxy_allow_ips = "*"
