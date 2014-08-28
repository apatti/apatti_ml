from numpy import *
import matplotlib
import matplotlib.pyplot as plt

#Distance = SqRoot(Sum((X-Label)^2))
def classify(input,data,labels,k):
    #converting input array to be matrix of same size as data so that we can use it for subtract
    diffMat = tile(input,(data.shape[0],1)) - data
    sqDiffMat = diffMat**2
    sumSqDiffMat = sum(sqDiffMat,axis=1)
    distances = sumSqDiffMat**0.5
    sortedIndices = distances.argsort() # sort the indexes
    votedLabels={}
    for i in range(k):
        votedLabels[labels[sortedIndices[i]]] = votedLabels.get(labels[sortedIndices[i]],0)+1
    
    return max(votedLabels.iteritems(),key=lambda x:x[1])[0]


def fileToMat(file,labelsPresent):
    labels=None
    fileData = genfromtxt(file,delimiter=',',skip_header=1,dtype="int")
    if labelsPresent:
        labels = fileData[:,0]
        fileData=fileData[:,1:]
    return fileData,labels

def visualize(data,labels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data[:,0],data[:,1],15.0*labels,15.0*labels)
    ax.set_ylabel("Percentage of time spent playing video game")
    ax.set_xlabel("Liters of icecream consumed per week")
    ax.set_title("Scatter Plot")
    #plt.legend(loc='upper center')
    plt.show()

def normalize(data):
    min = data.min(0)
    max = data.max(0)
    range = max-min
    normData = (data-tile(min,(data.shape[0],1)))/tile(range,(data.shape[0],1))
    return normData,range,min

def testClassifier():
    data,labels = fileToMat("data/train.csv",True)
    #normData,ranges,min = normalize(data)
    testPercent=0.1
    #numTestVectors=int(testPercent*normData.shape[0])
    numTestVectors = 3000
    
    for k in range(1):
        errorCount=0.0
        for i in range(numTestVectors):
            classifiedLabel = classify(data[i],data[numTestVectors:9000,],labels[numTestVectors:9000,],77)
        #print r'Test:%d,Actual:%d' %(classifiedLabel,labels[i])
            if(classifiedLabel!=labels[i]):
                errorCount=errorCount+1.0
        print r'K:%d,Error Rate:%f'%(k,((errorCount/float(numTestVectors))*100))

def digitRecognizer():
    trainData,labels = fileToMat("data/train.csv",True)
    testData,trainLabels = fileToMat("data/test.csv",False)
    classifiedResult = zeros((testData.shape[0],2))
    #with open("testResult.csv","w") as outputFile:
    for i in range(testData.shape[0]):
        #classifierResult = classify(testData[i],trainData,labels,3)
            #outputFile.write("%d,%d\n"%(i+1,classifierResult))
        classifiedResult[i,0]=i+1
        classifiedResult[i,1]=classify(testData[i],trainData,labels,3)
        print "%d "%(i+1)
    savetxt("testResult_apatti_3.csv",classifiedResult,delimiter=',',fmt="%d,%d",header='ImageId,Label')

if __name__ == "__main__":
    digitRecognizer()
