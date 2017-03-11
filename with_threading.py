from wait import slow_process
import threading

for i in range(0,10):
    print("Calling something that takes time to execute")
    t = threading.Thread(target=slow_process)
    t.start()
