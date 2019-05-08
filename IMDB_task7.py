from pprint import pprint
from IMDB_task5 import movie_detail
# in this task we are taking a data, how many movies made by the perticuler actore
# analyse of movie Director
def analyse_movies_director():
	movie_data= movie_detail()
	count_directore = {}
	for one_movie_data in movie_data:
		movie_directore= (one_movie_data["Director"])
		for one_movie_directore in movie_directore:
			if one_movie_directore not in count_directore :
				count_directore[one_movie_directore]=1
			else :
				count_directore[one_movie_directore]+=1
	return (count_directore)
pprint (analyse_movies_director())
