import requests
from bs4 import BeautifulSoup as soup 
from random import randint
from time import sleep

html = requests.get('https://www.tripadvisor.fr/Hotels-g187147-Paris_Ile_de_France-Hotels.html')

pages1 = soup(html.content,'lxml')


links = []

for review in pages1.findAll('a',{'class':'review_count'}):
  a = review['href']
  a = 'https://www.tripadvisor.fr'+ a
  a = a[:(a.find('Reviews')+7)] + '-or{}' + a[(a.find('Reviews')+7):]
  links.append(a)

L=[]
reviews = []
for link in links:

  headers = {}
  html2 = requests.get(link.format(i for i in range(5,1000,5)),headers=headers)
  sleep(randint(1,5))
  pages2 = soup(html2.content,'lxml')
  for r in pages2.findAll('q'):
    reviews.append(r.span.text.strip())
    L.append(r.span.text.strip())


print(L)


