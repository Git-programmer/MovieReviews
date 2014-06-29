MovieReviews
============

Movie Recommendations from the Rotten Tomatoes api.

Programs to read data from the rotten tomatoes api, clean it and use it to build a recommender system.

MovieRev.py reads the json files in the api and writes to a text file, the Name of the reveiwer, rating (freshness), name of the movie for 
a list of movies scraped from wikipedia. To run this you need to register for the rotten tomatoes api and get an apikey. Write this into the code at apikey=' '

The R scripts clean the data for the recommender systems to work with. The reshape function changes the columns of the reviews to NameoftheReviewer, ratingofmovie1, ratingofmovie2 ....

nnb is an ipython notebook that finds the nearest neighbour/ person with the nearest taste to you and uses him to recommend movies. This is a stupid algorithm when data is sparse.

Mov_cofi uses a standard collaborative filtering algorithm. (This needs work.)

The rest of the files are test data and sample outputs



