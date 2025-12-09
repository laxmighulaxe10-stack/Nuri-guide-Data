from flask import Flask, render_template, request
import mysql.connector
from models.rules import recommend_meal
from models.ml_model import predict_meal

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SKPatul@50790",  # CHANGE THIS
    database="nuriguide"
)
cursor = db.cursor()

# Disease code for ML model
disease_mapping = {
    "None": 0,
    "Diabetes": 1,
    "Blood Pressure": 2,
    "Thyroid": 3
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    gender = request.form['gender']
    disease = request.form['disease']

    # BMI Calculation
    bmi = weight / ((height / 100) ** 2)

    # Save user input
    cursor.execute(
        "INSERT INTO users (age, height, weight, gender, bmi, disease) VALUES (%s,%s,%s,%s,%s,%s)",
        (age, height, weight, gender, bmi, disease)
    )
    db.commit()

    # Rule-based recommendation
    bmi_meal, disease_meal = recommend_meal(bmi, disease)

    # ML model prediction
    disease_code = disease_mapping[disease]
    ml_meal = predict_meal(bmi, disease_code)

    return render_template(
        "result.html",
        bmi=round(bmi, 2),
        bmi_meal=bmi_meal,
        disease_meal=disease_meal,
        ml_meal=ml_meal
    )

if __name__ == "__main__":
    app.run(debug=True)
