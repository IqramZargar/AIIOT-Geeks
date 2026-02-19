# 🎬 Sentiment Analysis of Movie Reviews

A simple **Machine Learning + NLP project** that predicts whether a movie review is **Positive** or **Negative** using text analysis.
The project is built using **Python, Scikit-learn, and Streamlit**.

---

## 📌 Project Goal

The goal of this project is to:

* Understand **Natural Language Processing (NLP)** basics
* Convert text data into numbers understandable by machines
* Train a Machine Learning model to classify sentiments
* Build a simple **Streamlit web app** for user interaction
* Upload a clean, reproducible project to GitHub

---

## 🧠 What is Sentiment Analysis?

Sentiment analysis is a process of identifying emotion or opinion from text.

Example:

| Review                  | Sentiment |
| ----------------------- | --------- |
| This movie was amazing! | Positive  |
| Worst movie ever        | Negative  |

Our model learns patterns from many examples and predicts sentiment for new reviews.

---

## 🏗️ Project Structure

```
sentiment-analysis-movie-review/
│
├── data/
│   └── IMDB Dataset.csv
│
├── notebook/
│   └── sentiment.ipynb
│
├── app/
│   └── streamlit_app.py
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── requirements.txt
├── README.md

```

---

## ⚙️ Workflow (High-Level)

```
Movie Reviews Dataset
        ↓
Text Cleaning (remove noise)
        ↓
Text Vectorization (TF-IDF)
        ↓
Model Training (Logistic Regression)
        ↓
Model Evaluation
        ↓
Save Model
        ↓
Streamlit App
```

---

## 📊 Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression
* Streamlit
* Pickle

---

## 🧹 Text Preprocessing

Text cleaning steps:

* Convert text to lowercase
* Remove special characters and numbers
* Remove unnecessary symbols

This helps the model focus on meaningful words.

---

## 🔢 Text → Numbers (TF-IDF)

Machine learning models cannot understand words directly.

TF-IDF converts words into numerical vectors based on importance:

* Important words → higher weight
* Common words → lower weight

---

## 🤖 Model Training

Model used:

**Logistic Regression**

The model learns patterns between:

```
Text features (numbers) → Sentiment labels
```

---

## 📈 Model Evaluation

Performance checked using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix (optional)

---

## 💾 Saved Files

After training:

* `model.pkl` → trained ML model
* `vectorizer.pkl` → TF-IDF converter

These files are used in the Streamlit app so we don’t retrain every time.

---

## 🌐 Streamlit Web App

The app allows users to:

1. Enter a movie review
2. Click **Predict**
3. View sentiment result instantly

Run locally using:

```bash
streamlit run app/streamlit_app.py
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/IqramZargar/AIIOT-Geeks/tree/main/Advance%20ML/sentiment_analysis_movie_review
cd sentiment-analysis-movie-review
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Train Model (Notebook)

Run:

```
notebook/sentiment.ipynb
```

### Launch Streamlit App

```bash
streamlit run app/streamlit_app.py
```

---

## 🎯 Learning Outcomes

By completing this project, you learn:

* Basics of NLP
* Text preprocessing
* Feature extraction (TF-IDF)
* Classification models
* Model saving/loading
* Building ML web apps with Streamlit
* Project structuring for GitHub

---

## 📌 Future Improvements

* Add Neutral sentiment class
* Use Deep Learning (LSTM / Transformers)
* Improve UI design
* Deploy online (Streamlit Cloud / Render / HuggingFace)
* Add model confidence score

---

## 👨‍💻 Author

**Muhammad Iqram**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
