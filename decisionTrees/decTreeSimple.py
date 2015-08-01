from sklearn import tree
from numpy import *

def fileToMat(file):
    fileData = genfromtxt(file,dtype="S",delimiter=',')
