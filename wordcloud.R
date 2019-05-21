w1 <- c("말","동안","양반","양반이","댁","말을","그라믄","말이요","양반도","말은","말이","그","말이지","일이","양반을","많은","짓을","자신도","사람","일")
w2<-factor(w1)f1 <-c("45","40","32","25","20","18","17","13","11","11","10","10","9","9","9","9","8","8","8","7","7")
f2<-as.integer(f1)
library(wordcloud)
pal<-brewer.pal(9, "Set1")
n<-2
wordcloud(w2, f2, scale=c(3,1), rot.per=0.25, min.freq=2, random.order=F, random.color=T, colors=pal)
