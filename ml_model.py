import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Train model on dummy dataset
def train_model():
    X = np.array([
        [18, 0],    # Underweight + No disease
        [23, 0],    # Normal + No disease
        [28, 0],    # Overweight
        [32, 1],    # Obese + Diabetes
        [27, 2],    # Overweight + BP
        [22, 3],    # Thyroid
    ])

    y = ["High Protein", "Balanced Diet", "Low Carb", "Diabetic Diet", "BP Diet", "Thyroid Diet"]

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, "meal_model.pkl")


def predict_meal(bmi, disease_code):
    model = joblib.load("meal_model.pkl")
    return model.predict([[bmi, disease_code]])[0]


# Train model when file runs
train_model()
