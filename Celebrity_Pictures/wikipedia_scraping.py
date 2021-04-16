
from bs4 import BeautifulSoup
import urllib
import regex as re
import requests
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

def scrape_wiki(name):
	""" args:
             str (the title of wiki article or the name of a person )
        returns:
              list
     """

	# Query the wiki page and parse the HTML code
	person_url = []
	urlpage =  'https://en.wikipedia.org/wiki/' + name
	page = requests.get(urlpage).text
	soup1= BeautifulSoup(page)
	birthday = soup1.find("span", {"class": "bday"}).string
	year, month, day = birthday.split('-')
	age= relativedelta(date.today(), date(int(year), int(month), int(day))).years


	soup2 = BeautifulSoup(page, 'html.parser')

	for raw_img in soup2.find_all('img'):
		link = raw_img.get('src')
		if re.search('wikipedia/.*/thumb/', link) and not re.search('.svg', link):
			infos = [name, link, birthday,age]
			break



	return infos



def generate_dataframe(names):

	""" args :
	           list

        returns:
              dataframe

    """
	infos = []
	for name in names:
		info = scrape_wiki(name)
		if info:
			infos.append(info)


	infos = pd.DataFrame(infos, columns=['Name', 'pic_url','Birthday','age'])
	return infos


print(generate_dataframe(["Diego Maradona"]))
