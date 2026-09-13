import numpy as np 

"""
PROBLEM: Implement gradient descent with k iterations to optimize logistic regression parameters
Given: [x, y, a, b, k] where x is feature value, y is label, a and b are sigmoid parameters, k is iterations
Task: Use numerical gradients to compute updated parameters after k gradient descent steps
Returns: [a_new, b_new] rounded to 3 decimal places after k iterations
"""

arr = [1, 2, 1, 2, 10]  # Added k=10 iterations

def grad_descent_looped(arr):

    x, y, a, b, k = arr

    delta = 1e-3
    lr = 1.0 

    def sigmoid(a, b):
        return 1.0/(1.0 + np.exp(- (a*x - b)))
    
    def loss(a, b):
        y_pred = sigmoid(a,b)
        return -(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))

    # Loop for k iterations
    for i in range(k):
        dL_a = (loss(a + delta, b) - loss(a - delta, b))/(2*delta)
        dL_b = (loss(a, b + delta) - loss(a, b - delta))/(2*delta)

        a = a - lr*dL_a
        b = b - lr*dL_b

    return [np.round(a, 3), np.round(b, 3)]
