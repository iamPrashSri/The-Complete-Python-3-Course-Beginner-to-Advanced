# Writing and Reading contents to/from a file

# newfile = open('newfile.txt', 'w+')
#
# string = "This is the file content to be written"
# newfile.write(string)

import simplejson as json
import os

if os.path.isfile('./ages.json') and os.stat('./ages.json').st_size != 0:
    old_file = open('./ages.json')
    data = json.loads(old_file.read())
    print("Current Age is:", data['age'], ' adding a year')
    data['age'] = data['age'] + 1
else:
    old_file = open('./ages.json', 'w')
    data = {'name':'Prashant', 'age':26}
    print('No file found, setting default to ', data['age'])

old_file.seek(0)
old_file.write(json.dumps(data))
