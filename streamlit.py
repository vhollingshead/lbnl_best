import streamlit as st
from PIL import Image
import base64

st.set_page_config(layout="wide")

# Set custom background color
st.markdown("""
    <style>
    body, .main, .block-container, header, footer, .stSidebar {
        background-color: #1d392b !important;
    }
    </style>
""", unsafe_allow_html=True)


# Load and encode image
with open("best.png", "rb") as img_file:
    encoded = base64.b64encode(img_file.read()).decode()

# Background image container with no padding
if st.session_state.get("page") != "Get Started":
    st.markdown(f"""
        <div style="
            background-image: url('data:image/png;base64,{encoded}');
            background-size: cover;
            background-position: center;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;">
        </div>
    """, unsafe_allow_html=True)

# Simulated overlay using centered column
col1, col2, col3 = st.columns([3, 1, 3])
with col2:
    if st.button("Get Started"):
        st.session_state.page = "Get Started"
        st.rerun()

# Page routing
def get_started():
    st.title("Get Started")
    st.write("Follow these steps to begin your journey...")

if st.session_state.get("page") == "Get Started":
    get_started()