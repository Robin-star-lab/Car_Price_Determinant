# Taxi Price Prediction with MLflow

This repository contains an end-to-end machine learning application for predicting taxi fares. It utilizes MLflow for experiment tracking, model management, and reproducibility. The training pipeline is designed to be flexible, allowing for dynamic parameter tuning to optimize prediction accuracy.

## Table of Contents

-   Introduction
-   Features
-   Installation
-   Usage
-   Model Details
-   Dynamic Parameter Tuning
-   Dataset
-   MLflow Tracking
-   Evaluation
-   Contributing
-   License
-   Contact

## Introduction

This application aims to provide accurate taxi fare predictions based on various features such as pickup/dropoff locations, passenger count, and time of day. By leveraging machine learning and MLflow, we ensure a robust and reproducible prediction pipeline.

## Features

-   **End-to-End Prediction:** Processes input data and delivers a fare prediction output.
-   **Dynamic Training Parameters:** Allows for flexible model tuning and optimization.
-   **MLflow Integration:** Tracks experiments, logs parameters, metrics, and models.
-   **Data Preprocessing:** Handles missing values, feature engineering (e.g., distance calculation, time-based features), and scaling.
-   **Model Persistence:** Saves trained models with MLflow for future use and deployment.
-   **Comprehensive Evaluation Metrics:** Provides detailed insights into model performance.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/yourusername/taxi-fare-prediction.git](https://www.google.com/search?q=https://www.google.com/search%3Fq%3Dhttps://github.com/yourusername/taxi-fare-prediction.git)
    cd taxi-fare-prediction
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    conda create -n Car_price/
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Start MLflow tracking server (optional but recommended):**

    ```bash
    mlflow ui
    ```

    This will open the MLflow UI in your browser, allowing you to view tracked experiments.

## Usage

1.  **Run the training script (adjust as needed):**

    ```bash
    python app.py
    ```

    This will train the model, log parameters, metrics, and the model to MLflow.

2.  **Run the prediction script (adjust as needed):**

    ```bash
    python predict.py
    ```

3.  **Input taxi trip data as prompted (or through the UI).**

   * **Example Input format:**
     * pickup_longitude: -73.982155
     * pickup_latitude: 40.767937
     * dropoff_longitude: -73.964630
     * dropoff_latitude: 40.765602
     * passenger_count: 1
     * pickup_datetime: 2015-01-07 13:09:03 UTC

4.  **Prediction Output:**
    * Predicted Fare: $8.50 (Example)

## Model Details

-   **Model Architecture:** [All models are highlighted as dictionary and the best model chosen for prediction]
-   **Key Libraries:** scikit-learn, pandas, numpy, MLflow, etc.
-   **Feature Engineering:** All done using columntransformer.

## Dynamic Parameter Tuning

The application allows for dynamic tuning of the following training parameters:

These parameters can be adjusted directly in the `params.yaml` script or through command-line arguments. MLflow will track each experiment with its corresponding parameters.

## Dataset

The model is trained on the [Taxi trip pricing] dataset, which contains  taxi trip records.The training data is stored inside github.From which extracted from.



## MLflow Tracking

-   MLflow is used to track all experiments, including parameters, metrics, and models.
-   Run `mlflow ui` to view the MLflow tracking UI.
-   Models are saved and managed using MLflow's model registry.

## Evaluation

The model's performance is evaluated using the following metrics:

-   **Mean Squared Error (MSE):** [MSE score].
-   **Root Mean Squared Error (RMSE):** [RMSE score].
-   **Mean Absolute Error (MAE):** [MAE score].
-   **R-squared (R2):** [R2 score].

MLflow will log these metrics for each experiment.

## Contributing

Contributions are welcome! Please follow these steps:

1.  The UI is made by a contributor who is in the contributors list.

## License

This project is licensed under the [MIT] License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact:

-   +254-115534038 - [alumarobin@gmail.com]
-   [https://github.com/Robin-star-lab]