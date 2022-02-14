# Importations

import numpy as np
import pandas as pd
from joblib import dump
from pydantic import BaseModel

from enum import Enum

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

class DiamondCut(str, Enum):
    #'Fair', 'Good', 'Very Good', 'Ideal', 'Signature Ideal'
    signature_ideal = "Signature-Ideal"
    ideal = "Ideal"
    very_good = "Very Good"
    good = "Good"
    fair = "Fair"

class DiamondColor(str, Enum):
    #'D' 'E' 'F' 'G' 'H' 'I'
    d = "D"
    e = "E"
    f = "F"
    g = "G"
    h = "H"
    i = "I"

class DiamondClarity(str, Enum):
    #'SI1', 'VS1', 'VS2', 'VVS2', 'VVS1', 'IF', 'FL'
    flawless = "FL"
    int_flawless = "IF"
    vvs1 = "VVS1"
    vvs2 = "VVS2"
    vs2 = "VS2"
    vs1 = "VS1"
    si1 = "SI1"

class DiamondPolish(str, Enum):
    #'EX' 'G' 'ID' 'VG'
    ideal = "ID"
    excellent = "EX"
    very_good = "VG"
    good = "G"


class DiamondSymmetry(str, Enum):
    #'EX' 'G' 'ID' 'VG'
    ideal = "ID"
    excellent = "EX"
    very_good = "VG"
    good = "G"
    

class DiamondReport(str, Enum):
    #'AGSL' 'GIA'
    agsl = "AGSL"
    gia = "GIA"


# Class which describes a diamond
class Diamond(BaseModel):
    carat_weight: float
    cut: DiamondCut
    color: DiamondColor
    clarity: DiamondClarity
    polish: DiamondPolish
    symmetry: DiamondSymmetry
    report: DiamondReport

# Class for training the model and making predictions
class DiamondModel:
    # Class constructor, loads the dataset and loads the model
    # if exists. If not, calls the _train_model method and
    # saves the model
    def __init__(self):
        self.df = pd.read_csv('data/diamond.csv')
        self.model_fname_ = 'diamond_price.pkl'
        
        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            dump(self.model, self.model_fname_)

    def _preprocessing(self, X):
        enc = LabelEncoder()

        for col in X.columns:
            if X[col].dtype == 'object':
                X[col] = enc.fit_transform(X[col])

        return X

    # Perform model training using the RandomForest regressor
    def _train_model(self):
        X = self.df.drop(['Price'], axis=1)
        y = self.df['Price']

        X = self._preprocessing(X)
        rfc = RandomForestRegressor()
        model = rfc.fit(X, y)
        return model

    # Make a prediction based on the user-entered data
    # Returns the predicted diamond 
    def predict_diamond(self, data):
        prediction = self.model.predict(data)
        return prediction
