import streamlit as st

# Sidebar with a selectbox and radio button
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

# Main content area
st.title("Customer Contact and Shipping Preferences")

st.header("Shipping Information")
st.write(f"Selected shipping method: **{add_radio}**")
st.write("Thank you for using our service!")
