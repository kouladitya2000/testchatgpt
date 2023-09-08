import os
import openai
from secret_key import openapi_key
import streamlit as st

# Set up OpenAI API credentials
os.environ['OPENAI_API_KEY'] = openapi_key
os.environ['OPENAI_API_BASE'] = "https://htioaiservice.openai.azure.com/"
os.environ['OPENAI_API_VERSION'] = "2023-5-15"

openai.api_type = "azure"
openai.api_base = "https://htioaiservice.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_restaurant_info(input1):
    response = openai.Completion.create(
        engine="restaurant",
        prompt=input1,
        temperature=1,
        max_tokens=100,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=None)

    return response.choices[0].text.strip()

def main():
    st.title("Dev GPT")
    user_input = st.text_input("Write your query...", "input goes here")
    if st.button("Generate"):
        restaurant_info = generate_restaurant_info(user_input)
        st.write(restaurant_info)

if __name__ == "__main__":
    main()
