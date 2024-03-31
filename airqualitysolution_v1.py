import streamlit as st 
from openai import OpenAI

client = OpenAI(api_key="my-open-ai-key") 

def get_air_quality_suggestions(city, state):
      completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
        messages = [
            {"role": "system", "content": "You are an environmentalist looking to find solution to reduce air quality in a local city. Given the {city} and {state}, provide the user 5 simple solutions in numbered formatting on how to help improve the air quality in their geographic area."},
            {"role": "user", "content": city}
        ]
      )
      return completion.choices[0].message.content


# Streamlit App
with st.form(key = "chat"):
    st.title('Air Quality Improvement Suggestions')
    st.write('Enter your city and state to get suggestions for improving air quality.')

    city = st.text_input('City')
    state = st.text_input('State')

    submitted = st.form_submit_button("Submit")

    if submitted:
        if city and state:
            suggestions = get_air_quality_suggestions(city, state)
            st.subheader('Solutions:')
            st.write(suggestions)
        else:
            st.error('Please enter both city and state!')
