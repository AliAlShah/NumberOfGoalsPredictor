import pandas as pd
import numpy as np
import tkinter as tk
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

window = tk.Tk()

#Loading Data
data = pd.read_csv("data.csv")
data = data[["Club", "Position", "Nationality", "Age", "Appearances", "Wins", "Losses", "Goals"]]

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
        print(unique_index_dict)

    for i in field:
        make_it_happen(i)

    


clean_data("Club", "Position", "Nationality")
int_list = []

for i in data["Age"]:
    int_list.append(int(i))
data["Age"] = int_list
    
#Setting up train and test data
y = data["Goals"]
x = data.drop("Goals", axis=1)

#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

#Making Model and Testing accuracy
#model = LinearRegression()
#model.fit(x_train, y_train)

#acc = model.score(x_test, y_test)
#print(acc)

#Training and saving model
#n = 0
#high_score = 0
#high_score_history = []
#while n<100000:
#    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=random.uniform(0.05, 0.5))
#    model = LinearRegression()
#    model.fit(x_train, y_train)
#    acc = model.score(x_test, y_test)
#
#    if acc > high_score:
#        high_score = acc
#        high_score_history.append(high_score)
#        with open("savedmodel.pickle", "wb") as f:
#                pickle.dump(model, f)
#
#    print(f"Accuracy: {high_score}")
#    print(f"Iteration: {(n/100000) * 100}%")
#    n = n + 1
#print(high_score_history)



def predict(values):
    pickle_in = open("savedmodel.pickle", "rb")
    model = pickle.load(pickle_in)
    values = [int(value) for value in values]

    result = model.predict([values])
    if result[0] < 0:
        result[0] = 0
    else:
        result = result

    new_window = tk.Toplevel(window)
    tk.Label(new_window, text=str(round(float(result[0])))).pack()

    

club_text = tk.Label(text="Club", width=25).grid(column=0, row=0)
club_input_field = tk.Entry(width=25)
club_input_field.grid(column=0, row=1)

position_text = tk.Label(text="Position", width=25).grid(column=1, row=0)
position_input_field = tk.Entry(width=25)
position_input_field.grid(column=1, row=1)

nationality_text = tk.Label(text="Nationality", width=25).grid(column=2, row=0)
nationality_input_field = tk.Entry(width=25)
nationality_input_field.grid(column=2, row=1)

age_text = tk.Label(text="Age", width=25).grid(column=3, row=0)
age_input_field = tk.Entry(width=25)
age_input_field.grid(column=3, row=1)

apperances_text = tk.Label(text="Apperances", width=25).grid(column=4, row=0)
apperances_input_field = tk.Entry(width=25)
apperances_input_field.grid(column=4, row=1)

wins_text = tk.Label(text="Wins", width=25).grid(column=5, row=0)
wins_input_field = tk.Entry(width=25)
wins_input_field.grid(column=5, row=1)

losses_text = tk.Label(text="Losses", width=25).grid(column=6, row=0)
losses_input_field = tk.Entry(width=25)
losses_input_field.grid(column=6, row=1)

predict_button = tk.Button(text="Predict", width=20, bg="red", command=lambda: predict(
    [club_input_field.get(), position_input_field.get(), nationality_input_field.get(), age_input_field.get(), apperances_input_field.get(), wins_input_field.get(), losses_input_field.get()])).grid(column=0, row=2)




window.mainloop()