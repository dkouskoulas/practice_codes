import torch
from sklearn.metrics import r2_score

# Basic Linear Regression in PyTroch (manual W/b + autograd)
# Time Complexity: O(epochs * n) for 1D data (each epoch is a full pass)
# Space Complexity: O(n) for storing data + O(1) model params(W,b)

import matplotlib.pyplot as plt

def linear_regression_sgd(X, y, lr = 1e-2, epochs=2000):

    #think auto data in table... n-rows, d-columns

    n, d = X.shape
    
    #weight vector (1 per feature)
    W = torch.zeros(d, 1, dtype=X.dtype, requires_grad=True)

    #offset
    b = torch.zeros(1, dtype = X.dtype, requires_grad=True)

    for epoch in range(epochs):

        #forward 
        y_hat = X @ W + b
        loss = ((y_hat - y)**2).mean()

        loss.backward()

        with torch.no_grad():
            W -= lr * W.grad
            b -= lr * b.grad

            W.grad.zero_()
            b.grad.zero_()

        
        if (epoch + 1) % 500 == 0:
            print(f"epoch ={epoch+1} loss = {loss.item():.4f}")

    return W.detach(), b.detach()



if __name__ == "__main__":
    torch.manual_seed(0)

    # Toy data: y = 2*x1 + 5*x2 + 1 + noise
    n = 200
    X = torch.rand(n, 2) * 10.0  # n rows, 2 features
    y = 2.0 * X[:, [0]] + 5.0 * X[:, [1]] + 1.0 + torch.randn(n, 1) * 0.5

    W, b = linear_regression_sgd(X, y, lr=1e-3, epochs=3000)
    print(f"Learned coefficients: {W.view(-1).tolist()}")
    print(f"Intercept: {b.item():.3f}")

    # Predict on training data for diagnostics
    y_train_pred = X @ W + b

    # Predict for new data points
    X_new = torch.tensor([[0.0, 0.0], [1.0, 2.0], [5.0, 10.0]])
    y_pred = X_new @ W + b
    print("Preds:", y_pred.view(-1).tolist())

    # Plot predicted vs actual for training data
    plt.scatter(y.numpy(), y_train_pred.detach().numpy())
    plt.xlabel("Actual y")
    plt.ylabel("Predicted y")
    plt.title("Predicted vs Actual")
    plt.show()

    # Calculate residuals
    residuals = y - y_train_pred

    # Plot residuals vs predicted values
    plt.scatter(y_train_pred.detach().numpy(), residuals.detach().numpy(), c='orange')
    plt.axhline(0, color='black', linestyle='--')
    plt.xlabel("Predicted y")
    plt.ylabel("Residual (Actual - Predicted)")
    plt.title("Residuals vs Predicted")
    plt.show()

    import numpy as np
    from scipy.stats import shapiro

    # 1. Standard deviation of residuals
    resid_std = np.std(residuals.detach().numpy())
    print("Residual Std Dev:", resid_std)

    # 2. Mean of residuals
    resid_mean = np.mean(residuals.detach().numpy())
    print("Residual Mean:", resid_mean)

    # 3. Shapiro-Wilk normality test
    stat, p = shapiro(residuals.detach().numpy())
    print("Shapiro-Wilk p-value:", p)
    # p > 0.05 suggests residuals are normally distributed

    # 4. R^2 Score
    r2 = r2_score(y.numpy(), y_train_pred.detach().numpy())
    print("R^2 Score:", r2)