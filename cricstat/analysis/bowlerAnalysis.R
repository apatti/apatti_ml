inputfilename <- "../data/ipl_bowler.csv"

rawData <- read.csv(inputfilename,header = TRUE)

require(ggplot2)
str(rawData)
rawData$innings <- as.factor(rawData$innings)
rawData$over <- as.factor(rawData$over)
rawData$year <- as.factor(rawData$year)
deathOversData <- rawData[rawData$over==17 |rawData$over==18 |rawData$over==19|rawData$over==20,c('matchid','year','innings','bowler','over','runs','wickets') ]
deathOvers2016 <- deathOversData[deathOversData$year==2016,]
deathOvers2015 <- deathOversData[deathOversData$year==2015,]
deathOvers2014 <- deathOversData[deathOversData$year==2014,]
library(data.table)
dt <- data.table(deathOvers2016)
tables()
setkey(dt,bowler,over,innings)
dt[,economy=sum(runs)/3]
dt[,sum(runs),by=list(bowler,over)][order(bowler,-V1)]
temp <- dt[,sum(runs),by=list(bowler,over)][order(over,-V1)]
qplot(data=temp,x=over,y=V1) + facet_wrap("bowler")+geom_bar(stat="identity")
eco_wickets = dt[,list(eco=sum(runs)/.N,Wickets=sum(wickets),.N),by=list(bowler,over)][order(eco,-N)]
qplot(data=eco_wickets,x=over,y=eco)+geom_bar(stat="identity")+facet_wrap("bowler")
overall <- dt[,list(ECO=sum(runs)/.N,wickets=sum(wickets),Num_Overs=.N),by=bowler][order(ECO,-wickets)]
overall$rank <- 1:nrow(overall)
setcolorder(overall,c("rank","bowler","Num_Overs","ECO","wickets"))
library(grid)
library(gridExtra)
dev.off()
grid.newpage()
grid.table(overall[1:20,])
grid.newpage()
grid.table(overall[21:45,])
grid.newpage()
grid.table(overall[46:70,])
filteredData <- overall[Num_Overs>8]
filteredData$rank <- 1:nrow(filteredData)
grid.table(filteredData)

inningsData <- dt[,list(ECO=sum(runs)/.N,wickets=sum(wickets),Num_Overs=.N),by=list(bowler,innings)][order(ECO,-wickets)]
inningsData <- inningsData[Num_Overs>4]
qplot(data=inningsData,x=innings,y=ECO)+geom_bar(stat="identity")+facet_wrap("bowler")+ ggtitle("Death Overs performace per innigs\n(Minimum 5 overs)")

