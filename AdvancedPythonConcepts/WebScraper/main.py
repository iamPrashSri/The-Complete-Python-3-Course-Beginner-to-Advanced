from bs4 import BeautifulSoup
import requests

searchInput = input('Enter search term:')
params = {"q":searchInput}
r = requests.get('https://www.bing.com/search', params=params)

soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find('ol', {'id':'b_results'})
links = results.findAll('li', {'class':'b_algo'})

for item in links:
    item_text = item.find('a').text
    item_href = item.find('a').attrs['href']

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print('Parent:', item.find('a').parent)  # Find Parent element of the item
        print('Summary:', item.find('a').parent.parent.find('p').text) # Using parent property to navigate

        # Get children
        # children = item.children
        # for child in children:
        #     print('CHild:', child)

        # Get next sibling of the element
        child = item.find('h2')
        print('Next Sibling of the H2:', child.next_sibling)

# print(soup.prettify())
