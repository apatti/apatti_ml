import os

with open("../data/spamsubject.csv","a") as out:
    category = "spam"
    for file in os.listdir("../data/spam"):
        with open("../data/spam/"+file) as inputfile:
            content = inputfile.readlines()
            for line in content:
                if line.startswith("Subject:"):
                    line = line.replace(",","")
                    out.write("{0},{1}\n".format(line[8:-1],category))
                
