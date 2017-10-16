import subprocess
import threading

address = "www.google.com"

def worker(count):
    print count
    res = subprocess.call(['ping', '-s', '2','-q', address],stdout=subprocess.PIPE)
    return


threads = list()
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()


