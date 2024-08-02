from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="gemini")  # Keep this call

st.title("Image Processing App")

def get_gemini_response(input ,image,prompt):
    model= genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input,image[0],prompt])
    return response.text


def input_image_setup(upload_file):
    if upload_file is not None:
        bytes_data = upload_file.getvalue()

        image_parts = [
            {
                "mime_type" : upload_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no  file")
    

# st.set_page_config(page_title="gemini ")

input =st.text_input("input",key = "input")
uploaded_file= st.file_uploader("choose the image" ,type = ['jpg','jpeg','png'])
image= ""

if uploaded_file is not None:
    image= Image.open(uploaded_file)
    st.image(image,caption='uploaded immage',use_column_width=True)



submit = st.button("tell me about the image")

input_prompt = """
Use the Google Generative AI Gemini model to analyze the image and extract information about the following:
Objects present in the image
Actions being performed by the individuals in the image
Contextual information about the scene (e.g., location, time of day)
Based on the extracted information, generate a detailed summary of the image content, including:
A list of objects and their descriptions
A description of the actions being performed
An analysis of the scene context
Use a formal and informative tone in the generated summary.
"""

if submit:
    image_parts = input_image_setup(uploaded_file)
    response = get_gemini_response(input, image_parts, input_prompt)
    st.write(response)