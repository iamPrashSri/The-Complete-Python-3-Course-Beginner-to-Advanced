# Posting data to a Webpage

import requests

mydata = {'name':'Nick', 'email':'prashantsrivastava.masters@gmail.com'}
r = requests.post("https://www.w3schools.com/php/welcome.php", data=mydata)

f = open('postresponse.html', 'w+')
f.write(r.text)