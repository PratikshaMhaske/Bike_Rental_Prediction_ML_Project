# Import required Libraries
import streamlit as st
import pickle
import pandas as pd

# Load scaler and model
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('xgb_model.pkl', 'rb') as f:
    xgb_model = pickle.load(f)

# Prediction function
def predict(
    Year, Month, Hour, Holiday, Weekday, Workingday, Atemp,
    Humidity, Windspeed, is_peak_hour, is_weekend,
    Season_springer, Season_summer, Season_winter,
    Weathersit_Heavy_Rain, Weathersit_Light_Snow, Weathersit_Mist
):
    input_data = pd.DataFrame([[ 
        Year, Month, Hour, Holiday, Weekday, Workingday, Atemp,
        Humidity, Windspeed, is_peak_hour, is_weekend,
        Season_springer, Season_summer, Season_winter,
        Weathersit_Heavy_Rain, Weathersit_Light_Snow, Weathersit_Mist
    ]], columns=[
        "Year","Month","Hour","Holiday","Weekday","Workingday","Atemp",
        "Humidity","Windspeed","is_peak_hour","is_weekend",
        "Season_springer","Season_summer","Season_winter",
        "Weathersit_Heavy_Rain","Weathersit_Light_Snow","Weathersit_Mist"
    ])

    numeric_features = ["Year","Month","Hour","Weekday","Atemp","Humidity","Windspeed"]
    input_data[numeric_features] = scaler.transform(input_data[numeric_features])

    prediction = xgb_model.predict(input_data.values)
    return int(prediction[0])

# Main Function
def main():
    st.markdown("<h1 style='text-align: center;'>🏍️ Bike Rental Prediction 🏍️</h1>", unsafe_allow_html=True)
    st.write("")

    # Date & Time Features
    st.subheader("📅 Date & Time Features")
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        Year = st.slider("Year", 2011, 2025, 2011)
    with col2:
        Month = st.slider("Month", 1, 12, 1)
    with col3:
        Hour = st.slider("Hour", 0, 23, 12)
    with col4:
        Weekday = st.slider("Weekday (0=Sun,6=Sat)", 0, 6, 0)
    st.write("")

    #Environment Features
    st.subheader("🌤 Weather & Environment")
    col1, col2, col3 = st.columns(3)
    with col1:
        Atemp = st.number_input("Atemp (°C)", value=25.0)
    with col2:
        Humidity = st.number_input("Humidity (%)", value=50.0)
    with col3:
        Windspeed = st.number_input("Windspeed (km/h)", value=10.0)
    st.write("")

    # Compute peak hour & weekend automatically.
    is_peak_hour = 1 if Hour in [7, 8, 9, 17, 18, 19] else 0
    is_weekend = 1 if Weekday in [0, 6] else 0

    # Radio Buttons
    st.subheader("🔘 Holiday, Working Day, Season & Weather")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        Holiday = st.radio("Holiday", ["No", "Yes"])
        Holiday = 1 if Holiday == "Yes" else 0
    with col2:
        Workingday = st.radio("Working Day", ["No", "Yes"])
        Workingday = 1 if Workingday == "Yes" else 0
    with col3:
        season = st.radio("Season", ["Fall", "Springer", "Summer", "Winter"])
        Season_springer = 1 if season == "Springer" else 0
        Season_summer = 1 if season == "Summer" else 0
        Season_winter = 1 if season == "Winter" else 0
    with col4:
        weather = st.radio("Weather", ["Clear", "Mist", "Light Snow", "Heavy Rain"])
        Weathersit_Mist = 1 if weather == "Mist" else 0
        Weathersit_Light_Snow = 1 if weather == "Light Snow" else 0
        Weathersit_Heavy_Rain = 1 if weather == "Heavy Rain" else 0
    st.write("")

    #Predict Button
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 8px 20px;
            border-radius: 6px;
            border: none;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        div.stButton > button:hover {
            background-color: #45a049;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("Predict"):
        result = predict(
            Year, Month, Hour, Holiday, Weekday, Workingday, Atemp,
            Humidity, Windspeed, is_peak_hour, is_weekend,
            Season_springer, Season_summer, Season_winter,
            Weathersit_Heavy_Rain, Weathersit_Light_Snow, Weathersit_Mist
        )
        st.markdown(f"""
            <div style="
                border: 2px solid #4CAF50;
                padding: 10px;
                border-radius: 8px;
                text-align: center;
                background-color: #f0f8ff;
                width: fit-content;
                margin-left: auto;
                margin-right: auto;
            ">
                <h3 style='color:blue; margin:0;'>Predicted Bike Count: {result} 🏍️</h3>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
