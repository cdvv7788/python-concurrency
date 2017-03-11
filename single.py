from wait import slow_process

for i in range(0,10):
    print("Calling something that takes time to execute")
    slow_process()
