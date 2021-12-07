import bs4 as BeautifulSoup
import urllib.request

def scrapper():
    source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
    