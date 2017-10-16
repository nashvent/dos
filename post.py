import requests
import threading

url = 'http://'+'www.httpbin.org/post'
payload = {'user': 'nash', 'password': '123'}

#r = requests.get(url)
#r = requests.get(url, params=payload)
#r = requests.post(url, data=payload)
#print(r.text)
#print(r.status_code)



"""funcion que realiza el trabajo en el thread"""
def worker(count):
    r = requests.post(url, data=payload)
    print count
    #print(r.text)
    #print(r.status_code)
    return


threads = list()
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
