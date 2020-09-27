import requests
import simplejson as json

linkRequest = { 
    "name": "Adheesh Ganaka DDS", 
    "email": "dds_ganaka_adheesh@torp-gibson.com", 
    "gender": "Female"
}

requestHeaders = {
    "Content-type": "application/json"
    #"access-token": '4b1c85d624736c07e787320262bef6fb'
}

r = requests.post("https://gorest.co.in/public-api/users",
                  data=json.dumps(linkRequest),
                  headers=requestHeaders)

print(r.text)
print(r.headers)
print(json.loads(r.text)['code'])
print(json.loads(r.text)['data']['message'])
