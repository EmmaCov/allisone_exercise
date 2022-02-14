import joblib
import numpy as np
import pandas as pd

from fastapi import FastAPI

import main 
import characteristics as chara
import preprocess as prep

from sklearn.preprocessing import LabelEncoder

# Create app and model objects
app = FastAPI()
model = main.DiamondModel()

@app.post("/test")
def index():
    """
    Basic function that tells if the app works fine or not
    """
    return{'Sanity check'}

@app.get("/prediction")
def prediction(carat_weight: float,
               cut: chara.DiamondCut,
               color: chara.DiamondColor,
               clarity: chara.DiamondClarity,
               polish: chara.DiamondPolish,
               symmetry: chara.DiamondSymmetry,
               report: chara.DiamondReport):
    """
        Function that predicts the diamond object

         Parameters
        ----------
        carat_weight : float
            The carat weight of the gem
        cut : characteristics.DiamondCut
            The cut of the gem
        color : characteristics.DiamondColor
            The color of the gem
        clarity : characteristics.DiamondClarity
            The clarity of the gem
        polish : characteristics.DiamondPolish
            The polish of the gem
        symmetry : characteristics.DiamondSymmetry
            The symmetry of the gem
        report : characteristics.DiamondReport
            The report of the gem

        Attributes
        ----------
        data : numpy narray
            The array of the data
        
        Returns
        -------
        prediction : float
            The predicted price of the diamond
    """
    # Function that predicts the price of a diamond according to its
    # characteristics

    # Create Diamond object
    diamond = main.Diamond(carat_weight=carat_weight,
                            cut=cut, 
                            color=color,
                            clarity=clarity,
                            polish=polish,
                            symmetry=symmetry, 
                            report=report)

    # Get the values of the diamond object
    values = list(dict(diamond).values())

    # Transform categorical values into numerical ones
    values = prep.preprocess(values)

    # Reshape the value array
    values = values.reshape((1, -1))
    
    # Apply the predict function of the trained model
    prediction = float(model.predict_diamond(values))

    return {'prediction': prediction}
