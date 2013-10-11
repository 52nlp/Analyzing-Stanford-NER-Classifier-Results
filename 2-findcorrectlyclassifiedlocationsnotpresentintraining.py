"""This method allows us to read in the files we generated with identifytruandidentifiedlocations.py, contained
in this GitHub repository, and then parse those files to determine whether and to what extent the Stanford NER
classifier identified locations that were not included in its training data"""

#import required packages
import os
import glob
import csv 

#identify path to the files we generated with identifytruandidentifiedlocations.py, contained
#in this GitHub repository. Please note I resaved those files as csv files to make them easier to parse
#in Python. Their contents have not changed, only the character that seperates the columns within the file
#(which changed from "\t" to ",")

#path to csv with all tokens the classifier identified as locations
pathtoidentified = "C:\\Users\\Douglas\\Desktop\\identified.csv"

#path to csv with all tokens the training texts identified as locations
pathtotruth = "C:\\Users\\Douglas\\Desktop\\truth.csv"

#create name for the output file we'll generate with this script
out = open("surprisingdecisions.tsv", "w")

#open the second csv identified above in readonly mode
opentrue = open(pathtotruth, "r")

#read the contents of this csv
readtrue = opentrue.read()

#convert the read file to a string object
strtrue = str(readtrue)

#split the string on new lines (so that each row, i.e. each token in the file,
#is a unique string in the list object "splittrue")
splittrue = strtrue.split("\n")

#now open the first csv identified above in readonly mode
openidentified = open(pathtoidentified, "r")

#read the opened file
readidentified = openidentified.read()

#convert it to a string
stridentified = str(readidentified)

#make each row a unique string
splitidentified = stridentified.split("\n")

#create an empty list called "locationidentifiedinrun"
locationidentifiedinrun = []

#Step One: Create a list that contains all of the tokens our trained classifier identified as locations

#for each row in our csv of all tokens identified by the classifier as a location
for line in splitidentified:
    
    #split that row by each of its columns
    splitoncomma = line.split(",")
    
    #if the length of this split object is greater than one (i.e. if the token has associated "LOC" or "0" values)
    if len(splitoncomma) > 1:
        
        #and if the value of the filename (which we stored to column 0 when we made our tsv files in
        #identifytrueandidentifiedlocations.py) is equal to "inc1" (that is, if the row we're analyzing comes
        #from the first of ten directories we established)
        if splitoncomma[0] == "inc1":
            
            #add that token (just the word, which is contained in the second column of the tsv, which we
            #identify with splitoncomma[1] because Python starts its counting from 0) to our list
            #locationidentifiedinrun, which we created above. Once we're done iterating over this for loop,
            #this list will contain all of the tokens that our trained classifier identified when it analyzed
            #the first of our ten directories during
            locationidentifiedinrun.append(splitoncomma[1])

#Step Two: Create a list that contains all of the tokens our training files identified as locations

#create a new empty list called true locations
truelocations = []

#for each row in our csv that contains a token that our training texts identify as locations
for trueline in splittrue:
    
    #split that row each time you meet a comma (i.e. make each column in the row a unique string) 
    truesplitoncomma = line.split(",")
    
    #if the length of this split string is greater than one (i.e. if the row contains more than one column,
    #as it ought to)
    if len(truesplitoncomma) > 1:
        
        #if this particular token comes from the file "inc1"
        if truesplitoncomma[0] == "inc1":
            
            #ignore it, because it wasn't included in our training set. (The classifier we ran on the first
            #of our ten directories was trained on directories 2-10.)
            continue
        
        #otherwise, this token was included in our training texts, so let's add the token to our list of
        #tokens we identified as locations
        else:
            truelocations.append(truesplitoncomma[1])

#Step Three: Compare our list of locations identified by the classifier to our list of locations we fed to the
#classifier when we trained it. See if there are any locations the classifier identified that were not part of
#its training data, and if so, write those locations to the output file we identified above (surprisingdecisions.tsv)

#for each token in our list of locations identified by the trained classifier
for location in locationidentifiedinrun:
    
    #if that token is in the list of locations we fed to the classifier
    if location in truelocations:
        
        #do nothing
        pass
    
    #otherwise, we've found a location the trained classifier was able to correctly identify without having
    #encountered before, so let's print that location to the terminal and write it to our output file followed
    #by a new line.
    else:
        print location
        out.write(str(location) + "\n")

