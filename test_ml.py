import pytest
# TODO: add necessary import
import os
import pandas as pd
from ml.data import *
from ml.model import (
    compute_model_metrics,
    inference,
    load_model,
    performance_on_categorical_slice,
    save_model,
    train_model,
)
from train_model import cat_features



#project = "Deploying-a-Scalable-ML-Pipeline-with-FastAPI/"
#data_path = os.path.join(project, "data", "census.csv")
#data = pd.read_csv(data_path,delimiter=",")

@pytest.fixture
def data():
    path = "~/Deploying-a-Scalable-ML-Pipeline-with-FastAPI/"
    df_path = os.path.join(path,"data/census.csv")
    df = pd.read_csv(df_path)
    return df

# TODO: implement the first test. Change the function name and input as needed
def test_shape(data: pd.DataFrame):
    """
    # Ensure data is without null values
    """
    assert data.shape == data.dropna().shape
   


# TODO: implement the second test. Change the function name and input as needed
def test_process_data(data: pd.DataFrame):
    """
    # Confirm process_data function performing as intended
    """
    X_train, y_train, encoder, lb = process_data(
        data,
        categorical_features=cat_features,
        label="salary",
        training=True
    )

    assert X_train.shape[0] > 0
    assert y_train.shape[0] > 0

# TODO: implement the third test. Change the function name and input as needed
def pickle_made(data: pd.DataFrame):
    """
    Confirm the pickle files were made 
    """
    project = "~/Deploying-a-Scalable-ML-Pipeline-with-FastAPI/"
    model_pickle = os.path.join(project, "model", "model.pkl")
    
    assert os.path.exists(model_pickle)

