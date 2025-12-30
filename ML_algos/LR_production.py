import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

class LinearRegression(nn.Module):
    def __init__(self, d):
        super().__init__()
        self.linear = nn.Linear(d, 1)

    def forward(self, x):
        return self.linear(x)

def train(
    model,
    dataloader,
    optimizer,
    loss_fn,
    epochs,
    device="cpu"
):
    model.train()   # 🔑 training mode
    
    for epoch in range(epochs):
        epoch_loss = 0.0

        for X, y in dataloader:
            X = X.to(device)
            y = y.to(device)

            optimizer.zero_grad()      # 1️⃣ clear gradients
            
            y_hat = model(X)           # 2️⃣ forward
            loss = loss_fn(y_hat, y)   # 3️⃣ loss
            
            loss.backward()            # 4️⃣ backward (gradients)
            
            optimizer.step()           # 5️⃣ update parameters

            epoch_loss += loss.item()

        print(f"Epoch {epoch+1:4d} | Loss = {epoch_loss / len(dataloader):.6f}")

# ----- create synthetic data -----
torch.manual_seed(42)

n = 2000          # number of samples
d = 3             # EXACTLY three features

# Feature matrix
X = torch.randn(n, d)

# True parameters (unknown to the model)
true_W = torch.tensor([[2.0], [-1.5], [0.7]])   # shape (3, 1)
true_b = 0.5

# Targets with noise
y = X @ true_W + true_b + 0.1 * torch.randn(n, 1)

# ----- dataset & dataloader -----
dataset = TensorDataset(X, y)
dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

# ----- model, loss, optimizer -----
model = LinearRegression(d)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-2)

# ----- train -----
train(
    model=model,
    dataloader=dataloader,
    optimizer=optimizer,
    loss_fn=loss_fn,
    epochs=50
)

# ----- learned parameters -----
W_learned = model.linear.weight.detach().T
b_learned = model.linear.bias.detach()

print("\nTrue W:\n", true_W)
print("Learned W:\n", W_learned)

print("\nTrue b:", true_b)
print("Learned b:", b_learned.item())
