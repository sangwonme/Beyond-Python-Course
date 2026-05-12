import streamlit as st
import pandas as pd

st.title("📦 Inventory Check System")

# ----------------------------------
# (1) Load Data
# ----------------------------------
with st.expander("1️⃣ Load Data"):
    st.write("Load inventory data from CSV file.")

    # Load CSV file into DataFrame
    
    df = pd.read_csv('./data/data.csv')

    if df is None:
        st.warning("No data.")
    else:
        st.write(df)

# ----------------------------------
# (2) Indexing
# ----------------------------------
with st.expander("2️⃣ Indexing"):
    st.write("Select rows and columns to display.")

    if df is None:
        st.warning("No data.")
    else:
        # UI: column multiselect
        selected_columns = st.multiselect(
            "Select columns",
            options=df.columns.tolist(),
            default=df.columns.tolist()
        )

        # UI: row range slider
        row_range = st.slider(
            "Select row range",
            min_value=0,
            max_value=len(df) - 1,
            value=(0, len(df) - 1)
        )

        # Index DataFrame using loc
        selected_df = df.loc[
            row_range[0]:row_range[1],
            selected_columns
        ]

        st.write(selected_df)

# ----------------------------------
# (3) Insert New Row
# ----------------------------------
with st.expander("3️⃣ Insert New Row"):
    st.write("Add a new item to the inventory.")

    if df is None:
        st.warning("No data.")
    else:
        # Input fields for each column
        product = st.text_input("Product")
        price = st.number_input("Price", min_value=0)
        category = st.text_input("Category")
        stock = st.number_input("Stock", min_value=0)

        if st.button("Add Data"):
            # Safely insert a new row using dict
            df.loc[len(df)] = {
                'Product': product,
                'Price': price,
                'Category': category,
                'Stock': stock
            }

        st.write(df)
