from bs4 import BeautifulSoup

with open("index1.html", encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'lxml')

heading = soup.find(name="h1").get_text()
name = soup.find(name='h2', id='name').get_text()
title = soup.find(name='h3', class_='heading').get_text()
print(heading)

all_a_tags = soup.find_all(name='a')
print(all_a_tags)

for tag in all_a_tags:
    print(tag.getText())
    print(tag.get('href'))


company_url = soup.select_one(selector="p a").get('href')
print(company_url)

all_food = soup.find_all(name='li')
for food in all_food:
    print(food.getText())
