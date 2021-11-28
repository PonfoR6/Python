# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get('https://www.amazon.com/dp/B081NXV3ZR/ref=sspa_dk_detail_1?pd_rd_i=B081NXV3ZR&pd_rd_w=KAvbT&pf_rd_p=9fd3ea7c-b77c-42ac-b43b-c872d3f37c38&pd_rd_wg=gawkO&pf_rd_r=JE6A2NXNAGSVHGW2Z71P&pd_rd_r=0c68e819-04c5-4989-b274-0dede78bd345&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNUY1RjYwSlQ4TlNEJmVuY3J5cHRlZElkPUExMDIwOTczMUVWMzFQR1ZNU0QxNiZlbmNyeXB0ZWRBZElkPUEwNTgxNDQxV1ZCNTVMTDQ4TVhNJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1')
# amazon_page = response.text
#
# soup = BeautifulSoup(amazon_page, 'html.parser')
#
# heading = soup.find(name="span").get_text()
#
# print(heading)
import matplotlib as matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

no_pages = 2


def get_data(pageNo):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    r = requests.get(
        'https://www.amazon.in/Ikigai-H%C3%A9ctor-Garc%C3%ADa/dp/178633089X/ref=zg_bs_books_2/257-6232615-7666342?_encoding=UTF8&psc=1&refRID=PM5FNT7X39H06A6X9CZ2' + str(pageNo) + '?ie=UTF8&pg=' + str(pageNo),
        headers=headers)
    content = r.content
    soup = BeautifulSoup(content, features='lxml')

    alls = []

    for d in soup.findAll('div', attrs={'class': 'a-section a-spacing-none aok-relative'}):
        # print(d)
        name = d.find('span', attrs={'class': 'zg-text-center-align'})
        n = name.find_all('img', alt=True)
        price = d.find('span', attrs={'class': 'olp-from'})

        all1 = []

        if name is not None:
            # print(n[0]['alt'])
            all1.append(n[0]['alt'])
        else:
            all1.append("unknown-product")
        if price is not None:
            # print(price.text)
            all1.append(price.text)
        else:
            all1.append('0')
        alls.append(all1)
    return alls


results = []
for i in range(1, no_pages + 1):
    results.append(get_data(i))
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results), columns=['Name', 'Price'])
df.to_csv('amazon_products.csv', index=False, encoding='utf-8')

