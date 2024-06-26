import streamlit as st
from multiapp import MultiApp
from apps import home, prediction, profile # import your app modules here

app = MultiApp()

st.title('Heart Disease Prediction and Treatment Recomendation System')

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Prediction", prediction.app)
app.add_app("Profile", profile.app)
# The main app
app.run()
