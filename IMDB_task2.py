# in this task i sepreted the movie accordintg to year
import json
from pprint import pprint
with open("movie_list.json") as file :
	movies = json.load(file)
def group_by_year(movies):
	movies_data = {}
	# for taking data of the movie
	for data in movies :
		year = data["year"]
		movies_data[year] = []
	# for the chack condition of the year
	for i in movies_data :
		for key in movies :
			var = key["year"]
			if i == var :
				movies_data[i].append(key)
	return (movies_data)
# pprint (group_by_year(movies))
