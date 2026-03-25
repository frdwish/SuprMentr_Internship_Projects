import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
study_hours = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
scores = np.array([35, 40, 50, 55, 65, 70, 80, 90])

# Model training
model = LinearRegression()
model.fit(study_hours, scores)

# Prediction
predicted_score = model.predict([[6]])
print("Predicted Score for 6 study hours:", int(predicted_score[0]))

# Testing with new input
new_hours = float(input("Enter study hours: "))
new_prediction = model.predict([[new_hours]])
print("Predicted Score:", int(new_prediction[0]))