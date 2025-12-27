import numpy as np

def get_data(n_samples=100):
    """
    Generates synthetic data for a simple linear regression model.

    Args:
        n_samples (int): The number of samples to generate.

    Returns:
        tuple: A tuple containing the features (X) and the target (y).
    """
    X = np.random.rand(n_samples, 1) * 10
    y = 2 * X + 1 + np.random.randn(n_samples, 1) * 2
    return X, y
