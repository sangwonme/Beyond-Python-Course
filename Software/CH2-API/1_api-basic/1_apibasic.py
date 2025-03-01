import streamlit as st

import requests
from PIL import Image
from io import BytesIO

st.title("Lorem Picsum Test")

# URL session state
if 'url' not in st.session_state:
    st.session_state['url'] = 'https://picsum.photos/1280/720'

# Fetching and displaying the image
if st.button("Fetch Image"):
    response = requests.get(st.session_state['url'])
    with st.expander("Result"):
      st.write("Response status code: ", response.status_code)
      st.write("Response content: ", response.content)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        st.image(image)
    else:
        st.error("Failed to fetch image. Please check the settings and try again.")
