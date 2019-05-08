from pprint import pprint
from IMDB_task5 import movie_detail
# in this task we are taking a data, how many movies made same language par bani hei 
# analyse of movie language
def analyse_movies_language():
	movie_data= movie_detail()
	count_of_language = {}
	for one_movie_data in movie_data :
		movie_language= (one_movie_data["Language"])
		for one_movie_language in movie_language:
			if one_movie_language not in count_of_language :
				count_of_language[one_movie_language]=1
			else :
				count_of_language[one_movie_language]+=1
	return (count_of_language)
pprint (analyse_movies_language())
