import gevent
from gevent import socket
from wait import gevent_slow_process

jobs = [gevent.spawn(gevent_slow_process) for i in range(1,10)]
gevent.joinall(jobs)
