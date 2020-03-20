from bs4 import BeautifulSoup
import requests

URL = "https://livanova.com"
r = requests.get(URL)
#r.encoding = 'ISO-8859-1'
print((r.content.json()))

'''
page_link = "http://www.kemahjetskirentals.com/"
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

print (page_content.title)

'''