

def linear_regression_sg(X, y, lr = 1e-2, epochs = 2000):

    n, d = X.shape

    W = torch.zeros(d,1,dtype=X.dtype, requires_grad = True)
    b = torch.zeros(1, dtype = X.dtype, requires_grad = True)


    for epoch in range(epochs):
        y_hat = X @ W + b
        loss = ((y_hat - y)**2).mean()
        loss.backward()
        with torch.no_grad():
            W -= lr * W.grad
            b -= lr * b.grad
            W.grad.zero_()
            b.grad.zero_()

    return W.detach(), b.detach()