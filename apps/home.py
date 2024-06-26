import streamlit as st

def app():
    # Set background image URL
    background_image = "https://miro.medium.com/v2/resize:fit:640/1*UIOup_6QtddueH9VjaT8HQ.jpeg"

    # Use HTML to set the background image
    # You can adjust the background-size, background-repeat, and other properties as needed
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url("{background_image}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Home')
    st.image(background_image, use_column_width=True)

if __name__ == "__main__":
    app()
