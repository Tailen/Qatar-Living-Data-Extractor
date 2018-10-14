from bs4 import BeautifulSoup

with open('./Sample_Page.html', 'r', encoding='utf-8') as html:
    soup = BeautifulSoup(html.read(), 'html.parser')
    print(soup.prettify())