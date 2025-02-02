# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Write a function that takes a single movie and returns True if its IMDB score is above 5.5

#1st task
def one_movie_above_five_dot_five_score(random_movie):
    if random_movie["imdb"] > 5.5:
        return True
    else:
        return False

print("choose numbers from 0 to 14:")
x = int(input())
print(one_movie_above_five_dot_five_score(movies[x]))

#2nd task
def sublist_imdb_above_five_and_five(aboves):
    sublist = []
    for i in aboves:
        if i["imdb"] < 5.5:
            sublist.append(i)
            
    for i in sublist:
        print(i)

sublist_imdb_above_five_and_five(movies)

#3rd task
def category_depended_movies(overall, specified):
    specified_category = []
    for i in overall:
        if i["category"] == specified:
            specified_category.append(i["name"])
    print(specified_category)

print("choose a category of a movie:")
ctgry = input()
category_depended_movies(movies, ctgry)

#4th task
total = len(movies)

def calculating_average(movies, total):
    allsum = 0
    for i in movies:
        allsum += i["imdb"]
    avg = allsum / total
    
    return avg

print(calculating_average(movies, total))

#5th task
def ctg_imdb_avg(all_movies):
    category = input()
    total_of_category = 0
    category_imdb = 0
    for i in all_movies:
        if i["category"] == category:
            total_of_category += 1
            category_imdb += i["imdb"]
    avg_of_ctg = category_imdb / total_of_category
    return avg_of_ctg

print(ctg_imdb_avg(movies))