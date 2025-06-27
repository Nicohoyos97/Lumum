import streamlit as st
import pandas as pd

# Load data (same structure as the cleaned table you provided)
data = [
    {"Section": "Bathroom", "Size": "Half", "Price": 50},
    {"Section": "Bathroom", "Size": "Full", "Price": 95},
    {"Section": "Bathroom", "Size": "Master", "Price": 120},
    {"Section": "Bedroom", "Size": "Regular", "Price": 40},
    {"Section": "Bedroom", "Size": "Large", "Price": 60},
    {"Section": "Kitchen", "Size": "Basic", "Price": 70},
    {"Section": "Kitchen", "Size": "+Oven", "Price": 30},
    {"Section": "Kitchen", "Size": "+Microwave", "Price": 20},
    {"Section": "Living Room", "Size": "Standard", "Price": 70},
    {"Section": "Living Room", "Size": "Large", "Price": 120},
]
df = pd.DataFrame(data)

# Initialize session state for cart
if 'cart' not in st.session_state:
    st.session_state.cart = []

st.title("Cleaning Quote Calculator")
st.write("Select the areas and sizes to generate a cleaning quote in real time.")

# Section selector
section = st.selectbox("Choose a section", df['Section'].unique())

# Filter sizes for selected section
available_sizes = df[df['Section'] == section]['Size'].unique()
size = st.selectbox("Choose a size", available_sizes)

# Get price
price = df[(df['Section'] == section) & (df['Size'] == size)]['Price'].values[0]
st.markdown(f"### Price: ${price}")

# Add to quote
if st.button("Add to Quote"):
    st.session_state.cart.append({"Section": section, "Size": size, "Price": price})

# Display cart
if st.session_state.cart:
    st.subheader("Current Quote")
    quote_df = pd.DataFrame(st.session_state.cart)
    st.table(quote_df)
    total = sum(item['Price'] for item in st.session_state.cart)
    st.markdown(f"## Total: ${total}")

# Option to reset cart
if st.button("Reset Quote"):
    st.session_state.cart = []
