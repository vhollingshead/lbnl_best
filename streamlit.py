import streamlit as st
from PIL import Image
import base64

# Use Streamlit's built-in page routing
st.set_page_config(layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("", ["About Us", "Methodology", "Get Started"])

# Function to display homepage with background and button
def display_home():
    # Load image from local file
    image_path = "placeholder_image.png"  
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    # Background image styling via CSS
    st.markdown(f"""
        <style>
        .background {{
            background-image: url("data:image/jpg;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
        }}
        .overlay-text {{
            font-size: 3em;
            color: white;
            font-weight: bold;
            text-align: center;
            margin-top: 200px;
        }}
        </style>
        <div class="background"></div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='overlay-text'>Sample Text</div>", unsafe_allow_html=True)

    # Centered button
    col1, col2, col3 = st.columns([3, 1, 3])
    with col2:
        if st.button("Get Started"):
            st.session_state.page = "Get Started"

# Navigation logic using session state
if "page" not in st.session_state:
    st.session_state.page = page

if st.session_state.page == "About Us":
    st.title("About Us")
    st.write("Welcome to our decarbonization journey platform. Here we aim to support...")

elif st.session_state.page == "Methodology":
    st.title("Methodology")
    st.write("We use advanced analytics, stakeholder engagement, and policy modeling to...")

elif st.session_state.page == "Get Started":
    st.title("Get Started")
    st.write("Follow these steps to begin your journey...")

else:
    display_home()

# Allow direct navigation via button
if page != st.session_state.page:
    st.session_state.page = page
    st.experimental_rerun()
