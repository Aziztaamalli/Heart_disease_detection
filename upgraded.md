def identify_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target):
    if target == 0:
        if cp == 2 or restecg == 2:
            return "Coronary Artery Disease"
        elif thal == 3:
            return "Arrhythmia Disease"
        elif exang == 1 or fbs == 1:
            return "Cardiomyopathy Disease"
        elif slope == 0 or ca == 0:
            return "Aortic Disease"
        elif age >= 60:
            return "Age-related Heart Disease"
        elif trestbps > 140:
            return "Hypertension"
        elif chol > 200:
            return "Hypercholesterolemia"
        elif sex == 0 and age > 50:
            return "Menopause-related Heart Disease"
        else:
            return "Heart Failure Disease"
    else:
        return "No Heart Disease"


# Get user input
age = int(input("Enter the age: "))
sex = int(input("Enter the sex (0 for female, 1 for male): "))
cp = int(input("Enter the Chest Pain: "))
trestbps = int(input("Enter the resting blood pressure: "))
chol = int(input("Enter the serum cholesterol level: "))
fbs = int(input("Enter the fasting blood sugar (1 if > 120 mg/dl, 0 otherwise): "))
restecg = int(input("Enter the resting electrocardiographic results: "))
thalach = int(input("Enter the maximum heart rate achieved: "))
exang = int(input("Enter exercise-induced angina (1 if yes, 0 otherwise): "))
oldpeak = float(input("Enter the ST depression induced by exercise relative to rest: "))
slope = int(input("Enter the slope of the peak exercise ST segment: "))
ca = int(input("Enter the number of major vessels colored by fluoroscopy: "))
thal = int(input("Enter the thalassemia (thal) value: "))
target = int(input("Enter the target (0 for heart disease, 1 for no heart disease): "))

# Call function to identify heart disease type
heart_disease_type = identify_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target)
print("Heart Disease Type:", heart_disease_type)

------------------------------------
---------------------------------------------
----------------------------------------------------------------------

or we can also put 
--------------
def identify_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target):
    diseases = {
        (2, None, None): "Coronary Artery Disease",
        (None, None, 3): "Arrhythmia Disease",
        (None, 1, None): "Cardiomyopathy Disease",
        (0, None, None): "Aortic Disease",
        (60, None, None): "Age-related Heart Disease",
        (None, None, None): "Heart Failure Disease",
        (None, None, None, 1, None, None): "Hypertension",
        (None, None, None, None, 1, None): "Hypercholesterolemia",
        (None, 0, 50): "Menopause-related Heart Disease"
        # Add more disease conditions and corresponding labels as needed
    }
    
    # Check if the input conditions match any disease condition in the dictionary
    for conditions, disease in diseases.items():
        if all(condition is None or condition == value for condition, value in zip(conditions, [cp, fbs, age])):
            return disease
    
    return "No Heart Disease"


# Get user input
age = int(input("Enter the age: "))
sex = int(input("Enter the sex (0 for female, 1 for male): "))
cp = int(input("Enter the Chest Pain: "))
trestbps = int(input("Enter the resting blood pressure: "))
chol = int(input("Enter the serum cholesterol level: "))
fbs = int(input("Enter the fasting blood sugar (1 if > 120 mg/dl, 0 otherwise): "))
restecg = int(input("Enter the resting electrocardiographic results: "))
thalach = int(input("Enter the maximum heart rate achieved: "))
exang = int(input("Enter exercise-induced angina (1 if yes, 0 otherwise): "))
oldpeak = float(input("Enter the ST depression induced by exercise relative to rest: "))
slope = int(input("Enter the slope of the peak exercise ST segment: "))
ca = int(input("Enter the number of major vessels colored by fluoroscopy: "))
thal = int(input("Enter the thalassemia (thal) value: "))
target = int(input("Enter the target (0 for heart disease, 1 for no heart disease): "))

# Call function to identify heart disease type
heart_disease_type = identify_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target)
print("Heart Disease Type:", heart_disease_type)