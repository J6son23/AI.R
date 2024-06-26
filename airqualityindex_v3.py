import streamlit as st
import requests
from openai import OpenAI

client = OpenAI(api_key="my-open-api-key") 

def fetch_air_quality_data(city):
    try:
        url = f"https://api.airvisual.com/v2/city?city={city}&state=California&country=USA&key=my-aqi-key"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            st.error("Failed to fetch air quality data. Please try again.")
            return None
    except Exception as e:
        st.error(f"Error occurred: {e}")
        return None
    
with st.form(key = "chat"):

    menu_selection = st.sidebar.selectbox(
        "Choose an option!",
        ("Air Quality Index", "Air Quality Solutions", "Public Transit Route")
    )

def get_pollution_level(aqi):
    if aqi <= 50:
        return "Good"
    elif 51 <= aqi <= 100:
        return "Moderate"
    elif 101 <= aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif 151 <= aqi <= 200:
        return "Unhealthy"
    elif 201 <= aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

def display_air_quality(selected_city):
    data = fetch_air_quality_data(selected_city)
    if data:
        try:
            aqi = data["data"]["current"]["pollution"]["aqius"]
            pollution_level = get_pollution_level(aqi)
            st.write(f"The current AQI in {selected_city} is: **{aqi}**")
            st.write(f"Air Pollution Level: **{pollution_level}**")
        except KeyError:
            st.error(f"Failed to parse air quality data for {selected_city}.")
    else:
        st.error("Failed to fetch air quality data. Please try again.")

if menu_selection == "Air Quality Index":
    st.title("Real-time Air Quality Index Comparison 🌬️")

    cities = ["San Jose", "Los Angeles", "San Francisco", "Sacramento", "Fresno"]
    selected_city = st.selectbox("Select a city to fetch air quality data:", cities)

    if st.button("Fetch Air Quality"):
        display_air_quality(selected_city)

    selected_cities = st.multiselect("Select cities to compare:", cities, default=cities[:2])

    if st.button("Compare Air Quality"):
        st.write("City | AQI | Pollution Level")
        for city in selected_cities:
            data = fetch_air_quality_data(city)
            if data:
                try:
                    aqi = data["data"]["current"]["pollution"]["aqius"]
                    pollution_level = get_pollution_level(aqi)
                    st.write(f"{city} | {aqi} | {pollution_level}")
                except KeyError:
                    st.error(f"Failed to parse air quality data for {city}.")
            else:
                st.error(f"No data available for {city}.")

main()
