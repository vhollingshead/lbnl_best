import streamlit as st
from streamlit_option_menu import option_menu
import base64

st.set_page_config(layout="wide")

def about_us():
    st.title("About Us")
    st.write("Welcome to our decarbonization journey platform. Here we aim to support...")

def methodology():
    st.title("Methodology")
    st.write("We use advanced analytics, stakeholder engagement, and policy modeling to...")

def get_started():
    st.title("Get Started")
    st.write("Follow these steps to begin your journey...")

def home():
    image_path = "placeholder_image.png"
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

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

    col1, col2, col3 = st.columns([3, 1, 3])
    with col2:
        if st.button("Get Started"):
            st.session_state.page = "Get Started"



def main():
    if "page" not in st.session_state:
        st.session_state.page = "Home"
    if st.session_state.page == "Get Started":
        get_started()
        return
    
    # Display a banner image above the navigation menu
    banner_image_path = "placeholder_image.png"
    with open(banner_image_path, "rb") as image_file:
        encoded_banner = base64.b64encode(image_file.read()).decode() 

        st.markdown(f"""
        <div style='text-align: center; padding-bottom: 10px;'>
        <img src='data:image/png;base64,{encoded_banner}' style='width: 100%; height: auto;'>
        </div>
        """, unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us", "Methodology", "Get Started"],
        icons=["house", "info-circle", "graph-up-arrow", "clipboard-data"],
        orientation="horizontal",
        default_index=["Home", "About Us", "Methodology", "Get Started"].index(st.session_state.page),
        styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"},
            "icon": {"color": "black", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "color": "black",
                "background-color": "#e0e0e0"
            },
            "nav-link-selected": {
                "background-color": "#4F7849",
                "color": "white"
            }
        }
    )

    st.session_state.page = selected

    if selected == "Home":
        home()
    elif selected == "About Us":
        about_us()
    elif selected == "Methodology":
        methodology()
    elif selected == "Get Started":
        get_started()

if __name__ == "__main__":
    main()
