from fastapi import FastAPI

from allisone_exercise.domain.model import DiamondModel
from allisone_exercise.utils.objects.base_object import Diamond
from allisone_exercise.utils.objects.constant import DiamondClarity, DiamondColor, DiamondCut, DiamondPolish, DiamondReport, DiamondSymmetry
from allisone_exercise.domain.preprocess import preprocess

# Create app and model objects
app = FastAPI()
model = DiamondModel()

@app.get("/prediction", tags=["Prediction"])
def prediction(
    carat_weight: float,
    cut: DiamondCut,
    color: DiamondColor,
    clarity: DiamondClarity,
    polish: DiamondPolish,
    symmetry: DiamondSymmetry,
    report: DiamondReport
) -> dict[str, float]:
    """
        Function that predicts the diamond object

        Parameters
        ----------
        carat_weight : float

            The carat weight of the gem

        cut : DiamondCut

            The cut of the gem, values can be be "Signature-Ideal", "Ideal","Very Good", "Good", "Fair"

        color : DiamondColor

            The color of the gem, values dan be "D", "E", "F", "G", "H", "I"

        clarity : DiamondClarity

            The clarity of the gem, values can be "FL", "IF", "VVS1", "VVS2", "VS2", "VS1", "SI1"

        polish : DiamondPolish

            The polish of the gem, values can be "ID", "EX", "VG", "G"

        symmetry : DiamondSymmetry

            The symmetry of the gem, values can be "ID", "EX", "VG", "G"

        report : DiamondReport

            The report of the gem, values can be "AGSL", "GIA"

        
        Returns
        -------
        prediction : float

            The predicted price of the diamond
    """

    # Create Diamond object
    diamond = Diamond(
        carat_weight=carat_weight,
        cut=cut, 
        color=color,
        clarity=clarity,
        polish=polish,
        symmetry=symmetry, 
        report=report
    )

    # Get the values of the diamond object
    values = list(dict(diamond).values())

    # Transform categorical values into numerical ones
    values = preprocess(values)

    # Reshape the value array
    values = values.reshape((1, -1))
    
    # Apply the predict function of the trained model
    prediction = float(model.predict_diamond(values))

    return {'prediction': prediction}


@app.post("/score", tags=['Score'])
def score() -> dict[str, float]:
    """
    Function that computes the score of the model

    Returns
    -------

    score : float

        The score of the model
    """

    score = float(model.score())

    return {'score': score*100}

@app.post("/test", tags=['Test'])
def test() -> str:
    """
    Basic function that tells if the app works fine or not
    """
    return 'Sanity check'