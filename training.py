import torch
import torch.nn as nn
import torch.optim as optim

def train_model(model, X_train, y_train, num_epochs=100, learning_rate=0.01):
    """
    Trains the simple regression model.

    Args:
        model (torch.nn.Module): The model to train.
        X_train (torch.Tensor): The training features.
        y_train (torch.Tensor): The training target.
        num_epochs (int): The number of epochs to train for.
        learning_rate (float): The learning rate for the optimizer.

    Returns:
        torch.nn.Module: The trained model.
    """
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        model.train()

        # Forward pass
        outputs = model(X_train)
        loss = criterion(outputs, y_train)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")

    return model
