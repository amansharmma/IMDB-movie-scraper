from pprint import pprint
from IMDB_task1 import scrape_top_list
import os,json
# for count the movie genere

# this is for take data from a file of our directory
def load_movies_data():
	movies_list = scrape_top_list()
	all_movies_data = []
	for movie_data in movies_list :
		ids = (movie_data['urls'][-10:-1])
		exists = os.path.exists("screpingdata/" + str(ids) + ".json")
		cwd = os.getcwd()
		if exists:
			with open(cwd+"/screpingdata/" + str(ids) + ".json","r+") as file :
				data = json.load(file)
				all_movies_data.append(data)
	return(all_movies_data)

# all_movies_data = (load_movies_data())

# this is for count the genere of movie 
def analyse_movies_genre(all_movies_data):
	genere_list = []
	for genere_list_data in all_movies_data :
		for get_genere in genere_list_data["Genere"] :
			genere_list.append(get_genere)
	final_dic = {}
	for genere in genere_list :
		if genere not in final_dic :
			final_dic[genere] = 1
		else :
			final_dic[genere] += 1
	return (final_dic)
# pprint(analyse_movies_genre(all_movies_data))
