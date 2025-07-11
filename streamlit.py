
import streamlit as st
import pandas as pd

st.title("Streamlit Web App")

rows, cols = 3, 3
input_grid = []

st.write("Enter numbers (or upload a CSV):")

uploaded = st.file_uploader("Upload CSV", type="csv", label_visibility="collapsed")
csv_data = None
if uploaded:
    try:
        csv_data = pd.read_csv(uploaded).values.tolist()
    except:
        st.error("Invalid CSV format.")

for i in range(rows):
    cols_data = []
    cols_container = st.columns(cols)
    for j in range(cols):
        default_val = ""
        if csv_data and i < len(csv_data) and j < len(csv_data[i]):
            default_val = str(csv_data[i][j])
        val = cols_container[j].text_input(f"R{i}C{j}", value=default_val, label_visibility="collapsed")
        cols_data.append(val)
    input_grid.append(cols_data)

if st.button("Next"):
    st.write("Values entered:")
    st.write(input_grid)
