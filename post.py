import requests
url = 'http://'+'www.httpbin.org/post'
payload = {'usuario': 'nash', 'password': '123'}

#r = requests.get(url)
#r = requests.get(url, params=payload)
r = requests.post(url, data=payload)
print(r.text)
print(r.status_code)
