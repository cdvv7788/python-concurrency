from wait import slow_process
from multiprocessing import Process

for i in range(0,10):
    print("Calling something that takes time to execute")
    p = Process(target=slow_process)
    p.start()
