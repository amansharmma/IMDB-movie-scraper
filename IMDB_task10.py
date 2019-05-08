from pprint import pprint
from IMDB_task1 import scrape_top_list
import os,json
movies_list = scrape_top_list()
# in this task we have to make a dictionary which is conten the data of director's languag.
# in how meny language make a movie and how meny time. 
def analyse_language_and_directors(movies_list):
	all_movies_data = []
	final_dic = {}
	# for checking file exist or not
	for movie_data in movies_list :
		ids = (movie_data['urls'][-10:-1])
		exists = os.path.exists("screpingdata/" + str(ids) + ".json")
		cwd = os.getcwd()
		if exists:
			with open(cwd+"/screpingdata/" + str(ids) + ".json","r+") as file :
				data = json.load(file)
				all_movies_data.append(data)
				language_list = []
				director_list = []
				# for taking languages and directorse name 1 time
				for movis in all_movies_data :
					for language in movis["Language"] :
						if language not in language_list :
							language_list.append(language)
					for director in movis["Director"] :
						if director not in director_list :
							director_list.append(director)
	# for make dictionary and count of the movie
	for directors in director_list :
		dic2 = {}
		for language in language_list :
			count = 0
			for movie_data in all_movies_data :
				if directors in movie_data["Director"]:
					if language in movie_data["Language"]:
						count += 1
			if count > 0 :
				dic2[language] = count
		final_dic[directors]=dic2
	return (final_dic)
pprint (analyse_language_and_directors(movies_list))



# =======secound trick=============================

# def analyse_language_and_directors(movies_list):
# 	director = []
# 	p_director = []
# 	language = []
# 	p_language = []
# 	all_data = []
# 	dic = {}
# 	for i in movies_list :
# 		id1 = (i['urls'][-10:-1])
# 		exists = os.path.exists("screpingdata/" + str(id1) + ".json")
# 		cwd = os.getcwd()
# 		if exists:
# 			with open(cwd+"/screpingdata/" + str(id1) + ".json","r+") as file :
# 				data = json.load(file)
# 				all_data.append(data)
# 				language.append(data["Language"])
# 				director.append(data["Director"])
# 				all_data.append(data)
# 	for v in language :
# 		for w in v :
# 			if w not in p_language :
# 				p_language.append(w)
# 	for x in director :
# 		for z in x :
# 			if z not in p_director :
# 				p_director.append(z)
# 	for y in p_director :
# 		dic2 = {}
# 		for l in p_language :
# 			count = 0
# 			for g in all_data :
# 				if y in g["Director"]:
# 					if l in g["Language"]:
# 						count += 1
# 			if count > 0 :
# 				dic2[l] = count
# 		dic[y]=dic2
# 	return (dic)
# pprint (analyse_language_and_directors(movies_list))
