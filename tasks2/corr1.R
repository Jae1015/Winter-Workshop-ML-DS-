data <- read.csv("@SrBachchan.csv")
a = data$length
b = data$no_hashtags
c = data$no_men
d = data$likes
e = data$retweets
f = data$sentiment_polarity
g = data$time
print(cor(a,b))
print(cor(a,c))
print(cor(a,d))
print(cor(a,e))
print(cor(a,f))
print(cor(a,g))
print(cor(b,c))
print(cor(b,d))
print(cor(b,e))
print(cor(b,f))
print(cor(b,g))
print(cor(c,d))
print(cor(c,e))
print(cor(c,f))
print(cor(c,g))
print(cor(d,e))
print(cor(d,f))
print(cor(d,g))
print(cor(e,f))
print(cor(e,g))
print(cor(f,g))
