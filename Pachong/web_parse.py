from bs4 import BeautifulSoup

with open('D:\Python_DS\Pachong\Sample1.html', 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    # images = Soup.select('body > div.mainContent > ul > li:nth-of-type(1) > img')
    images = Soup.select('body > div.mainContent > ul > li > img')
    print(images)

'''
body > div.header > img
body > div.mainContent > ul > li:nth-child(1) > img
body > div.mainContent > ul > li:nth-child(2) > img
body > div.mainContent > ul > li:nth-child(3) > img
'''




from bs4 import BeautifulSoup

with open('D:\Python_DS\Pachong\mooc.com', 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    # images = Soup.select('body > div.mainContent > ul > li:nth-of-type(1) > img')
    images = Soup.select('#main > div:nth-child(3) > div > div > div:nth-child(1) > a > div.course-card-top.hashadow > img')
    print(images)
