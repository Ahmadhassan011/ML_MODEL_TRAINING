import torch
import torch.nn as nn

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the trained simple regression model.

    Args:
        model (torch.nn.Module): The trained model.
        X_test (torch.Tensor): The testing features.
        y_test (torch.Tensor): The testing target.
    """
    model.eval()
    with torch.no_grad():
        predicted = model(X_test)
        criterion = nn.MSELoss()
        loss = criterion(predicted, y_test)
        print(f"Mean Squared Error on test data: {loss.item():.4f}")
