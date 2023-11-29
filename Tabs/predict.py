"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import pandas as pd

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Early Prediction of Demenia.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    total_protein = st.slider("total_protein", int(df["total_protein"].min()), int(df["total_protein"].max()))
    total_keratine = st.slider("total_keratine", int(df["total_keratine"].min()), int(df["total_keratine"].max()))
    hair_texture = st.slider("hair_texture", int(df["hair_texture"].min()), int(df["hair_texture"].max()))
    vitamin = st.slider("vitamin", int(df["vitamin"].min()), int(df["vitamin"].max()))
    manganese = st.slider("manganese", int(df["manganese"].min()), int(df["manganese"].max()))
    iron = st.slider("iron", float(df["iron"].min()), float(df["iron"].max()))
    calcium = st.slider("calcium", float(df["calcium"].min()), float(df["calcium"].max()))
    body_water_content = st.slider("body_water_content", float(df["body_water_content"].min()), float(df["body_water_content"].max()))
    stress_level = st.slider("stress_level", float(df["stress_level"].min()), float(df["stress_level"].max()))
    liver_data = st.slider("liver_data", float(df["liver_data"].min()), float(df["liver_data"].max()))
    # Create a list to store all the features
    features = [total_protein,total_keratine,hair_texture,vitamin,manganese,iron,calcium,body_water_content,stress_level,liver_data]

    
    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns=["total_protein","total_keratine","hair_texture","vitamin","manganese","iron","calcium","body_water_content","stress_level","liver_data"]
    st.dataframe(df3)

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score#correction factor
        st.info("Predicted Sucessfully")

        # Print the output according to the prediction
        if (prediction == 1):
            st.success("The person has no risk of Hair Loss")
        elif (prediction == 2):
            st.error("The person has risk of few hair loss if not maintained")
        elif (prediction == 3):
            st.error("The person has risk of medium hair loss if not maintained")
        elif (prediction == 4):
            st.error("The person has risk of acute hair loss if not maintained")
        elif (prediction == 5):
            st.error("The person has risk of acute baldness and may have genetic causes.")
        
        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", round((score*100)), "%")
        