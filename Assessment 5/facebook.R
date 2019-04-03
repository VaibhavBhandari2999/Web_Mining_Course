#If while running library(igraph), it says igraph not recognized, then execute the next line to install it again. or just tick it in Packages menu. If it's not there in packages menu, install it using the next line .
#install.packages("igraph")
library(igraph)
igraphDat <- read.graph(file = "D:/VIT/Semester 3/Web Mining Lab/Assessment 5/facebook/facebook/0.edges", directed = FALSE)
igraphDat <- simplify(igraphDat, remove.multiple = TRUE, remove.loops = TRUE)
## Give numbers
V(igraphDat)$label <- seq_along(V(igraphDat))
communityEdgeBetwn <- edge.betweenness.community(igraphDat)
(averagePathLength <- average.path.length(igraphDat))
(transitivityDat <- transitivity(igraphDat, type = "localaverage",isolates = "zero"))
set.seed("20140513")
plot(igraphDat, vertex.color = communityEdgeBetwn$membership, vertex.size = log(degree(igraphDat) + 1), mark.groups = by(seq_along(communityEdgeBetwn$membership), communityEdgeBetwn$membership, invisible))
## Annotate
title("Stanford Facebook data", sub = "http://snap.stanford.edu/data/egonets-Facebook.html")
text(x = -1, y = -1,labels = sprintf("Average path length: %.2f\nTransitivity:%.2f", averagePathLength, transitivityDat))
deg2 <- degree(igraphDat, mode="all")
hist(deg2, breaks=1:vcount(first)-1, main="Histogram of node degree")

hist(deg2,
     main="Histogram",
     xlab="Degree of vertices",
     xlim=c(0,100),
     col="darkmagenta",
     freq=TRUE
)

