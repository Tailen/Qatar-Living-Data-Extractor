from bs4 import BeautifulSoup
import csv

with open('./Sample_Page_3.html', 'r', encoding='utf-8') as html:
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

    # cards = soup.find_all(class_='b-card b-card-mod-h item card-sticky')
    categories = soup.find_all(class_='b-ad-excerpt b-par-mod-clear b-line-mod-thin--mix-item') # in format of 'Category, Location'
    cards_sticky = soup.find_all(class_='b-card b-card-mod-h item card-sticky')
    cards = soup.find_all(class_='b-card b-card-mod-h item')
    print(len(list(cards_sticky)))
    print(len(list(cards)))
    categoryList = []
    descriptionList = []
    for category in categories:
        categoryList.append(category.get_text())
    for card_sticky in cards_sticky:
        detail = list(card_sticky)[3]
        link = list(detail)[3]
        description = list(link)[0]
        descriptionList.append(description.get_text())
    for card in cards:
        detail = list(card)[3]
        link = list(detail)[3]
        description = list(link)[0]
        descriptionList.append(description.get_text())
    with open('./output_v2_test.csv', 'a', newline='') as csvFile:
        csv_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(max(len(categoryList), len(descriptionList))):
            if (i >= len(categoryList)):
                csv_writer.writerow(['', descriptionList[i]])
            if (i >= len(descriptionList)):
                csv_writer.writerow([categoryList[i], ''])
            else:
                csv_writer.writerow([categoryList[i], descriptionList[i]])
        print('Added {} categories'.format(len(categoryList)))
        print('Added {} descriptions'.format(len(descriptionList)))