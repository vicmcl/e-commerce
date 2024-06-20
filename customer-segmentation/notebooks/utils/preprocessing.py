import numpy as np
import pandas as pd

### Preprocessing functions ###

def customer_aggregation(data):

    # Aggregation by customer
    agg_data = data.groupby("customer_unique_id").agg(
        {
            "order_id": "count",
            "total_payments": "sum",
            "mean_review_score": "mean",
            "time_since_order": "min",
            "delay": "mean",
        }
    )

    # Set column names
    agg_data.columns = [
        "n_orders",
        "total_payments",
        "mean_review_score",
        "time_since_order",
        "mean_delay",
    ]
    return agg_data


def impute_data(data, columns, imputer, set_type = "train"):
    if set_type == "train":
        for col in columns:
            data[col] = imputer.fit_transform(np.array(data[col]).reshape(-1, 1))
    elif set_type == "test":
        for col in columns:
            data[col] = imputer.transform(np.array(data[col]).reshape(-1, 1))
    return data


def convert_to_seconds(data, columns):
    return data[columns].map(lambda cell: cell.total_seconds())


def log_transformation(data, columns):
    return data[columns].map(lambda cell: np.log1p(cell))


def standardize_data(data, columns, scaler):
    for col in columns:
        data[col] = scaler.fit_transform(np.array(data[col]).reshape(-1, 1))
    return data


### Preprocessing pipeline ###

def customer_preprocessing(data, imputer, scaler, set_type = "train"):

    agg_data = customer_aggregation(data)

    # Impute mean value to review score
    agg_data = impute_data(
        data = agg_data,
        columns = ["mean_review_score"],
        imputer = imputer,
        set_type = set_type,
    )

    # Convert datetime to seconds
    agg_data[["time_since_order", "mean_delay"]] = convert_to_seconds(
        data = agg_data, columns = ["time_since_order", "mean_delay"]
    )

    # Log tranformation
    agg_data[["n_orders", "total_payments"]] = log_transformation(
        data = agg_data, columns = ["n_orders", "total_payments"]
    )

    # Standardization
    agg_data = standardize_data(
        data = agg_data,
        columns = [
            "n_orders", "total_payments", "mean_review_score",
            "time_since_order", "mean_delay"
        ],
        scaler = scaler,
    )

    return agg_data