import streamlit as st
from PIL import Image
import os
import pathlib
import textwrap

from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

def get_gemini_response(input, image):
    model = genai.GenerativeModel('models/gemini-3-flash-preview')
    
    if input !="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content([image])
        
    return response.text

st.set_page_config(page_title="Gemini-3-Flash Image Captioning", page_icon=":robot_face:")

st.header("🤖 Gemini-3-Flash Image Captioning")
input = st.text_input('Input prompt: ', key = 'input')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

uploaded_image = "" 
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
submit = st.button('Generate response about Image using Gemini-3-LLM')

if submit:
    response =get_gemini_response(input, image)
    st.subheader("Gemini-3 LLM response: ")
    st.write(response)