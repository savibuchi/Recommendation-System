#SVD coding for filling in NA's value
setwd("~/Python Scripts/change")
#SVD part
data1<- read.csv("original.csv",header = FALSE,na.strings=FALSE)
data1[data1 == 0] <- NA
data2<- read.csv("data6n.csv",header = FALSE,na.strings=FALSE)
datar<- (data1-data2) 
datar[is.na(datar)] <- 0

dataSVD <- svd(datar)
plot(dataSVD$d[1:40] * dataSVD$d[1:40], type = 'b')

#from scree plot only 20 components is a good approximation
datalow <- dataSVD$u[,1:20] %*% diag(dataSVD$d[1:20]) %*% t(dataSVD$v[,1:20])
datalast<- data2+datalow

#Sustitute Missing Ratings by Recreated Ratings
datalast2 <- data1
datalast2[is.na(datalast2)] <- datalast[is.na(datalast2)]
datamap<- as.numeric(datalast2)
write.csv(datalast2,"datalast2.csv",row.names=TRUE)

#heatmap for all data visualization
heatmap(datalast2, Rowv = NA, Colv = NA, na.rm = TRUE, scale = "none")
heatmap(datalow, Rowv = NA, Colv = NA, na.rm = TRUE, scale = "none")
heatmap(datar, Rowv = NA, Colv = NA, na.rm = TRUE, scale = "none")