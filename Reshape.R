#Reshapes a long skinny text of reviews into a wide table with movies as columns
#'myfile.txt' is the skinny table. Coulumn names: Name, Freshness, Movie

x<-read.csv('myfile.txt')
names(x)<-c('Name','Freshness','Movie')
y<-reshape(x,direction='wide',timevar='Movie',idvar='Name')
write.table(y,file='reviewfile.txt',sep=',')