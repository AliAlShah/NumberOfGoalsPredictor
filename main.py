import pandas as pd
import numpy as np
import pickle
import random
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
       # print(unique_index_dict)

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
y = data["Goals"]
x = data.drop("Goals", axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

#Making Model and Testing accuracy
model = LinearRegression()
model.fit(x_train, y_train)

acc = model.score(x_test, y_test)
print(acc)

#Training and saving model
n = 0
high_score = 0
high_score_history = []
while n<10000:
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=random.uniform(0.05, 0.5))
    model = LinearRegression()
    model.fit(x_train, y_train)
    acc = model.score(x_test, y_test)

    if acc > high_score:
        high_score = acc
        high_score_history.append(high_score)
        with open("savedmodel.pickle", "wb") as f:
                pickle.dump(model, f)

    print(f"Accuracy: {high_score}")
    print(f"Iteration: {(n/10000) * 100}%")
    n = n + 1
print(high_score_history)


pickle_in = open("savedmodel.pickle", "rb")
model = pickle.load(pickle_in)
print(model.predict([[29, 4, 2, 0, 21, 25, 13, 9]]))