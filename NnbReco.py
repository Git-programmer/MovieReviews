#This is like Hamming distance. It counts how many movies two people agree on (out of 
#the ones they've both seen)
#Each person is represented by a list of 1,0 or 'na' depending on wether the've liked/disliked/
#not seen the movie
import random

def hamming(p1,p2):
    watched=0
    agreed=0
    if  len(p1)==len(p2):
        for i in range(len(p1)):
            if not p1[i]=='NA' and not p2[i]=='NA':
                watched+=1
                agreed+=(p1[i]==p2[i])
    #print agreed,watched            
    return agreed,watched

#This finds the person who agrees with you the most.
def nneighbour(p1,listofpeople):
    
    max=(0,0)
    maxperson=[]
    for p in listofpeople:
        w=hamming(p1,p)[1]
        m=hamming(p1,p)[0]
        if m>max[0]:
            max=(m,w)            
            maxperson=p
    #print  maxperson, max        
    return maxperson, max        

#This recommends the movie the guy above liked among the movies you haven't seen.
def recomendations(p1,listofpeople,movies):
    rec,nrec,common=[],[],[]
    nnb=nneighbour(p1,listofpeople)[0]
    agreement=(nneighbour(p1,listofpeople)[1][0]*100.0)/nneighbour(p1,listofpeople)[1][1]
    for i in range(len(p1)-1):
        if p1[i]=='NA' and (nnb[i])=='1':
            rec.append(movies[i])
        if p1[i]=='NA' and (nnb[i])=='0':
            nrec.append(movies[i])     
        if not (p1[i])=='NA' and not (nnb[i])=='NA':
            common.append(movies[i])     
             
            
    print "Simon says, watch these:",random.sample(rec,10)
    #print "He says, don't Watch these:",nrec
    print "You and he have seen %d movies in common"%nneighbour(p1,listofpeople)[1][1]
    #print "This is based on these movies you've seen in common:",common
    print "Simon agrees with you %.0f percent of the time" %agreement

#This is a test    
import csv
x=[]
f=open('reviewfile.txt','r')
#f=open('Testreviews.csv','r')
data=csv.reader(f,delimiter=',')
for row in data:
    x.append(row[2:])
    #print row

#The last element of x seems to be the empty list for some reason. Get rid of it
x=x[:-1]

movies=x[0]
data=x[1:-1]
you=x[-1]

#print x[0],x[1]
#recomendations(you, data, movies)
#print len(you)

f.close()
#How sparse is the data?
emptiness=0
totalnum=0
for row in data:
    for entry in row:
        if entry=='NA':
            emptiness+=1
        totalnum+=1
#print "\n %.0f percent of the data is missing"%((float(emptiness)/totalnum)*100)    

#Initialize you to all 'NA's
you=['NA']*len(you)
#print you,len(you)

# A small list of movies that you can rate to get started
nicemovies=[
"..Beautiful",
"..Chocolat",
"..Meet the Parents",
"..What Women Want",
"..The House of Mirth",
"..The Legend of Bagger Vance",
"..Serendipity",
"..The Princess Diaries",
"..The Sweetest Thing",
"..Sweet Home Alabama",
"..Spanglish",
"..The Polar Express",
"..The Perks of Being a Wallflower",
"..What to Expect When You're Expecting"
]

violentmovies=[
"..Gladiator",
"..Memento",
"..Shaft",
"..Snatch",
"..Unbreakable",
"..Mission: Impossible II",
"..Basic",
"..300",
"..Alien vs. Predator",
"..The Final Cut",
"..Killers",
"..Machete",
"..Predators",
"..Battle: Los Angeles",
"..Texas Killing Fields",
"..Battleship",
"..Resident Evil: Retribution",
"..Ghost Rider: Spirit of Vengeance",
]

print 'The movies you liked'
print violentmovies


#Gets the index of the movies in the samplelist above
speciallist=[]
for movie in nicemovies:
    speciallist.append(movies.index(movie))
#print len(speciallist)
#Asks you rate the sample movies
print speciallist

speciallist=[]
for movie in violentmovies:
    speciallist.append(movies.index(movie))
#print len(speciallist)
#Asks you rate the sample movies
print speciallist



for i in speciallist:
    #print movies[i][2:]
    inp='1'
    #raw_input("Do you like this movie?Yes,No,Haven't seen as 1,0 and anything else if you have't seen it ")
    if inp=='1': you[i]='1'
    elif inp=='0': you[i]='0'
    else: you[i]='NA'
 
#print len(you)
#Calls the main function to give you recommendations
recomendations(you, data, movies)
print movies[0]
