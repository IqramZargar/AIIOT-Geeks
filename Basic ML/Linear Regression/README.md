# 🏠 House Price Prediction Using Linear Regression

This project demonstrates **Simple Linear Regression** using a 2D NumPy array to predict house prices based on area (in square feet).  
It also evaluates model performance and visualizes the regression line.

---

## 📌 Project Overview

The goal is to predict **house price (in Lakhs)** using:

- **Input Feature:** Area of the house (sqft)
- **Output Target:** Price (Lakhs)

The model is trained using **Scikit-learn’s LinearRegression** and evaluated using standard regression metrics.

---

## 🛠️ Technologies Used

- Python
- NumPy
- Matplotlib
- Scikit-learn

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt

Or install manually:

pip install numpy matplotlib scikit-learn

📊 Dataset Description

The dataset is defined as a 2D NumPy array:

Area (sqft)	Price (Lakhs)
800	  30
1000	38
1200	45
1500	55
1800	65
2000	70
2200	78
2500	90
2800	100
3000	110

⚠️ This is a small synthetic dataset created for learning purposes.

⚙️ Program Workflow
1️⃣ Create Dataset

Data is stored as a 2D NumPy array.

2️⃣ Split Features and Target

X → Area (independent variable)

y → Price (dependent variable)

3️⃣ Train-Test Split

80% Training data

20% Testing data

4️⃣ Train Linear Regression Model

The model learns the best-fit line from the training data.

5️⃣ Make Predictions

Predicts house prices for the test dataset.

6️⃣ Evaluate Model

Intercept

Coefficient

Mean Squared Error (MSE)

R² Score

7️⃣ Visualization

Scatter plot of actual data points

Regression best-fit line

▶️ How to Run the Program

1️⃣ Install required libraries:

pip install numpy matplotlib scikit-learn


2️⃣ Run the Python file:

python linear_regression_2d.py

✅ Sample Output
Intercept: -3.21
Coefficient: 0.037

Actual vs Predicted:
Actual: 38, Predicted: 40.12
Actual: 100, Predicted: 103.45

MSE: 4.82
R2: 0.98


Values may vary due to train-test split randomness.

📈 Visualization Output

The output graph shows:

🔵 Scatter plot of actual house prices

🔴 Straight regression line representing best fit

⚠️ Notes

This is Simple Linear Regression with only one feature.

Dataset is small and synthetic.

Assumes a linear relationship between area and price.

🚀 Future Enhancements

Use real housing datasets

Add multiple features (bedrooms, location, age of house, etc.)

Compare with Polynomial Regression

Save trained model using joblib or pickle

Deploy as a simple web app

📚 Learning Outcomes

By completing this project, you will understand:

✔️ How Linear Regression works

✔️ Working with 2D NumPy arrays

✔️ Train-test splitting

✔️ Model evaluation using MSE & R²

✔️ Data visualization with Matplotlib

👨‍💻 Author

Muhammad Iqram
