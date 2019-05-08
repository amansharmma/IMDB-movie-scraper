# in this task i hed find the lead actore name and find omly 5 co-actors
# and chack which co-actore actore in which time made a movie with lead actore 

from IMDB_task11 import load_movies_data
from pprint import pprint
all_movies_data = (load_movies_data())
def anlyas_actors(actor_data):
	analyas_of_actores = {}
	# for take all movie data of cast and make a key in the value of lead actor id
	for movie_data in actor_data[:4]:
		id_of_movie = (movie_data["cast"][0]["imdb_id"])
		analyas_of_actores[id_of_movie] = {}
		analyas_of_actores[id_of_movie]["name"] = (movie_data["cast"][0]["name"])
		analyas_of_actores[id_of_movie]["frequent_co_actors"] = []
		cast_of_movie = movie_data["cast"][1:6]
		frequent_co_actors = analyas_of_actores[id_of_movie]["frequent_co_actors"]
		for movie in cast_of_movie:
			count = 0
			id_list = []
			id_list.append(id_of_movie)
			id_list.append(movie["imdb_id"])
			for one_actore_data in actor_data:
				equal_cast = one_actore_data["cast"][0:6]
				for one_equal_cast in equal_cast:
					movie_id = one_equal_cast["imdb_id"]
					if movie_id == id_list[0]: 
						for cast_data in equal_cast:
							cast_id = cast_data["imdb_id"]
							if cast_id == id_list[1]:
								count += 1
			final_data = {"imdb_id":movie["imdb_id"],"name":movie["name"],"num_movies":count}
			frequent_co_actors.append(final_data)
	return(analyas_of_actores)
pprint(anlyas_actors(all_movies_data))
