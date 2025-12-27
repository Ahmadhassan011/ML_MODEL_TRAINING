from data import get_data
from preprocessing import preprocess_data
from model import SimpleRegressionModel
from training import train_model
from evaluate import evaluate_model
import torch

def main(n_samples=100, num_epochs=100, learning_rate=0.01):
    """
    The main function to run the machine learning pipeline.
    """
    # Get data
    X, y = get_data(n_samples)

    # Preprocess data
    X_train, y_train, X_test, y_test = preprocess_data(X, y)

    # Initialize model
    input_dim = 1
    output_dim = 1
    model = SimpleRegressionModel(input_dim, output_dim)

    # Train model
    trained_model = train_model(model, X_train, y_train, num_epochs, learning_rate)

    # Evaluate model
    evaluate_model(trained_model, X_test, y_test)

    # Save the model
    torch.save(trained_model.state_dict(), "model.pth")
    print("Model saved to model.pth")

if __name__ == "__main__":
    main()
