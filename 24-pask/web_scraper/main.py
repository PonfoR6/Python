from bs4 import BeautifulSoup
import requests

response = requests.get('https://en.wikipedia.org/wiki/Main_Page')
wiki_page = response.text

soup = BeautifulSoup(wiki_page, 'html.parser')

wiki_projects = soup.select(selector="#sister-projects-list li .extiw")
wiki_projects_normalized = []

for project in wiki_projects:
    wiki_projects_normalized.append(project.getText())

print(wiki_projects_normalized)
