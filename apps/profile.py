import streamlit as st
from PIL import Image

# Function to identify heart disease based on user input
def identify_heart_disease(cp, target, thal, fbs, restecg, exang, slop, ca):
    if target == 0:
        if cp == 2 or restecg == 2:
            return "Coronary Artery Disease"
        elif thal == 3:
            return "Arrhythmia Disease"
        elif exang == 1 or fbs == 1:
            return "Cardiomyopathy Disease"
        elif slop == 0 or ca == 0:
            return "Aortic Disease"
        else:
            return "Heart Failure Disease"
    else:
        return "No Heart Disease"

treatment_options = {
    "Coronary Artery Disease": "Treatment may include medications (such as aspirin, beta blockers, or statins), lifestyle changes (such as diet and exercise), and in some cases, procedures like angioplasty or bypass surgery.",
    "Arrhythmia Disease": "Treatment may include medications (such as antiarrhythmic drugs) or procedures like cardioversion, catheter ablation, or implantation of a pacemaker or defibrillator.",
    "Cardiomyopathy Disease": "Treatment may include medications (such as ACE inhibitors, beta blockers, or diuretics), lifestyle changes (such as reducing salt intake), and in severe cases, heart transplantation.",
    "Aortic Disease": "Treatment depends on the specific type and severity of the aortic disease. It may include medications to lower blood pressure or surgery to repair or replace the damaged portion of the aorta.",
    "Heart Failure Disease": "Treatment may include medications (such as ACE inhibitors, beta blockers, or diuretics), lifestyle changes (such as reducing salt intake and exercising regularly), and in advanced cases, devices like implantable cardioverter-defibrillators (ICDs) or heart transplantation."
}

# Streamlit app
def app():
    st.title('Heart Disease Symptoms')

    # Adding an image upload option to the sidebar
    st.sidebar.title("User Profile")
    name = st.sidebar.text_input("Name")
    age = st.sidebar.number_input("Age", min_value=0, max_value=150, value=30)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])

    uploaded_image = st.sidebar.file_uploader("Upload User Image", type=["jpg", "jpeg", "png"])

    # Input sliders with labels
    cp = st.slider("Chest Pain (0: None, 1: Low, 2: Medium, 3: High)", 0, 3, 1)
    thal = st.slider("Thal (0: Normal, 1: Fixed, 2: Reversible, 3: Other)", 0, 3, 1)
    fbs = st.slider("Fasting Blood Sugar (0: Normal, 1: High)", 0, 1, 0)
    restecg = st.slider("Resting Electrocardiographic Results (0: Normal, 1: Abnormality, 2: Probable)", 0, 2, 1)
    exang = st.slider("Exercise Induced Angina (0: No, 1: Yes)", 0, 1, 0)
    slop = st.slider("Slope of the Peak Exercise ST Segment (0: Upsloping, 1: Flat, 2: Downsloping)", 0, 2, 1)
    ca = st.slider("Number of Major Vessels Colored by Fluoroscopy", 0, 4, 0)
    target = st.slider("Target (0: Heart Disease, 1: No Heart Disease)", 0, 1, 0)

    # Button to trigger prediction
    if st.button("Predict"):
        # Call function to identify heart disease type
        heart_disease_type = identify_heart_disease(cp, target, thal, fbs, restecg, exang, slop, ca)
        
        # Display user profile
        st.title("User Profile")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")

        # Display uploaded image
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            resized_image = image.resize((150, 150))
            st.sidebar.image(resized_image, caption='Uploaded Image', use_column_width=True)

        # Display prediction result
        st.title("Heart Disease Prediction Result")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_v1XA4Ow6w3RxLZP47auVeg-4Suz3w5fMkQ&usqp=CAU", use_column_width=True)
 

        st.write("**Heart Disease Type:**", heart_disease_type)

        treatment = treatment_options.get(heart_disease_type, "No specific treatment information available.")
        st.write("**Recommended Treatment:**", treatment)

        st.text(" ")
        
        st.subheader("Now, you can visit any cardiologist to get your recommended treatment....! ")

        st.image("https://img.freepik.com/premium-photo/stethoscope-forming-heart-with-its-cord-thank-you-doctor-nurses-medical-personnel-team_78048-616.jpg?size=626&ext=jpg", use_column_width=True)
        
        