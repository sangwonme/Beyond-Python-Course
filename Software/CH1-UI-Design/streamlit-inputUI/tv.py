import streamlit as st

# Title of the application
st.title('Input UI')

# # Button

if st.button('Plus', type='primary'):
    st.write(10)
else:
    st.write(0)

# # Checkbox
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

# # Toggle
cctv = st.toggle('CCTV')
tv = st.toggle('TV')
ac = st.toggle('AC')
light = st.toggle('LIGHT')
st.write('Switch ON: ')
if cctv:
    st.write('CCTV is on')
if tv:
    st.write('TV is on')
if ac:
    st.write('AC is on')
if light:
    st.write('LIGHT is on')

# # Select Box
option = st.selectbox(
    'How would you like to be contacted?',
    ['Email', 'Home phone', 'Mobile phone'])

st.write('You selected:', option)

# # Multiselect
price = {
    'apple': 30,
    'banana': 20,
    'grape': 50
}
options = st.multiselect(
    'What fruits do you want to buy?',
    ['apple', 'banana', 'grape'],
)

total = 0
for fruit in options:
    total += price[fruit]
st.write('Price: ', total)

# Slider
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Text Input
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

# Number Input
number = st.number_input('Insert a number')
st.write('The current number is ', number)