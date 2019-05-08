from pprint import pprint
import requests
from bs4 import BeautifulSoup
from IMDB_task12 import scrape_movie_cast
movie_url = "https://www.imdb.com/title/tt0066763/"
# also for task task13
# for collect 1 movie detaile
def scrape_movie_details(movie_url):
	movie_data = requests.get(movie_url)
	movie_text = movie_data.text
	soup = BeautifulSoup(movie_text,"html.parser")
	full_detail_of_movie = {}
	full_detail_of_movie["cast"] = scrape_movie_cast(movie_url)
	find_name = soup.find("h1")
	name = (find_name.text[:-8])
	full_detail_of_movie["Name"] = name
	director = soup.find("div",class_="credit_summary_item")
	direct = director.findAll('a')
	director_list=[]
	# for collect director name
	for director_name in direct:
		director_list.append(director_name.text)
	full_detail_of_movie["Director"] = (director_list)
	contry = soup.find('div', attrs ={ "class" : "article" , 'id':'titleDetails'})
	place_of_movie = contry.find_all("div",class_= "txt-block")
	language_list = []
	contry_name = ""
	# for find contry were made this movie and in which language use in this movie
	for place_of_movie_data in place_of_movie :
		h4 = (place_of_movie_data.find('h4'))
		if h4:
			if (h4.text == "Country:") :
				Country = place_of_movie_data.find("a")
				contry_name = (Country.text)
			if (h4.text == "Language:") :
				language = place_of_movie_data.find_all("a")
				for language_data in language :
					language_list.append(language_data.text)
	full_detail_of_movie["Country"] = (contry_name)
	full_detail_of_movie["Language"] = (language_list)
	img_url = soup.find("div",class_="poster").img["src"]
	full_detail_of_movie["Img_url"] = (img_url)
	bio = soup.find("div",class_="summary_text").text
	full_detail_of_movie["bio"] = ((bio).strip())
	time = soup.find("div",class_="title_block")
	find_time = time.find("time")
	time_text = ((find_time.text).strip())
	if len(time_text) == 8 :
		final_time = str((int(time_text[:1]))*60 + int(time_text[3:5])) + (" minute")
		full_detail_of_movie["Time"] = ((final_time).strip())
	elif len(time_text) == 7 :
		final_time = str((int(time_text[:1]))*60 + int(time_text[3])) + (" minute")
		full_detail_of_movie["Time"] = (final_time)
	else :
		final_time = str((int(time_text[0]))*60) + (" minute")
		full_detail_of_movie["Time"] = (final_time)
	genere = soup.find("div",class_="subtext")
	all_genere = genere.find_all("a")
	genere_data = []
	# for taking genere of movie
	for a in range(len(all_genere)-1) :
		genere_data.append((all_genere[a].text))
	full_detail_of_movie["Genere"] = (genere_data)
	return (full_detail_of_movie)
# pprint (scrape_movie_details(movie_url))
