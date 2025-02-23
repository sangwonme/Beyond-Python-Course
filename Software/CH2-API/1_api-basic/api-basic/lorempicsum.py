import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("Random Image Viewer from Lorem Picsum")

if 'url' not in st.session_state:
    st.session_state['url'] = 'https://picsum.photos/1280/720'

# User inputs for image customization
st.sidebar.subheader("Customize Your Image")
width = st.sidebar.number_input("Width", min_value=100, max_value=1920, value=500)
height = st.sidebar.number_input("Height", min_value=100, max_value=1080, value=500)
grayscale = st.sidebar.checkbox("Grayscale")
blur = st.sidebar.checkbox("Blur")

# Constructing the API URL based on user input
# TODO: update_url

# Fetching and displaying the image
if st.sidebar.button("Fetch Image"):
    # TODO
    response = requests.get(st.session_state['url'])
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        st.image(image, caption="Random Image from Lorem Picsum")
    else:
        st.error("Failed to fetch image. Please check the settings and try again.")

st.write("Adjust the settings in the sidebar to customize the image.")
