import streamlit as st
import pickle

model = pickle.load(open("model/model.pkl","rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl","rb"))

st.title("Movie Review Sentiment Analysis")

review = st.text_area("Enter movie review")

if st.button("Predict"):
    vector = vectorizer.transform([review])
    prediction = model.predict(vector)[0]
    st.success(f"Sentiment: {prediction}")
