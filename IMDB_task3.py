# in this task we have to set the movie acording to decade means 10 year defrence between years.  
import json
from pprint import pprint
from IMDB_task2 import group_by_year
with open("movie_list.json","r") as file :
	movies = json.load(file)
movies_by_year = group_by_year(movies)
def group_by_decade(movies):
	year = 0
	all_year = []
	movie_detail = []
	# for the taking movie data from json file
	for movie_data in movies :
		if movie_data not in movie_detail:
			movie_detail.append(movie_data)
	# for get year from json file
	for get_year in movie_detail:
		year = (get_year["year"])
		all_year.append(year)
	# for the taking minimum or meximum year from the list
	min1 = min(all_year)
	max1 = max(all_year)
	# for taking min or max decade year
	while True:
		if min1 % 10 != 0 :
			min1 -= 1
		elif max1 % 10 != 0 :
			max1 += 1
		else :
			break
	decade_list = []
	dicade_value = {}
	for decade in range(min1,max1 ,10):
		decade_list.append(decade)
	for decade_data in decade_list :
		list1 = []
		for i in movies_by_year :
			if decade_data < i and decade_data+10 > i :
				list1.append(movies_by_year[i][0])
		dicade_value[decade_data] = list1
	return (dicade_value)
# pprint (group_by_decade(movies))
