import os
import time
import psutil
print("Time interval in minutes: ")
Time_interval = float(input())*60
f = open("data.txt", 'w')
f.write("CPU(%): RSS(b): VMS(b): fd:\n")
f.close()

while time.time() < time.time() + Time_interval:
    # Начало процесса
    for i in range(0, 4999):
        a = i**i
    # Конец процесса
    CPU = psutil.cpu_percent(interval=None)
    process = psutil.Process(os.getpid())
    fd = process.num_fds()
    print(fd)
    line = [CPU, process.memory_info().rss, process.memory_info().vms, fd]
    repr(line)
    with open("data.txt", 'a') as f:
        f.write(repr(line)+'\n')
        f.close()


