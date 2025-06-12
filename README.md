🏠 House Price Prediction using Machine Learning
This project is a Machine Learning-based web application that predicts house prices based on various features like area, number of bedrooms, and bathrooms. It aims to provide a quick and accurate estimation for real estate users using a simple, user-friendly interface built with Flask.

📌 Project Overview
The goal of this project is to:

Collect and preprocess real estate data.

Train a machine learning model to predict house prices.

Deploy the model using a Flask web application.

Provide an interactive frontend for users to input details and view predictions.

🔧 Technologies Used
👨‍💻 Backend
Python 🐍

NumPy, Pandas

Scikit-learn (for ML model)

Pickle (to save the model)

🌐 Frontend
HTML/CSS

Bootstrap (for UI)

JavaScript (optional interactivity)

🚀 Deployment
Flask Web Framework

🧠 Machine Learning Workflow
Data Collection: Used a cleaned dataset containing housing features and price.

Preprocessing: Handled missing values, label encoding, feature selection.

Model Selection: Chose Linear Regression for prediction.

Training & Evaluation: Split data into train-test sets, trained the model, and evaluated with metrics like R² score.

Model Saving: Serialized the trained model using Pickle.

Integration: Connected the model to the Flask backend for real-time predictions.

💡 Features
📍 Predicts house price based on input parameters.

🧮 Clean ML pipeline from preprocessing to model evaluation.

🌐 Simple UI for easy interaction.

🔄 Real-time prediction using Flask.

