import urllib
import json
import string
import re
import signal

apikey='65sytfrxwkzsk9kgr7wb2naq'
#register for a rotten tomatoes api account and get a key

#Takes in a name of a movie, returns id the site uses from the api
def get_id(movie):
    movie= string.replace(movie, ' ' ,'+')
    movie_url="http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey="+ apikey +"&q="+movie+"&page_limit=1"
    moviefile=urllib.urlretrieve(movie_url)
    jsonfile=open(moviefile[0])
    return json.load(jsonfile)[u'movies'][0][u'id']

#Takes in a movie, reads reviews from the api and writes them to a text file as 'Reviewer','Review','Movie'
def getreviews(movie):
    movie_id=get_id(movie)
    f = open('myfilee.txt','a')

    for i in range(1,5):
        review_url='http://api.rottentomatoes.com/api/public/v1.0/movies/'+movie_id+'/reviews.json?_prettyprint=true&review_type=all&apikey='+apikey+'&page_limit=50&page='+str(i)
        reviewfile=urllib.urlretrieve(review_url)
        jsonfile=open(reviewfile[0])
        reviews=json.load(jsonfile)[u'reviews']
        
        for i in range(len(reviews)):
            f.write(reviews[i][u'critic']+','+str(int((reviews[i][u'freshness']=='fresh')))+','+movie+'\n')
            #print reviews[i][u'critic']+','+str(int((reviews[i][u'freshness']=='fresh')))+','+movie+'\n'
            #This is a check
    f.close()

   
#Takes in a list of movies and appends the reviews to the file. Also, multi threading is cool. If a particular movie takes too long, the independent timer raises an exception after 5 seconds, and the try/except skips it.
def rev_list(list_of_movies):
    count=1
    err=open('ErrorLog.txt','a')
    mov=open('MovieList.txt','w')
    for movie in list_of_movies:
        print movie,' ',count,' started'  
        count+=1
        def handler(signum,frame):       
           raise Exception("That's taking too long. Skipping it")    

        signal.signal(signal.SIGALRM, handler)

        signal.alarm(5)

        try:
          getreviews(movie)
          mov.write(str(count-1)+','+movie+'\n')
          print movie,' ',count-1, ' done'

        except KeyError:
             print "There was a key error"
             err.write("There was a key error "+movie+'\n')
             count-=1
        except IndexError:
             print "There was an index error"
             err.write("There was a index error "+movie+'\n')
             count-=1
        except Exception, exc:
             print exc
             err.write(str(exc)+' :'+movie+'\n')
             count-=1 
        signal.alarm(0)
          
    err.close()		
    mov.close()
#rev_list(['Toy Story','Independence Day']).
#This is a Check.

#Scrapes list of movies for a given year, from Wikipedia. Pay no attention to the man behind the curtain. (re: \S is any nonspace \s is space)
def movie_list(year):
    movielist_url='http://en.wikipedia.org/wiki/List_of_American_films_of_'+str(year)
    x=urllib.urlopen(movielist_url)
    tex=x.read()
    movielist=re.findall('<td><i><a href=.+title=.+>(\S+)</a></i></td>', tex )
    movielist+=re.findall('<td><i><a href=.+title=.+>(\S+\s+\S)</a></i></td>', tex )
    movielist+=re.findall('<td><i><a href=.+title=.+>(\S+\s\S+\s\S+)</a></i></td>', tex )
    movielist+=re.findall('<td><i><a href=.+title=.+>(\S+\s\S+\s\S+\s\S+)</a></i></td>', tex )
    movielist+=re.findall('<td><i><a href=.+title=.+>(\S+\s\S+\s\S+\s\S+\s\S+)</a></i></td>', tex )
    movielist+=re.findall('<td><i><a href=.+title=.+>(\S+\s\S+\s\S+\s\S+\s\S+\s\S+)</a></i></td>', tex )
    return movielist

#print movie_list(2012)
#This is a check

#rev_list(movie_list(2013))

#Puts together the movies for a bunch of years
def big_movie_list(years):
 	biglist=[]    
	for year in years:
	    biglist+=movie_list(year)
	return biglist
        
movies21cent= big_movie_list(range(2000,2013))
#This is a check

rev_list(movies21cent)


#The wiki page html looks like:
#<td><i><a href="/wiki/After_Earth" title="After Earth">After Earth</a></i></td>

##  url='http://api.rottentomatoes.com/api/public/v1.0/movies/771036677/reviews.json?_prettyprint=true&review_type=all&apikey=65sytfrxwkzsk9kgr7wb2naq'


