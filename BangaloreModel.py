# Import Libraries
import numpy as np
import pandas as pd
import joblib
import json

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

availability_values = None
area_values = None
location_values = None
model = None

def load_saved_attributes():

    global availability_values
    global location_values
    global area_values
    global model

    with open("columns.json", "r") as f:
        resp = json.load(f)
        availability_values = resp["availability_columns"]
        area_values = resp["area_columns"]
        location_values = resp["location_columns"]

    model = joblib.load(open("bangalore_house_price_prediction_rfr_model.pkl", "rb"))

# load data
df = pd.read_csv("data/ohe_data_reduce_cat_class.csv")

# Split data
X = df.drop('price', axis=1)
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=51)

# feature scaling
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)


# Load Model

model = joblib.load('bangalore_house_price_prediction_rfr_model.pkl')

def get_location_names():
    #if location_values == None:
    #  load_saved_attributes()
    return location_values

def get_availability_values():
    #if availability_values == None:
    #  load_saved_attributes()
    return availability_values

def get_area_values():
    #if area_values == None:
    #   load_saved_attributes()
    return area_values

# it help to get predicted value of house  by providing features value
def predict_house_price(bath, balcony, total_sqft_int, bhk, price_per_sqft, area_type, availability, location):

    # create zero numpy array, len = 107 as input value for model
    x = np.zeros(len(X.columns))

    # adding feature's value accorind to their column index
    x[0] = bath
    x[1] = balcony
    x[2] = total_sqft_int
    x[3] = bhk
    x[4] = price_per_sqft

    if "availability" == "Ready To Move":
        x[8] = 1

    if 'area_type'+area_type in X.columns:
        area_type_index = np.where(X.columns == "area_type"+area_type)[0][0]
        x[area_type_index] = 1

    if 'location_'+location in X.columns:
        loc_index = np.where(X.columns == "location_"+location)[0][0]
        x[loc_index] = 1

    # feature scaling
    # give 2d np array for feature scaling and get 1d scaled np array
    x = sc.transform([x])[0]
    # return the predicted value by train XGBoost model
    return model.predict([x])[0]
