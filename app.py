#app.py
import streamlit as st
import pandas as pd 
import joblib 
#Load trained model 
model=joblib.load("house_price_model.pkl")
#Streamlit app
st.title("House price predictor")
st.subheader("Enter the details to estimate house price:")
#user inputs 
bedrooms=st.number_input("Number of Bedrooms",min_value=1,max_value=10,value=3)
bathrooms=st.number_input("Number of Bathrooms",min_value=1,max_value=10,value=3)
area=st.number_input("Area (sqft)",min_value=500,max_value=10000,value=1500)

#Prediction time
if st.button("Predict Price"):
    input_df=pd.DataFrame([[bedrooms,bathrooms,area]],columns=['Bedrooms','Bathrooms','Area (sqft)'])
    prediction = model.predict(input_df)[0]  # Get the first value
    prediction = float(prediction)           # Convert to Python float
    st.success(f"🏷 Estimated Price: ₹ {prediction:,.2f}")
