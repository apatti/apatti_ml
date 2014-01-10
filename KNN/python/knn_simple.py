from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]]) # this creates a 2D array (Matrix). its ndim =2, shape = (4,2)
	labels = ['A','A','B','B'] #we need label for every item in group.
	return group,labels

def classify0(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0] #get the size of the data
	#inX is one point, make it same as matrix and subtract
	diffMat = tile(inX,(dataSetSize,1)) - dataSet #dataSetSize,1 == 1 need to be changed.
	sqDiffMat = diffMat**2 #get the squares
	#if axis!=1 then it would sum all, we need sum along 1st.
	sumSqDiffMat = sqDiffMat.sum(axis=1)
	sqRootSumSqDiffMat=sumSqDiffMat**0.5
	sortDistIndices = sqRootSumSqDiffMat.argsort()
	votedLabelsCount ={};
	for i in range(k):
		vote = labels[sortDistIndices[i]]
		votedLabelsCount[vote]=votedLabelsCount.get(vote,0)+1 #get the vote, if not there then 0.
	#votedLablesCount has the following: [('A':1),('B':2)]
	sortedVotes = sorted(votedLabelsCount.items(),key=lambda x:x[1],reverse=True) #sort dict by the value (i.e. 2nd item)
	return sortedVotes[0][0]

def file2Matrix(filename,featurecount):
	fh = open(filename)
	number_lines = len(fh.readlines())
	dataMat = zeros((number_lines,featurecount))
	labels =[]
	index=0
	fh = open(filename)
	for line in fh.readlines():
		linesSplit = line.split('\t')
		dataMat[index:]=linesSplit[0:featurecount]
		labels.append(linesSplit[-1])
		index=index+1

	return dataMat,labels


