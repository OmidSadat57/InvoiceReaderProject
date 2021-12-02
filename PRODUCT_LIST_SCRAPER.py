import requests
from bs4 import BeautifulSoup
import pandas

# create list
product_list = list()

# scrape data
for x in range(50):
    url = 'https://www.ebay.de/b/Dekofiguren-skulpturen-statuen/36025/bn_2398593?_pgn=' + str(x + 1)
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'lxml')

    for i in range(50):

        try:
            item = soup.body.find('div', {'class': 'pagecontainer__center PR_right_wrap'}).find('div', id='mainContent').find('section', id='s0-27-9-0-1[0]-0-1').find('ul', {'class': 'b-list__items_nofooter'}).find_all('li')[i].find('div', {'class': 's-item__wrapper clearfix'}).find('div', {'class': 's-item__info clearfix'}).find('a', {'class': 's-item__link'}).find('h3')
            value = item.get_text()
            product_list.append(value)

        except:
            pass

# create DataFrame
product_df = pandas.DataFrame(product_list)

# save DataFrame as csv file
product_df.to_csv('product_decorations.csv', index=False)


