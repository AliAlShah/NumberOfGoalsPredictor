import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data.csv")
data = data[["Jersey Number", "Club", "Position", "Nationality", "Age", "Appearances", "Wins", "Losses", "Goals"]]
print(data.info())