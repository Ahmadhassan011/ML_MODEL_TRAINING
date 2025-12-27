# Data Flow

This page describes the data flow within the Simple ML Pipeline.

## Data Flow Diagram

The following diagram illustrates how data flows through the different components of the pipeline.

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant Main
    participant Data
    participant Preprocessing
    participant Model
    participant Training
    participant Evaluate
    participant Predict

    User->>CLI: Run pipeline with parameters
    CLI->>Main: Call main function with arguments
    Main->>Data: Get synthetic data
    Data-->>Main: Return X and y
    Main->>Preprocessing: Split data into train/test sets
    Preprocessing-->>Main: Return X_train, y_train, X_test, y_test
    Main->>Model: Initialize SimpleRegressionModel
    Model-->>Main: Return model
    Main->>Training: Train model
    Training-->>Main: Return trained model
    Main->>Evaluate: Evaluate model
    Evaluate-->>Main: Print evaluation results
    Main->>Predict: (Optional) Make predictions
    Predict-->>Main: Return prediction
```
