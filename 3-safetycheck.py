"""This simple script allows us to verify that the tokens in the list we generated after running
findcorrectlyclassifiedlocationsnotpresentintraining.py are in fact not included in any of the training texts"""

#import packages
import os
import glob

#identify path to the tsv files generated while testing the trained classifier
path = "C:\\Users\\Douglas\\Desktop\\results\\*"

#create a new output file called "safetycheck.tsv" in write mode
out = open("safetycheck.tsv", "w")

#for each file in the path identified by the path variable
for file in glob.glob(path):
    
    #store the filename in memory
    filename = os.path.basename(file)
    
    #open the file in readonly mode
    openfile = open(file, "r")
    
    #read the file
    readfile = openfile.read()
    
    #convert the file to a string
    strfile = str(readfile)
    
    #split the string each time you come to a new line (i.e. each time you come to a new row)
    splitonnewline = strfile.split("\n")
    
    #for each row in the tsv
    for line in splitonnewline:
        
        #split each time you come to a tab (i.e. each time you come to a column)
        splitontab = line.split("\t")
        
        #if the length of this split row is greater than one
        if len(splitontab) > 1:
            
            #and if the token in the first row is "Shelbyville" (one of the tokens that we believe
            #the classifier correctly identified as a location without having encountered before)
            if splitontab[0] == "Shelbyville":
                
                #write that row to our output file. Thus, our output file will contain all instances of the token Shelbyville
                #in our training texts. If we review this output file and discover that Shelbyville only occurs
                #in our first directory, then the trained Stanford NER classifier has in fact correctly
                #identified a location it hasn't encountered before
                out.write(str(filename) + "\t" + str(splitontab[0] + "\t" + str(splitontab[1]) + "\t" + str(splitontab[2])+ "\n"))
        
        #if the length of the row is not greater than one, do nothing
        else:
            pass