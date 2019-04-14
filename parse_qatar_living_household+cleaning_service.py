import requests
from bs4 import BeautifulSoup
import csv
import re


pageURL = ''
phonePattern = r'\d\d\d\d\d\d\d\d'
for i in range(35):
    # Get URL of page i
    if i == 0:
        pageURL = 'https://www.qatarliving.com/services/cleaning-services'
    else:
        pageURL = 'https://www.qatarliving.com/services/cleaning-services?page={}'.format(i)
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
    cards_sticky = soup.find_all(class_='b-card b-card-mod-h item card-sticky')
    cards = soup.find_all(class_='b-card b-card-mod-h item')
    titles = soup.find_all(class_='b-card--el-description')

    categoryList = []
    titleList = []
    phoneNumberList = []

    for category in categories:
        categoryList.append(category.get_text())

    for title in titles:
        titleText = list(title)[0]
        titleList.append(titleText)
        number = re.search(phonePattern, titleText)
        if number:
            phoneNumberList.append(str(number.group(0)))
        else:
            phoneNumberList.append('')
    # The First three are top bar cells
    phoneNumberList = phoneNumberList[3:]
    titleList = titleList[3:]

    with open('./cleaning_service_out.csv', 'a', newline='') as csvFile:
        csv_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(max(len(categoryList), len(phoneNumberList))):
            # if (i >= len(categoryList)):
            #     csv_writer.writerow(['', phoneNumberList[i]])
            # if (i >= len(phoneNumberList)):
            #     csv_writer.writerow([categoryList[i], ''])
            # else:

            # print(titleList[i])
            try:
                csv_writer.writerow([categoryList[i], titleList[i], phoneNumberList[i]])
            except:
                print('Encoutered Arabic Letter. Skipping the line.')

    print('Added {} categories'.format(len(categoryList)))
    # print('Added {} descriptions'.format(len(descriptionList)))
    print('Added {} titles'.format(len(titleList)))
    print('Added {} phone numbers'.format(len(phoneNumberList)))