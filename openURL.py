from urllib import urlopen

html = urlopen('https://www.qatarliving.com/classifieds/services')
print html.read()