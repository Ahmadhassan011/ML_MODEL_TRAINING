import torch
from model import SimpleRegressionModel
import numpy as np

def predict(model, data_point):
    """
    Makes a prediction on a new data point.

    Args:
        model (torch.nn.Module): The trained model.
        data_point (np.ndarray): The new data point.

    Returns:
        float: The prediction.
    """
    model.eval()
    with torch.no_grad():
        data_tensor = torch.from_numpy(data_point.astype(np.float32))
        data_tensor = data_tensor.unsqueeze(0) # Add batch dimension
        prediction = model(data_tensor)
        return prediction.item()

def main():
    """
    Loads the model and makes a prediction on a sample data point.
    """
    # Load the trained model
    input_dim = 1
    output_dim = 1
    model = SimpleRegressionModel(input_dim, output_dim)
    model.load_state_dict(torch.load("model.pth"))

    # Create a new data point
    new_data = np.array([5.0])

    # Make a prediction
    prediction = predict(model, new_data)
    print(f"Prediction for input {new_data[0]}: {prediction:.4f}")

if __name__ == "__main__":
    main()
