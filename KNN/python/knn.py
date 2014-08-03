from numpy import *
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    data = array([[1.1,1.1],[1.0,1.1],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return data,labels

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


def fileToMat(file):
    fileData = genfromtxt(file,delimiter='\t',usecols=(0,1,2))
    labels = genfromtxt(file,delimiter='\t',usecols=(-1),dtype=(int))
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
    data,labels = fileToMat("../data/datingTestSet2.txt")
    normData,ranges,min = normalize(data)
    testPercent=0.1
    numTestVectors=int(testPercent*normData.shape[0])
    print numTestVectors
    errorCount=0.0
    for i in range(numTestVectors):
        classifiedLabel = classify(normData[i],normData[numTestVectors:,],labels[numTestVectors:,],10)
        print r'Test:%d,Actual:%d' %(classifiedLabel,labels[i])
        if(classifiedLabel!=labels[i]):
            errorCount=errorCount+1.0
    print r'Error Rate:%f'%((errorCount/float(numTestVectors))*100)

def classifyPerson():
    freqFlyerMiles=float(raw_input("Number of frequent flyer miles earned per year?"))
    percentTimeSpent = float(raw_input("Percent of time spent playing video games?"))
    litersIcecream = float(raw_input("Liters of Ice cream consumed every week?"))
    resultList = ['Not at all','somewhat','very much']
    data,labels = fileToMat("../data/datingTestSet2.txt")
    normData,ranges,min=normalize(data)
    inArray = array([freqFlyerMiles,percentTimeSpent,litersIcecream])
    classifierResult = classify((inArray-min)/ranges,normData,labels,10)
    print "You would like this person: ",resultList[classifierResult-1]
