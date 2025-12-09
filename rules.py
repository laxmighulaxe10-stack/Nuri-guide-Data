def recommend_meal(bmi, disease):
    # BMI-based rules
    if bmi < 18.5:
        bmi_meal = "High-protein meals, eggs, nuts, whole grains, milk"
    elif 18.5 <= bmi <= 24.9:
        bmi_meal = "Balanced meals: fruits, vegetables, lean meat, whole grains"
    elif 25 <= bmi <= 29.9:
        bmi_meal = "Low-carb meals, salads, soups, vegetables"
    else:
        bmi_meal = "Very low-carb, green vegetables, avoid sugar"

    # Disease-based rules
    if disease.lower() == "diabetes":
        disease_meal = "Low-sugar foods, oats, green veggies, brown rice"
    elif disease.lower() == "blood pressure":
        disease_meal = "Low-salt diet, bananas, leafy vegetables"
    elif disease.lower() == "thyroid":
        disease_meal = "Iodine-rich diet, eggs, milk; avoid soy"
    else:
        disease_meal = "General healthy diet recommended"

    return bmi_meal, disease_meal
