# Welcome to the Simple ML Pipeline

This project provides a basic, end-to-end machine learning pipeline that demonstrates a simple linear regression model. The pipeline is built with Python and utilizes PyTorch for the model creation and training.

## Features

=== "Data Generation"

    The pipeline generates synthetic data for a linear regression task. This allows for quick experimentation and testing without the need for external datasets.

=== "Preprocessing"

    The data is automatically split into training and testing sets, ensuring a proper evaluation of the model.

=== "Model Training"

    A simple linear regression model is trained on the data using PyTorch's `nn.Module`.

=== "Evaluation"

    The trained model is evaluated on the test set to assess its performance.

=== "Prediction"

    The trained model can be used to make predictions on new data points.

## Get Started

To get started with the project, clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
pip install -r requirements.txt
```

Then, run the pipeline using the command-line interface:

```bash
python -m cli --n_samples 1000 --num_epochs 500
```
