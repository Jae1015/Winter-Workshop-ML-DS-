data <- read.csv("@SrBachchan.csv")
a = data$length
b = data$no_hashtags
c = data$no_men
d = data$likes
e = data$retweets
f = data$sentiment_polarity
g = data$time
plot(x=b,y=d, xlab="no_of_hashtags",ylab="num_of_likes",xlim= c(0,5),ylim=c(0,100),main="")
plot(x=c,y=d, xlab="no_men",ylab="likes",xlim= c(0,5),ylim=c(0,100),main="")
plot(x=b,y=e, xlab="no_of_hashtags",ylab="retweets",xlim= c(0,5),ylim=c(0,100),main="")
plot(x=c,y=e, xlab="no_men",ylab="retweets",xlim= c(0,5),ylim=c(0,100),main="")
png(file = "scatterplot.png")
dev.off()
