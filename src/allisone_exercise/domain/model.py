import joblib
import pandas as pd
from joblib import dump

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class DiamondModel:
    """
    Class that preprocesses the data, trains the model
    and makes predictions

    Attributes
    ----------
    df : pandas DataFrame
        The dataframe of the data
    model_fname_ : str
        The name of the model
    model : joblib model
        The trained model
    
    Methods
    -------
    preprocessing(data: narray)
        Preprocesses the categorical data into numerical data

    _train_model()
        Trains the model

    score()
        Computes the score of the model

    predict_diamond(data: narray)
        Predicts the price of a diamond
    """

    def __init__(self):
        # Class constructor, loads the dataset and loads the model
        # if exists. If not, calls the _train_model method and
        # saves the model
        self.df = pd.read_csv('data/diamond.csv')
        self.model_fname_ = 'diamond_price.pkl'
        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            dump(self.model, self.model_fname_)

    def preprocessing(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Method that preprocesses the data

        Attributes
        ----------
        data : numpy narray
            The array of the data
        
        Returns
        -------
        data : numpy narray
            The preprocessed data, where categorical values have been
            converted into numerical ones 
        """

        enc = LabelEncoder()

        for col in data.columns:
            if data[col].dtype == 'object':
                data[col] = enc.fit_transform(data[col])

        return data

    def _train_model(self) -> RandomForestRegressor:
        """
        Method that trains the model
        
        Returns
        -------
        model : RandomForestRegressor model
            The model trained on the preprocessed data 
        """
        
        X = self.df.drop(['Price'], axis=1)
        y = self.df['Price']

        X = self.preprocessing(X)
        rfc = RandomForestRegressor()
        model = rfc.fit(X, y)
        return model

    def score(self) -> float:
        """
        Method that compute the score of the model

        Returns
        -------
        score : float

        The score of the model
        """
        X = self.df.drop(['Price'], axis=1)
        y = self.df['Price']

        X = self.preprocessing(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.15, random_state=42)
        rfc = RandomForestRegressor(n_estimators=200)
        rfc.fit(X_train, y_train)

        score = rfc.score(X_test, y_test)
        return score

    def predict_diamond(self, data) -> float:
        """
        Method that predicts the price of a diamond

        Attributes
        ----------
        data : numpy narray
            The array of the data
        
        Returns
        -------
        prediction : float
            The predicted price of the diamond computed using 
            the predict method of the model
        """
        prediction = self.model.predict(data)
        return prediction
