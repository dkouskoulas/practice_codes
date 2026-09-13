
import numpy as np 

"""
PROBLEM: Implement gradient descent to optimize logistic regression parameters
Given: [x, y, a, b] where x is feature value, y is label, a and b are sigmoid parameters
Task: Use numerical gradients to compute updated parameters after one gradient descent step
Returns: [a_new, b_new] rounded to 3 decimal places
"""

arr = [1, 2, 1, 2] 

def grad_descent(arr):

    x, y, a, b = arr
    delta = 1e-3
    lr = 1.0 

    def sigmoid(a, b):
        return 1.0/(1 + np.exp(-(a*x + b)))
    
    def loss(a, b):
        y_pred = sigmoid(a, b)
        return -(y * np.log(y_pred) + (1-y) * np.log(1 - y_pred))
    
    dL_a = (loss(a+delta, b) - loss(a-delta, b))/(2*delta) 
    dL_b = (loss(a, b+delta) - loss(a, b - delta))/(2*delta)

    a_new = a - lr * dL_a
    b_new = b - lr * dL_b

    return [np.round(a_new,3), np.round(b_new,3)]
