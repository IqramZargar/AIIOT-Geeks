import streamlit as st
import pickle
import os

# Get the folder where this script resides
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths to model and vectorizer
MODEL_PATH = os.path.join(BASE_DIR, '..', 'model', 'model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, '..', 'model', 'vectorizer.pkl')

# Load model and vectorizer
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

with open(VECTORIZER_PATH, 'rb') as f:
    vectorizer = pickle.load(f)

# Streamlit UI
st.title("Movie Review Sentiment Analysis")

review = st.text_area("Enter movie review")

if st.button("Predict"):
    vector = vectorizer.transform([review])
    prediction = model.predict(vector)[0]
    st.success(f"Sentiment: {prediction}")
