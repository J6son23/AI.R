import os
import openai
import streamlit as st
import requests
from openai import OpenAI

client = OpenAI(api_key='my-api-key-here')

def fetch_air_quality_data(city):
    try:
        url = f"https://api.airvisual.com/v2/city?city={city}&state=California&country=USA&key=c415eb39-eed4-4363-bef2-a7dff7be5ee5"
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


def main():
    st.write("Enter your city to check the air quality index:")

    city = st.text_input("Enter city name:", "San Jose")

    if st.button("Check Air Quality"):
        with st.spinner("Fetching air quality data..."):
            data = fetch_air_quality_data(city)
        
        if data:
          
            aqi = data["data"]["current"]["pollution"]["aqius"]
            main_pollutant = data["data"]["current"]["pollution"]["mainus"]

            st.write(f"Air Quality Index (AQI): {aqi}")
            st.write(f"Main Pollutant: {main_pollutant}")

st.markdown("# Real-time Air Quality Index 🌬️")
st.sidebar.markdown("# Real-time Air Quality Index 🌬️")

main()

