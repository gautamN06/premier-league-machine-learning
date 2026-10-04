import numpy as np 
import pandas as pd 


def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cost_function(X, y, w, b):
    m = X.shape[0]
    cost_sum = 0 

    for i in range(m):
        z = np.dot(w, X[i]) + b
        g = sigmoid(z)

        cost_sum += -y[i] * np.log(g) - (1 - y[i]) * np.log(1 - g)

    return (1/m) * cost_sum 

def gradient_function(X,y,w,b):
    m = X.shape[0]
    n = X.shape[1]


    grad_w = np.zeros(n)
    grad_b = 0 


    for i in range(m):
        z = np.dot(w, X[i]) + b 
        g = sigmoid(z)

        grad_b += (g - y[i])
        for j in range(n):
            grad_w[j] += (g - y[i]) * X[i,j]

    grad_b = (1/m) * grad_b 
    grad_w = (1/m) * grad_w 

    return grad_b, grad_w 


def gradient_descent(X, y, alpha, num_iterations):
    n = X.shape[1]

    w = np.zeros(n)
    b = 0 

    for i in range(num_iterations):
        grad_b, grad_w = gradient_function(X,y,w,b)

        w = w - alpha * grad_w 
        b = b - alpha * grad_b 

        if i % 1000 == 0: 
            print(f"Iteration {i}: Cost {cost_function(X,y,w,b)}")

    return w,b 


def predict(X,w,b):
    z = np.dot(X,w) + b 
    g = sigmoid(z)

    return (g >= 0.5).astype(int)