#This r file cleans the reshaped movie data to files Matlab can read for the collabarative 
#filtration algorithm.

x=read.csv('Testreviews.csv')
#x=read.csv('reviewfile.txt')

y<-x[,-1]
# Get rid of the names of reviewers
y[!is.na(y)]<-1
y[is.na(y)]<-0
#Set 1 or 0 by not na or na

names(y)<-c()
# Get rid of movie titles. Stored elsewhere
write.csv(y,'RMatlab.csv',row.names=FALSE,col.names=FALSE)# Write it to a text MATlab can read from
#R(i,j) is wether the ith person watched the jth movie.

z<-x[,-1]
z[is.na(z)]<-0
# Set 'na's to 0 because entries have to be numeric. They won't figure into the calculation
names(z)<-c()

write.csv(z,'YMatlab.csv',row.names=FALSE,col.names=FALSE)
#Y(i,j) is the rating the ith person gave the jth movie
# Don't mind col.names error msg above.