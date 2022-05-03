import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Loading Data
data = pd.read_csv("data.csv")
data = data[["Jersey Number", "Club", "Position", "Nationality", "Age", "Appearances", "Wins", "Losses", "Goals"]]

#Cleaning Data
data = data.dropna()
def clean_data(*field):
    def make_it_happen(x):
        unique_data = []
        unique_index_dict = {}
        for i in data[x].unique():
            unique_data.append(i)
        for n in unique_data:
            unique_index_dict[n] = unique_data.index(n)
        
        new_list = []
        for m in data[x]:
            new_list.append(unique_index_dict.get(m))
        data[x] = new_list

    for i in field:
        make_it_happen(i)


clean_data("Club", "Position", "Nationality")
int_list = []
for i in data["Jersey Number"]:
    int_list.append(int(i))
data["Jersey Number"] = int_list
int_list = []

for i in data["Age"]:
    int_list.append(int(i))
data["Age"] = int_list
    
#Setting up train and test data
predict = data["Goals"]
x = np.array(data.drop([predict], 1))
y = np.array(predict)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)



print(data.info())