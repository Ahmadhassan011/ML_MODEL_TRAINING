# Simple Regression ML Pipeline

[![ci](https://github.com/Ahmadhassan011/ML_MODEL_TRAINING/actions/workflows/main.yml/badge.svg)](https://github.com/Ahmadhassan011/ML_MODEL_TRAINING/actions/workflows/main.yml)

This project implements a basic machine learning pipeline for simple linear regression. It includes modules for synthetic data generation, data preprocessing, model definition, training, evaluation, and a command-line interface.

## Installation

To get started, first install the required Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

You can run the entire machine learning pipeline using the provided command-line interface (`cli.py`) or by executing the `main.py` script directly.

### Using the Command-Line Interface (CLI)

The `cli.py` script allows you to customize the number of samples, training epochs, and learning rate.

```bash
python cli.py --n_samples 1000 --num_epochs 200 --learning_rate 0.001
```

You can view available options with:

```bash
python cli.py --help
```

### Running the Main Script Directly

To run the pipeline with default parameters, execute `main.py`:

```bash
python main.py
```

## Files

-   `requirements.txt`: Lists the Python dependencies required for the project (`numpy`, `scikit-learn`, `torch`).
-   `data.py`: Contains the `get_data` function to generate synthetic data for linear regression.
-   `preprocessing.py`: Includes `preprocess_data` for splitting data into training/testing sets and converting to PyTorch tensors.
-   `model.py`: Defines the `SimpleRegressionModel` using `torch.nn.Module`.
-   `training.py`: Provides the `train_model` function to train the model using MSE loss and SGD optimizer.
-   `evaluate.py`: Contains `evaluate_model` to assess the trained model's performance using Mean Squared Error.
-   `main.py`: Orchestrates the ML pipeline, calling functions from other modules and saving the trained model.
-   `cli.py`: Provides a command-line interface to run the `main.py` with configurable parameters.
