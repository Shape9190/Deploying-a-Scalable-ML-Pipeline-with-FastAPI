import pytest
# TODO: add necessary import
import os
import pandas as pd
from ml.data import process_data
from ml.model import inference
from train_model import *



#project = "~/Deploying-a-Scalable-ML-Pipeline-with-FastAPI/"
#data_path = os.path.join(project,"data/census.csv")
data = pd.read_csv("../data/census.csv")


# TODO: implement the first test. Change the function name and input as needed
def test_shape():
    """
    # Ensure data is without null values
    """
    assert data.shape == data.dropna().shape
   


# TODO: implement the second test. Change the function name and input as needed
def test_process_data():
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
def test_pickle():
    """
    # Check that model saved to pickle 
    """
    pe = os.path.join(project, "model/encoder.pkl")
    pm = os.path.join(project, "model/model.pkl")
    assert os.path.exists(pe)
    assert os.path.exists(pm)

    pass