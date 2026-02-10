🏠 House Price Prediction Using Linear Regression

This project demonstrates Simple Linear Regression using a 2D NumPy array to predict house prices based on area (in square feet). It also evaluates model performance and visualizes the regression line.

📌 Project Overview

The goal is to predict house price (in Lakhs) using:

Input Feature: Area of the house (sqft)

Output Target: Price (Lakhs)

The model is trained using Scikit-learn’s LinearRegression and evaluated using standard regression metrics.

🛠️ Technologies Used

Python

NumPy

Matplotlib

Scikit-learn

📊 Dataset Description

The dataset is defined as a 2D NumPy array:

Area (sqft)	Price (Lakhs)
800	30
1000	38
1200	45
1500	55
1800	65
2000	70
2200	78
2500	90
2800	100
3000	110
⚙️ Program Workflow

Create Dataset
Data is stored as a 2D NumPy array.

Split Features and Target

X → Area (independent variable)

y → Price (dependent variable)

Train-Test Split

80% Training data

20% Testing data

Train Linear Regression Model

Learns the best-fit line from training data

Make Predictions

Predicts house prices for test data

Evaluate Model

Intercept

Coefficient

Mean Squared Error (MSE)

R² Score

Visualization

Scatter plot of data points

Regression best-fit line

▶️ How to Run the Program

Install required libraries:

pip install numpy matplotlib scikit-learn


Run the Python file:

python linear_regression_2d.py

✅ Sample Output
Intercept: -3.21
Coefficient: 0.037

Actual vs Predicted:
Actual: 38, Predicted: 40.12
Actual: 100, Predicted: 103.45

MSE: 4.82
R2: 0.98


(Values may vary due to train-test split)

📈 Visualization Output

Scatter plot showing actual data points

Straight line representing the regression fit

⚠️ Notes

This is a simple linear regression with one feature.

Dataset is small and synthetic (for learning purposes).

Assumes a linear relationship between area and price.

🚀 Future Enhancements

Use real housing datasets

Add multiple features (bedrooms, location, etc.)

Compare with Polynomial Regression

Save trained model for reuse

📚 Learning Outcomes

Understanding Linear Regression

Working with 2D NumPy arrays

Model evaluation using MSE & R²

Data visualization with Matplotlib