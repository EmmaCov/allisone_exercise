import joblib
import numpy as np
import pandas as pd

from fastapi import FastAPI
from main import DiamondModel, Diamond, DiamondCut, DiamondColor, DiamondClarity, DiamondPolish, DiamondSymmetry, DiamondReport

from sklearn.preprocessing import LabelEncoder

# Create app and model objects
app = FastAPI()
model = DiamondModel()

# Expose the prediction functionality, make a prediction from the passed
# JSON data and return the predicted wine category with the confidence
@app.post("/test")
def index():
    return{'Nothing to see here'}

@app.get("/parameters")
def parameters(carat_weight: float, cut: DiamondCut, color: DiamondColor,
                clarity: DiamondClarity, polish: DiamondPolish,
                symmetry: DiamondSymmetry, report: DiamondReport):

    diamond = Diamond(carat_weight=carat_weight, cut=cut, color=color,
                        clarity=clarity, polish=polish, 
                        symmetry=symmetry, report=report)

    values = list(dict(diamond).values())

    for i in range(1, len(values)):
        values[i] = values[i].value
        enc = LabelEncoder()
        enc.fit(model.df.iloc[:,i])
        values[i] = list(enc.classes_).index(values[i])

    print(values)
    values = np.array(values).reshape((1, -1))
    
    prediction = float(model.predict_diamond(values))

    return {'prediction': prediction}
