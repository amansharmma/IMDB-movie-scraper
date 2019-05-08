from pprint import pprint
from IMDB_task4 import scrape_movie_details
import requests
from bs4 import BeautifulSoup
from IMDB_task1 import scrape_top_list
# for taking all 250 movie detail
def movie_detail():
	movie = scrape_top_list()
	movie_list = []
	for url in movie :
		movie_list.append(url["urls"])
	all_movie_detaile = []
	for movie_url in movie_list :
		one_movie_detaile = scrape_movie_details(movie_url)
		all_movie_detaile.append(one_movie_detaile)
	return (all_movie_detaile)
# pprint (movie_detail())
