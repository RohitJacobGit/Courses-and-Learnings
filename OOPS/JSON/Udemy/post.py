import requests

url = 'https://www.w3schools.com/python/demopage.php'
my_data = {'somekey': 'somevalue'}

r = requests.post(url, data= my_data)
print(r.status_code)
print(r.text)

f = open('./myfile.html','w+')
f.write(r.text)
