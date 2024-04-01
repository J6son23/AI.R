from openai import OpenAI
import streamlit as st 

client = OpenAI(api_key = "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")

def get_directions(prompt, model = "gpt-3.5-turbo"):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "You will be provided 2 addresses, one of the user's current location and one of the destination they wish to go to. Your task is to create a step-by-step instruction on how to get to the destination using public transit."
        },
        {
        "role": "user",
        "content": prompt
        }
    ],
    temperature=0.3,
    max_tokens=64,
    top_p=1
)
    return response.choices[0].message.content

with st.form(key = "chat"):
    location1 = st.text_input("Input address 1")
    location2 = st.text_input("Input address 2")
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(get_directions(location1, location2)) 