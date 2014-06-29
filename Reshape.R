#Read in the raw data
X<-read.csv('myfilee.txt')

#Name the columns
names(X)<-c('Name','.','Movie')

#Get rid of people with commas in their names. Messes with the csv format
X<-X[!X$'Movie'=='1',]
X<-X[!X$'Movie'=='0',]
X<-X[!X$'Movie'=='',]

#Turn into a wide table  with columns: Name, rating of movie1, rating movie2,...
Y<-reshape(X,direction='wide',timevar='Movie',idvar='Name')

#Write to a file
write.table(Y,file='reviewfile.txt',sep=',')

#Record movie names
nam<-names(Y)
write.table(nam,file='movienames.txt',row.names=FALSE,col.names=F)
