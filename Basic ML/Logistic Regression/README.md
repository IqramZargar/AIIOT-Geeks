# 🎓 Placement Prediction Using Logistic Regression

This project demonstrates how **Logistic Regression** can be used to predict whether a student will get placed based on their academic and skill-based performance.  
It uses a synthetic dataset of students and allows real-time user input for prediction.

---

## 📌 Project Overview

The model predicts **Placement Status (Placed / Not Placed)** using the following features:

- Analytical Skills Score
- Communication Skills Score
- Overall Percentage

### 🎯 Output (Binary Classification)

- **1 → Placed 🎉**
- **0 → Not Placed ❌**

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt

Or install manually:

pip install numpy pandas scikit-learn

📊 Dataset Description

A synthetic dataset of 10 students is used with the following columns:

Feature	Description
Analytical	Analytical skills score (0–100)
Communication	Communication skills score (0–100)
Overall_Percentage	Academic percentage (0–100)
Placed	Placement status (1 = Yes, 0 = No)

⚠️ This is a small synthetic dataset created for learning purposes.

⚙️ Program Workflow
1️⃣ Create Dataset

A synthetic dataset is created using Pandas.

2️⃣ Split the Data

70% Training data

30% Testing data

3️⃣ Train the Model

Logistic Regression model is trained using Scikit-learn.

4️⃣ Evaluate the Model

Accuracy Score

Classification Report (Precision, Recall, F1-score)

5️⃣ User Input Prediction

Takes new student details

Predicts placement outcome in real time

▶️ How to Run the Program
1️⃣ Install required libraries:
pip install numpy pandas scikit-learn

2️⃣ Run the Python script:
python placement_prediction.py

3️⃣ Enter student details when prompted:
Enter Analytical Skills (0-100):
Enter Communication Skills (0-100):
Enter Overall Percentage (0-100):

✅ Sample Output
Model Accuracy: 0.66

Classification Report:
              precision    recall  f1-score   support

--- Enter new student's details for placement prediction ---
Prediction: Placed 🎉


Accuracy may vary due to random train-test split.

⚠️ Notes

This is a small synthetic dataset, so performance may vary.

Designed for learning and demonstration purposes.

🚀 Future Enhancements

Use real placement data

Add data visualization

Save and load trained model

Build a GUI or web interface

Compare with other classification models (SVM, Random Forest, etc.)

📚 Learning Outcome

By completing this project, you will understand:

✔️ Logistic Regression (Binary Classification)

✔️ Working with Pandas DataFrames

✔️ Model evaluation techniques

✔️ Real-time prediction using Machine Learning

✔️ Accuracy, Precision, Recall, and F1-score

👨‍💻 Author

Muhammad Iqram
