import argparse
from main import main

def run():
    """
    The command-line interface for the machine learning pipeline.
    """
    parser = argparse.ArgumentParser(
        description="Run a simple machine learning pipeline."
    )
    parser.add_argument(
        "--n_samples",
        type=int,
        default=100,
        help="Number of samples to generate.",
    )
    parser.add_argument(
        "--num_epochs",
        type=int,
        default=100,
        help="Number of epochs to train for.",
    )
    parser.add_argument(
        "--learning_rate",
        type=float,
        default=0.01,
        help="Learning rate for the optimizer.",
    )
    args = parser.parse_args()

    main(
        n_samples=args.n_samples,
        num_epochs=args.num_epochs,
        learning_rate=args.learning_rate,
    )

if __name__ == "__main__":
    run()
