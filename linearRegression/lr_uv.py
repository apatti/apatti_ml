import numpy as np
import pylab as pl

#Cost
#J=(1/2)mSum(H-Y)^2
#H=Q0X0+Q1X1
def computecost(X,Y,theta):
    prediction=X.dot(theta)
    #need to flatten the prediction to make it 1 dim, as Y is 1 dim
    error = prediction.flatten()-Y
    sqerror=error**2
    return (1.0/(2*Y.size))*sqerror.sum()


#populate the data.
data = np.loadtxt("data/ex1data1.txt",delimiter=',')

#plot the data using scatterplot
pl.scatter(data[:,0],data[:,1],c='r',marker='o')
pl.title("Profit distribution")
pl.xlabel("Profits in 10,000s")
pl.ylabel("Population in 10,000s")
#pl.show()

##
#constants
##

#alpha - learning rate
alpha = 0.01

#iterations
iterations = 1500

# end of constants

#X & Y values.
X = data[:,0]
Y = data[:,1]

#size of training set.
m = X.size

#adding ones.
intercept = np.ones([m,2])
intercept[:,1]=X

#initial theta value
theta = np.zeros([2,1])
#print computecost(intercept,Y,theta)
    
#iterate
#calculate new theta using GD
#Qj=Qj-alpha*(1/m)Sum((H-Y)*Xj)
#H=X*Q
for index in range(iterations):
    prediction=intercept.dot(theta)
    error = prediction.flatten()-Y
    theta[0,0]=theta[0,0]-alpha*(1.0/m)*(error*intercept[:,0]).sum()
    theta[1,0]=theta[1,0]-alpha*(1.0/m)*(error*intercept[:,1]).sum()

print theta

#prediction equation would be:
#H=theta[0,0]+theta[1,0]*X or theta*X
#plot line
#between x values and predictions.

predictiondata = intercept.dot(theta)
pl.plot(data[:,0],predictiondata)
pl.show()
