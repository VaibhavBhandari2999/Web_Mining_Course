##Caterogical Data only:
## install mlbench
library(e1071)
library(mlbench)
data("HouseVotes84")
data(HouseVotes84,package="mlbech")
model<-naiveBayes(Class~.,data=HouseVotes84)
predict(model,HouseVotes84[1:10,])
predict(model,HouseVotes84[1:10,],type="raw")

pred<-predict()model,HouseVotes84
table(pred,HouseVotes84$class)

##using laplace smoothing

model<-naiveBayes(Class~.,data=HouseVotes84,laplace=3)
pred<-predict(model,HouseVotes84$Class)

##Example of using a Contingency table

data(titanic)
m<-naiveBayes(Survived~.,data=Titanic)
m
predict(m,as.data.frame(Titanic))

##Example with metric predictors:
data(iris)
m<-naiveBayes(Species~.data=iris)

##alternatively
m<-naiveBayes(iris[,-5],iris[,5])
m
table(predict(m,iris),iris[,5])
