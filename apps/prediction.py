import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
def load_data():
    df = pd.read_csv('heart.csv')
    return df

# Train model
def train_model(df):
    X = df.drop('target', axis=1)
    y = df['target']
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

# Make prediction
def predict(model, data):
    prediction = model.predict(data)
    return prediction

def app():
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT37yKCkbXIoYMiP4KOFsiZyMQk90Mlc0i_ew&usqp=CAU",use_column_width=True)

    st.title('Heart Disease Prediction')

    # Load data
    df = load_data()

    # Train model
    model = train_model(df)

    # User input for prediction
    st.sidebar.title('Enter Patient Details')
    age = st.sidebar.slider('Age', 20, 100, 50)
    sex = st.sidebar.selectbox('Sex', ['Male', 'Female'])
    cp = st.sidebar.slider('Chest Pain Type', 0, 3, 1)
    trestbps = st.sidebar.slider('Resting Blood Pressure (mm Hg)', 90, 200, 120)
    chol = st.sidebar.slider('Serum Cholesterol (mg/dl)', 100, 600, 200)
    fbs = st.sidebar.selectbox('Fasting Blood Sugar (> 120 mg/dl)', ['True', 'False'])
    restecg = st.sidebar.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T wave abnormality', 'Probable or definite left ventricular hypertrophy'])
    thalach = st.sidebar.slider('Maximum Heart Rate Achieved', 60, 220, 150)
    exang = st.sidebar.selectbox('Exercise Induced Angina', ['Yes', 'No'])
    oldpeak = st.sidebar.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 6.2, 1.0)
    slope = st.sidebar.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
    ca = st.sidebar.slider('Number of Major Vessels Colored by Fluoroscopy', 0, 4, 0)
    thal = st.sidebar.selectbox('Thalassemia', ['Normal', 'Fixed defect', 'Reversable defect'])

    # Convert categorical inputs to numerical
    sex = 1 if sex == 'Male' else 0
    fbs = 1 if fbs == 'True' else 0
    restecg_map = {'Normal': 0, 'ST-T wave abnormality': 1, 'Probable or definite left ventricular hypertrophy': 2}
    restecg = restecg_map[restecg]
    exang = 1 if exang == 'Yes' else 0
    slope_map = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
    slope = slope_map[slope]
    thal_map = {'Normal': 0, 'Fixed defect': 1, 'Reversable defect': 2}
    thal = thal_map[thal]
    
    # Create input data for prediction
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    })

    # Make prediction
    if st.sidebar.button('Predict'):
        prediction = predict(model, input_data)
        if prediction[0] == 1:
            st.write('**Prediction:** You have heart disease')
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKkjWmuujv3Pkp9_egdRcjy7OuPzvdo3BMZOU9fvAvMsLcar9-rsxxurx5B7YwwzFe3JU&usqp=CAU",use_column_width=True)
        else:
            st.write('**Prediction:** No Heart Disease')
            st.image("No_HD.png",use_column_width=True)
       

  
    

