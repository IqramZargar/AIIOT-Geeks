# 🚢 Titanic Exploratory Data Analysis (EDA)

## 📌 Project Overview
This project performs **Exploratory Data Analysis (EDA)** on the famous Titanic dataset.  
The goal is to analyze passenger data to discover patterns, relationships, and factors that influenced survival during the Titanic disaster.

EDA helps in understanding the dataset before applying machine learning or statistical modeling.

---

## 🎯 Objectives
- Understand dataset structure and features  
- Identify missing or inconsistent data  
- Analyze feature distributions  
- Explore relationships between variables  
- Extract meaningful insights from passenger data  
- Visualize trends using graphs and plots  

---

## 📊 Dataset Information
The dataset contains information about passengers aboard the Titanic.

### 🔗 Dataset Source
[Kaggle Titanic Competition Dataset](https://www.kaggle.com/competitions/titanic/data)

### 📁 Dataset Files
- `train.csv` → Used for analysis  
- `test.csv` → Optional (included for completeness)

---

## 🧾 Feature Description

| Feature | Description |
|-------|------------|
| PassengerId | Unique passenger ID |
| Survived | Survival status (0 = No, 1 = Yes) |
| Pclass | Passenger ticket class |
| Name | Passenger name |
| Sex | Gender |
| Age | Passenger age |
| SibSp | Number of siblings/spouse aboard |
| Parch | Number of parents/children aboard |
| Ticket | Ticket number |
| Fare | Ticket fare |
| Cabin | Cabin number |
| Embarked | Port of embarkation |

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  
- Git & GitHub  

---

## 📂 Project Structure

EDA-PROJECT-ON-TitanicDS/
│
├── dataset/
│ ├── train.csv
│ └── test.csv
│
├── notebooks/
│ └── EDA.ipynb
│
├── requirements.txt
└── README.md


---

## 🔍 EDA Workflow

### 1️⃣ Data Loading
- Imported dataset using Pandas  
- Verified structure and format  

### 2️⃣ Dataset Overview
- Checked shape, column names, and data types  
- Generated statistical summary  

### 3️⃣ Missing Value Analysis
- Identified missing values  
- Visualized missing data using heatmaps  

### 4️⃣ Univariate Analysis
- Survival count  
- Gender distribution  
- Age distribution  

### 5️⃣ Bivariate Analysis
- Survival vs Gender  
- Survival vs Passenger Class  
- Age vs Survival  

### 6️⃣ Correlation Analysis
- Generated correlation heatmap  
- Studied relationships between numerical features  

---

## 📈 Key Insights
- Female passengers had significantly higher survival rates  
- Passengers in higher classes (1st class) had better survival chances  
- Majority of passengers were adults  
- Some columns (Age, Cabin) contain missing values  

---

## ▶️ How To Run This Project

### Step 1 — Clone Repository
```bash
git clone <your-repo-link>
cd titanic-eda

Step 2 — Create Virtual Environment
python -m venv venv

Activate environment:

Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

Step 3 — Install Dependencies

pip install -r requirements.txt

Step 4 — Run Notebook

jupyter notebook


Open:

notebooks/EDA.ipynb

📷 Sample Visualizations

The notebook contains:

Count plots

Histograms

Box plots

Correlation heatmaps

Pairwise relationship plots

📚 Learning Outcomes

Through this project, I learned:

Importance of data exploration before modeling

Handling missing values

Understanding feature relationships

Creating meaningful data visualizations

Structuring real-world data analysis projects

🚀 Future Improvements

Data cleaning and preprocessing

Feature engineering

Machine learning survival prediction model

Interactive dashboard visualization

👤 Author

Muhammad Iqram
