



import numpy as np 

#X - feature matrix 
#y -targest

#theat - coefficients 9Intercepts & weights) 


from sklearn.linear_model import LinearRegression

def fit_linear_regression_sklearn(X, y):
    model = LinearRegression()
    model.fit(X, y)
    
    # Extract coefficients
    intercept = model.intercept_
    coefficients = model.coef_
    
    # Combine into theta format (same as manual version)
    theta = np.array([intercept, *coefficients])
    
    return theta, model

# Example usage:
# theta, model = fit_linear_regression_sklearn(X, y)
# y_pred = model.predict(X)