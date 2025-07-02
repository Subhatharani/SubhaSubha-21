import streamlit as st
from PIL import Image
from model import generate_image

st.set_page_config(page_title="Text-to-Image Generator", layout="centered")
st.title("🖼 Text-to-Image Generator")
st.markdown("Enter a text prompt to generate an image using Stable Diffusion.")

prompt = st.text_input("Text Prompt")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating... Please wait."):
            filepath = generate_image(prompt)
            image = Image.open(filepath)
            st.image(image, caption="Generated Image")
            st.success("Done!")
    else:
        st.warning("Please enter a prompt to generate an image.")
