import numpy as np
from sklearn.preprocessing import LabelEncoder

from allisone_exercise.domain.model import DiamondModel

def preprocess(data: list) -> np.ndarray:
    """
    Function that converts categorical values into numerical ones using
    the LabelEncoder class

    Parameters
    ----------
    data : list
        The data to preprocess

    Returns
    -------
    preprocessed_data : numpy narray of floats
        The preprocessed data
    """

    model = DiamondModel()
    df = model.df
    columns = df.columns

    enc = LabelEncoder()

    preprocessed_data = []

    for i in range(len(data)):
        preprocessed_data.append(data[i])
        if df[columns[i]].dtype == 'object':
            enc.fit(df[columns[i]])
        
            list_of_classes = list(enc.classes_)

            preprocessed_data[i] = list_of_classes.index(data[i])

    preprocessed_data = np.array(preprocessed_data)

    return preprocessed_data



