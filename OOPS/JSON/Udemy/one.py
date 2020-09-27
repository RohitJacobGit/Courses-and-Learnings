import simplejson as json
import os

#check if file exists
if os.path.isfile('./ages.json') and os.stat('./ages.json').st_size!=0:
    old_file = open('./ages.json','r+')
    # loading data from json
    data = json.loads(old_file.read())
    print('Current age is: ', data['age'])
    # real time updates
    data['age'] = data['age'] + 1
    print('Updated age: ', data['age'])
else:
    # create a file if not present
    old_file = open('./ages.json','w')
    data = {'name':'john', 'age': 25}
    print('No file found, setthing default age as ', data['age'])

old_file.seek(0)
old_file.write(json.dumps(data))