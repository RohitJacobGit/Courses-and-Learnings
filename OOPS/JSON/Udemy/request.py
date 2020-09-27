import requests

r = requests.get('http://google.com')
print('Status: ', r.status_code) # 200
print(r.url)
#print(r.text)

file_obj = open('./page.html','w+')
file_obj.write(r.text)

param = {'q':'pizza'}
r1 = requests.get('https://www.bing.com/search', params=param)
print(r1.status_code)
print(r1.url)
file_obj_one = open('./pizza.html','w+')
file_obj_one.write(r1.text)