import requests
from bs4 import BeautifulSoup as soup
import pandas as pd


html = requests.get('https://www.tripadvisor.fr/Hotels-g187147-Paris_Ile_de_France-Hotels.html')
pages = soup(html.content,'lxml')


hotel = []
for name in pages.findAll('div',{'class':'listing_title'}):
  hotel.append(name.text.strip())
  
ratings = []
for rating in pages.findAll('a',{'class':'ui_bubble_rating'}):
  ratings.append(rating['alt'])  
  
price = []

for p in pages.findAll('div',{'class':'price-wrap'}):
  price.append(p.text.replace('₹','').strip()) 

reviews = []
for review in pages.findAll('a',{'class':'review_count'}):
  reviews.append(review.text.strip())

d1 = {'Hotel':hotel,'Ratings':ratings,'No_of_Reviews':reviews,'Price':price}
df = pd.DataFrame.from_dict(d1)

print(df)