# this task for 
from IMDB_task11 import load_movies_data
from pprint import pprint
all_movies_data = (load_movies_data())
def movie_count():
	movie_id = []
	for movie in all_movies_data :
		cast = (movie["cast"])
		for cast_data in cast :
			if cast_data["imdb_id"] not in movie_id :
				movie_id.append(cast_data["imdb_id"])
	movie_count_data={}
	for one_movie_id in movie_id :
		count = 0
		for movie in all_movies_data :
			cast = (movie["cast"])
			for cast_data in cast :
				if cast_data["imdb_id"] == one_movie_id :
					count += 1
					if count > 1 :
						movie_count_data[one_movie_id] = {"name":cast_data["name"],"num_movies":count}	
	return (movie_count_data)
pprint(movie_count())
