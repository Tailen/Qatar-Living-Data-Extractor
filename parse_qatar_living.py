import requests
from bs4 import BeautifulSoup
import csv



pageURL = ''
for i in range(486):
    # Get URL of page i
    if i == 0:
        pageURL = 'https://www.qatarliving.com/classifieds/services'
    else:
        pageURL = 'https://www.qatarliving.com/classifieds/services?page={}'.format(i)
    # download page
    try:
        htmlFile = requests.get(pageURL)
        print('Downloaded page {}'.format(i))
    except:
        print('Failed to download page {}'.format(i))
    # Parse information and store to CSV file
    soup = BeautifulSoup(htmlFile.content, 'html.parser')
    # print(soup.prettify())
    # cards = soup.find_all(class_='b-card b-card-mod-h item card-sticky')
    categories = soup.find_all(class_='b-ad-excerpt b-par-mod-clear b-line-mod-thin--mix-item') # in format of 'Category, Location'
    cards = soup.find_all(class_='b-card b-card-mod-h item card-sticky')
    categoryList = []
    descriptionList = []
    for category in categories:
        categoryList.append(category.get_text())
    for card in cards:
        detail = list(card)[3]
        link = list(detail)[3]
        description = list(link)[0]
        descriptionList.append(description.get_text())
    with open('./output.csv', 'a', newline='') as csvFile:
        csv_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(max(len(categoryList), len(descriptionList))):
            if (i >= len(categoryList)):
                csv_writer.writerow(['', descriptionList[i]])
            if (i >= len(descriptionList)):
                csv_writer.writerow([categoryList[i], ''])
            else:
                csv_writer.writerow([categoryList[i], descriptionList[i]])
        print('Added {} entries'.format(min(len(categoryList), len(descriptionList))))
