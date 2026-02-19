import os
import pickle

BASE_DIR = os.path.dirname(os.path.realpath(__file__))  # safer than abspath
MODEL_PATH = os.path.normpath(os.path.join(BASE_DIR, '..', 'model', 'model.pkl'))
VECTORIZER_PATH = os.path.normpath(os.path.join(BASE_DIR, '..', 'model', 'vectorizer.pkl'))

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

with open(VECTORIZER_PATH, 'rb') as f:
    vectorizer = pickle.load(f)


st.title("Movie Review Sentiment Analysis")

review = st.text_area("Enter movie review")

if st.button("Predict"):
    vector = vectorizer.transform([review])
    prediction = model.predict(vector)[0]
    st.success(f"Sentiment: {prediction}")
