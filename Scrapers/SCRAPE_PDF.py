import requests
from bs4 import BeautifulSoup
import pandas

# term = 'bee'
#
# url = f'https://duckduckgo.com/?q={term}+filetype%3Apdf&t=h_&ia=web'
# page = requests.get(url).content
# soup = BeautifulSoup(page, 'lxml')
#
# item = soup.body.find('div', {'class': 'site-wrapper  js-welcome-wrapper'})#.find('div', {'class': 'web_content_wrapper'}).find('div', {'class': 'cw'}).find('div', id='links_wrapper').find('div', {'class': 'results--main'}).find('div', {'class': 'search-filters-wrap'}).find('div', id='links')
# # value = item.get_href()
# print(item)

# div class=site-wraper  js-welcome-wrapper,
# div id=web_content_wrapper,
# div class=cw,
# div id=links_wrapper,
# div class=results--main,
# div class=search-filters-wrap,
# div id=links,
# div id=r1-0...1...2(counter),
# div class=result_body links_main links_deep,
# h2,
# a class=result_title js-result-title-link

