# Regression on diamond price

Diamonds are precious stones consisting of a clear and colourless crystalline form of pure carbon. They are the hardest gemstones known to man and can be scratched only by other diamonds.

Diamonds are formed deep within the Earth about 100 miles or so below the surface in the upper mantle. Obviously, the temperature of this part of the Earth is very high. Plus, there is a lot of pressure, the weight of the overlying rock bearing down. The combination of high temperature and high pressure is what’s necessary to grow diamond crystals in the Earth.

Diamonds are rare because of the incredibly powerful forces needed to create them and therefore they are considered to be very costly.

The goal of this project is to do a regression on diamond prices using an API.

## *Required librairies*

- NumPy
- Pandas
- Scikit-learn
- FastAPI
- Joblib

## Dataset features
- Carat Weight: in grams
- Cut: how good the cut is
- Color: the color of the diamond
- Clarity: diamond clarity rating
- Polish: diamond polish rating
- Symmetry: diamond symmetry rating
- Report: which company has graded the diamond
- Price: in US dollars

We have qualitative features (categorical) such as Cut, Color, Clarity, Polish, Symmetry and Report; and some quantitative features (numerical) such as Carat Weight and Price. The target variable is Price.

## How to use
The project is built upon the idea of using an API.
To use the project, one must simply download the files, copy paste the following command in their terminal
```uvicorn api:app --reload``` go to ```http://127.0.0.1:8000/docs#``` and select parameters in the prediction function.



