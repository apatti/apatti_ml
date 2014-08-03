import os
                
def writeToFile(category):
    counter=1
    count = 1000
    with open("../data/training"+str(count)+".csv","a") as trainingout:
        with open("../data/testing"+str(count)+".csv","a") as testingout:
            for file in os.listdir("../data/"+category):
                with open("../data/"+category+"/"+file) as inputfile:
                    content = inputfile.readlines();
                    for line in content:
                        if line.startswith("Subject:"):
                            line = line.replace(",","")
                            if counter > count:
                                out = trainingout
                            else:
                                out = testingout
                            out.write("{0},{1}\n".format(line[8:-1],category))
                            counter=counter+1


writeToFile("spam")
writeToFile("easy_ham")
