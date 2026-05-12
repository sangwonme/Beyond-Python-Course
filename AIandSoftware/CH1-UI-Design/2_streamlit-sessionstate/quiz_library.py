import streamlit as st

st.title("My Personal Library Manager")

# Initialize an empty list to store books
if 'library' not in st.session_state:
    st.session_state['library'] = []

# TODO: add_book 

# TODO: remove_book

# TODO: search_book

# TODO: display_library
def display_library():
    print(st.session_state['library'])


with st.form("Library Form"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=1000, max_value=9999, step=1, format="%d")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        pass
        # TODO: call add_book

if st.button("Display Library"):
    pass
    # TODO: call display_library()

search = st.text_input("Search Book by Title")
if st.button("Search"):
    pass
    # TODO: call search_book()

remove = st.text_input("Remove Book by Title")
if st.button("Remove Book"):
    pass
    # TODO: remove_book()