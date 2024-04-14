import streamlit as st 
from openai import OpenAI

client = OpenAI(api_key="my-open-api-key") 

def get_air_quality_suggestions(city, state, option):
      completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are an environmentalist looking to give the user solutions to improve the air quality in their local area. Given the user's {city}, {state}, and chosen categorical {option} between transportation solutions, industrial / energy solutions, and urban planning / green spaces, provide five in-depth solutions specific to the inputs. Use reliable articles, sources, and data to generate your answers."},
            {"role": "user", "content": city},
            {"role": "user", "content": state},
            {"role": "user", "content": option},
        ]
      )
      return completion.choices[0].message.content


# Streamlit App
with st.form(key = "chat"):

    st.title('Air Quality Improvement Suggestions')

    city = st.text_input('City')
    state = st.text_input('State')

    option = st.selectbox (
        "Select one of the following categorical solutions:",
        ("Transportation Solutions", "Industrial / Energy Solutions" , "Urban Planning / Green Spaces")
    )

    submit_selections = st.form_submit_button("Submit")


    if submit_selections:
        if city and state and option:
            suggestions = get_air_quality_suggestions(city, state, option)
            st.subheader('Solutions:')
            st.write(suggestions)
            

            # st.text_input("Choose your category.")
        else:
            st.error('Please enter both city and state!')
