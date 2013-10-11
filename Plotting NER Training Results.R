#if necessary, uncomment these lines and install visualizing packages
#install.packages("ggplot2")
#install.packages("plotrix")
#install.packages("latticeExtra")

#set working directory (identify path to csv)
setwd("C:/Text/Professional/Digital Humanities/Programming Languages/R/Plotting NER Results")
#setwd("C:/Users/Douglas/Desktop")

#read in csv, identify the first row as a series of headers. #read.csv automatically converts the csv to a dataframe
readdataframe <- read.csv("DataFromStanfordReduced.csv", sep = ",", header=TRUE)

#to investigate different attributes of readdatagrame:
#typeof(readdataframe) 
#class(readdataframe)
names(readdataframe)

library(lattice)
library(latticeExtra)
barchart(F1 ~ factor(Training.Run), 
         data = readdataframe, 
         origin = 0, 
         groups = Classifier.Class, 
         main = "Default vs. Trained Classifier: F1 Values",
         xlab = "Test Number",
         ylab = "F1 Value",
         #col = c("green", "yellow", "red"), #use this method to change column colors. Note, though, that the autokey won't be accurate if you change colors...
         #auto.key = TRUE, #use this method to stack elements in key
         auto.key = list(columns = 2), #use this method to juxtapose elements in key #columns = number of variables, = number of barplots to make per test
         par.settings = ggplot2like()) #use this method to employ ggplot2 like graphics
         
help(barchart)