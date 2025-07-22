import streamlit as st
import numpy as np
import pickle
from joblib import load


model = load(r"D:\Data_Science\7-Machine_Learning\projects\British_Airways_realData\Flight Bookings_Model.joblib")
st.title("✈️ Flight Booking Prediction App")
st.write("Enter customer data to see if the reservation will be completed or not.")


# إدخال بيانات العميل
num_passengers = st.number_input("Number of Passengers", min_value=1, max_value=10, value=1)
sales_channel = st.selectbox("Sales Channel", [0, 1], format_func=lambda x: "Website" if x == 0 else "Mobile App")
trip_type = st.selectbox("Trip Type", [0, 1], format_func=lambda x: "One-way" if x == 0 else "Round-trip")
purchase_lead = st.number_input("Days before flight (Purchase Lead)", min_value=0, max_value=365, value=10)
length_of_stay = st.number_input("Length of Stay (days)", min_value=0, max_value=60, value=5)
flight_hour = st.number_input("Flight Hour (0-23)", min_value=0, max_value=23, value=10)
flight_day = st.number_input("Flight Day (0=Monday ... 6=Sunday)", min_value=0, max_value=6, value=2)
route = st.number_input("Route (Encoded)", min_value=0, max_value=100, value=5)
booking_origin = st.number_input("Booking Origin (Encoded)", min_value=0, max_value=100, value=10)
wants_extra_baggage = st.selectbox("Wants Extra Baggage?", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
wants_preferred_seat = st.selectbox("Wants Preferred Seat?", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
wants_in_flight_meals = st.selectbox("Wants In-flight Meals?", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
flight_duration = st.number_input("Flight Duration (hours)", min_value=0.0, max_value=20.0, value=2.0)

# زر التنبؤ
if st.button("Predict Booking Completion"):
    input_data = np.array([num_passengers, sales_channel, trip_type, purchase_lead, length_of_stay,
                            flight_hour, flight_day, route, booking_origin, wants_extra_baggage,
                            wants_preferred_seat, wants_in_flight_meals, flight_duration]).reshape(1, -1)

    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.error('❌ Customer is unlikely to complete the booking.')
    else:
        st.success("🎉 Customer is likely to complete the booking!")
