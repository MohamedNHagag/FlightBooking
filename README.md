# Flight Booking Completion Prediction ✈️

This project is part of the British Airways Data Science Virtual Experience on Forage.  
The goal was to analyze real-world flight booking data and build a predictive model to understand whether a customer will complete their booking.

---

## Pipeline Steps

1️⃣ **Data Ingestion:**  
Load and split the dataset into training and testing sets, then explore and understand the data.

2️⃣ **Data Transformation:**  
Clean and scale the data using a preprocessing pipeline.

3️⃣ **Model Training:**  
Train multiple classification models and select the best one using evaluation metrics.

4️⃣ **Model Evaluation:**  
Evaluate the best model using Accuracy, Precision, Recall, and F1-Score to select the most suitable model.  
Achieved the best Accuracy, which was the main requirement of the task.

5️⃣ **Model Deployment:**  
Use Streamlit to create a user-friendly web interface for making predictions.

---

## Tools & Technologies Used

- Python (pandas, numpy, scikit-learn)  
- Jupyter Notebook for EDA and initial modeling  
- Streamlit for deployment  
- Machine Learning algorithms: Logistic Regression, Random Forest, Gradient Boosting, XGBoost

---

## How to Run

Clone the repository and install dependencies:

```bash
git clone https://github.com/MohamedNHagag/FlightBooking.git
cd FlightBooking
streamlit run FlightBooking.py


