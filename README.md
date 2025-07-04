# HousePricePredictor
This is a basic house price predictor app that is built on Linear Regression. The app is deployed on streamlit and it is a very basic project to undertsnad how a ML model is built and deployed on stremalit.
## The project has following architecture:
/house-price-predictor
│
├── app.py
├── model.ipynb
├── house_prices.csv
├── house_price_model.pkl (generated after training)
├── requirements.txt
### app.py
This repo contains the python code for building the streamlit web app and integrating the ML model with the inputs from web app. 

### model.ipynb
It contains the logic of ML model building and exporting the model.

### house_prices.csv
This the dataet on which the model was trained

### house_price_model.pkl
This is the mdoel finalised ofter building the model. It is exported for croos file use of our ML Model.

### requirements.txt
It contains the necessary libraries for building and runming the whold app.


