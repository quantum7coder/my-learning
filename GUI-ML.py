# A simple GUI application using Tkinter that integrates a machine learning model to make predictions based on user input.

import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
import numpy as np
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])
model = LinearRegression()
model.fit(X, y)
def predict_value():
    try:
        user_val = float(entry.get())
        user_array = np.array([[user_val]])
        pred = model.predict(user_array)[0]
        messagebox.showinfo("Prediction", f"Predicted value: {pred:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
root = tk.Tk()
root.title("Simple ML Predictor")
root.geometry("300x200")
label = tk.Label(root, text="Enter a number:", font=("Arial", 12))
label.pack(pady=10)
entry = tk.Entry(root, width=15, font=("Arial", 12))
entry.pack()
predict_btn = tk.Button(root, text="Predict", command=predict_value,
                        font=("Arial", 12), bg="lightblue")
predict_btn.pack(pady=20)
root.mainloop()
