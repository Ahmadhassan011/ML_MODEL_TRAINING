from sklearn.model_selection import train_test_split
import numpy as np
import torch

def preprocess_data(X, y):
    """
    Preprocesses the data by splitting it into training and testing sets and
    converting it to PyTorch tensors.

    Args:
        X (np.ndarray): The features.
        y (np.ndarray): The target.

    Returns:
        tuple: A tuple containing the training and testing data as PyTorch tensors.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    X_train_tensor = torch.from_numpy(X_train.astype(np.float32))
    y_train_tensor = torch.from_numpy(y_train.astype(np.float32))
    X_test_tensor = torch.from_numpy(X_test.astype(np.float32))
    y_test_tensor = torch.from_numpy(y_test.astype(np.float32))

    return X_train_tensor, y_train_tensor, X_test_tensor, y_test_tensor
