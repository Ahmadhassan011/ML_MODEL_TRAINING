import torch.nn as nn

class SimpleRegressionModel(nn.Module):
    """
    A simple linear regression model.
    """
    def __init__(self, input_dim, output_dim):
        """
        Initializes the SimpleRegressionModel.

        Args:
            input_dim (int): The dimension of the input.
            output_dim (int): The dimension of the output.
        """
        super(SimpleRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        """
        The forward pass of the model.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The output of the model.
        """
        return self.linear(x)
