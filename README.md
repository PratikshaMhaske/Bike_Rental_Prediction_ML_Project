**Project Overview**
This project aims to predict the number of bike rentals based on various weather and seasonal features. Using historical data, machine learning models are trained to forecast daily bike rental demand, helping bike rental companies optimize inventory and improve customer service.

**Dataset**

The dataset includes the following features:

Feature         	Description
season           	Season (spring, summer, fall, winter)
weather	          Weather condition (clear, cloudy, rainy, etc.)
temperature	      Temperature in Celsius
humidity	        Humidity level
windspeed	        Wind speed
datetime	        Date and time of the record
count	            Number of bike rentals (target variable)


**Tech Stack**

Python 3.x

Libraries: pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn

ML Models: XGBoost Regressor, Random Forest Regressor, Linear Regression


**Project Steps**

**Data Preprocessing**

Handle missing values

Encode categorical variables

Feature scaling

**Exploratory Data Analysis (EDA)**

Visualize seasonal trends

Correlation analysis between features

**Model Training & Evaluation**

Train multiple regression models

Evaluate using R² score and RMSE

Select best-performing model (XGBoost achieved 91% R²)

**Prediction**

Predict bike rentals for given conditions

Handle extreme weather scenarios


**Results**

XGBoost Regressor: **R² = 0.91**

Predictions handle seasonality and weather changes accurately.

Provides actionable insights for bike rental companies.


**Future Improvements**

Incorporate holiday & event data for better predictions

Use time-series models like LSTM for more accuracy

Deploy as a web app for real-time predictions

**Author**

**Pratiksha Mhaske – Engineer**

**LinkedIn:** https://www.linkedin.com/in/pratiksha-mhaske-173643387

**GitHub:** https://github.com/PratikshaMhaske

**Project Explanation:** https://drive.google.com/file/d/1Nq0OItwnTrpSxjs_hKk2HWYBtdlW56tJ/view?usp=sharing
