import requests

params = {'q': 'pizza'}
r = requests.get('http://www.bing.com/search', params = params) #Creating a request
print('Status:', r.status_code)

#print(r.text)
f = open('page.html', 'w+')  # Write HTML text to the file
f.write(r.text)

