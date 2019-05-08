# this task for take cast data of the all data of the movie

from bs4 import BeautifulSoup
import requests,json
from pprint import pprint
from IMDB_task1 import scrape_top_list
all_movies_data = scrape_top_list()
for data in all_movies_data[:5] :
	url = data["urls"]
# task13
	def scrape_movie_cast(url):
		movie_url = requests.get(url)
		movie_text = movie_url.text
		soup = (BeautifulSoup(movie_text,"html.parser"))
		article = soup.find('div', attrs ={ "class" : "article" , 'id':'titleCast'})
		see_more = (article.find('div', attrs ={ "class" : "see-more"}))
		cast_url = ( url + (see_more).a["href"])
		cast = requests.get(cast_url)
		cast_soup = (BeautifulSoup(cast.text,"html.parser"))
		fulcredits = cast_soup.find('div', attrs ={ "class" : "header" , 'id':'fullcredits_content'})
		table = fulcredits.find("table",class_= "cast_list")
		tr = (table.find_all("tr"))
		tr.pop(0)
		movie_cast = []
		for one_tr in tr :
			all_movies_cast = {}
			td = one_tr.find_all("td")
			if len(td) > 1:
				table_data = (td[1])
				all_movies_cast["imdb_id"] = ((table_data.a["href"])[6:-1])
				all_movies_cast["name"] = ((table_data.text).strip())
				movie_cast.append(all_movies_cast)
		return (movie_cast)
	# pprint (scrape_movie_cast(url))
