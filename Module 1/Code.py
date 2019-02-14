#MODULE 1
 #PACKAGES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

 #Python function for sigmoid function
def sigmoid(z):
    		return 1/(1+np.exp(-z))

 #Function for Computing the cost
def computeCost(theta,x,y):
    		theta=np.matrix(theta)
      x=np.matrix(x)
      y=np.matrix(y)
      first=np.multiply(-y,np.log(sigmoid(x*theta.T)))
      second=np.multiply((1-y),np.log(1-sigmoid(x*theta.T)))
      cost=np.sum(first-second)
      cost=cost/(2*len(x))
      return cost

 #Function for Gradient Conversion
c=1 
def gradient(theta,x,y):
      theta=np.matrix(theta)
    	 x=np.matrix(x)
    	 y=np.matrix(y)
    	 error=sigmoid(x*theta.T)-y
    		grad=((x.T*error)/(2*len(x)))
    		grad=grad*c
    		return grad

 #Function for Predicting the input image
def predictall(x,theta):
       x=np.matrix(x)
       theta=np.matrix(theta)
       h=sigmoid(x* theta.T)
       h_argmax=np.argmax(h,axis=1)
       return h_argmax
