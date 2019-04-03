#If while running library(igraph), it says igraph not recognized, then execute the next line to install it again. or just tick it in Packages menu. If it's not there in packages menu, install it using the next line .
install.packages("igraph")
library(igraph)

first <- graph( edges=c("First","Second", "Second","Third","Third","First","Fifth","First"
                        ,"Fourth","Third","Fifth","Fourth"), directed=T) 
first <- first + vertices("Sixth","Seventh")
first <- first + edge("Second", "Fifth", attr=list(length=2.6))
first <- first + edge("Sixth", "Fifth","Seventh","Sixth","Seventh","Fourth",attr=list(length=2.6))
first[]
plot(first, edge.arrow.size=.5, vertex.color="green", vertex.size=15, vertex.frame.color="gray", 
     vertex.label.color="red",vertex.label.dist=2)


print("This is the total degree of all nodes")
degree(first, mode = c("all"),loops = TRUE, normalized = FALSE)
print("This is the Indegree of all nodes")
degree(first, mode = c("in"),loops = TRUE, normalized = FALSE)
print("This is the outdegree of all nodes")
degree(first, mode = c("out"),loops = TRUE, normalized = FALSE)


diameter(first, directed=T, weights=NA)

edge_density(first, loops=F)
ecount(first)/(vcount(first)*(vcount(first)-1)) #for a directed network


closeness(first, mode="all", weights=NA) 
centr_clo(first, mode="all", normalized=T) 

eigen_centrality(first, directed=T, weights=NA)
centr_eigen(first, directed=T, normalized=T)

betweenness(first, directed=T, weights=NA)
edge_betweenness(first, directed=T, weights=NA)

centr_betw(first, directed=T, normalized=T)

