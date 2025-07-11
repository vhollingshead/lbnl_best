import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64

# Use Streamlit's built-in page routing
st.set_page_config(layout="wide")

def about_us():
    # Header Section
    st.title("About Us")
    st.write("This is the about us page.")

def methodology():
    st.title("Methodology")
    st.write("This is the methodology page.")

def get_started():
    st.title("Get Started")
    st.write("This is the get started page.")



def main():
    with st.sidebar:
        selected = option_menu(
            "Navigation",
            ["About Us", "Methodology", "Get Started"],
            icons=["house", "graph-up-arrow", "clipboard-data", "lightbulb", "info-circle"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#f0f2f6"},
                "icon": {"color": "black", "font-size": "18px"},
                "nav-title": {  # This controls the "Navigation" label style
                    "color": "black",
                    "font-size": "18px",
                    "font-weight": "bold",
                    "text-align": "left"
                },
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
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

    # Navigate to the selected page
    if selected == "About Us":
        about_us()
    elif selected == "Methodology":
        methodology()
    elif selected == "Get Started":
        get_started()

if __name__ == "__main__":
    main()

######



# # Sidebar Navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("", ["About Us", "Methodology", "Get Started"])

# # Function to display homepage with background and button
# def display_home():
#     # Load image from local file
#     image_path = "placeholder_image.png"  
#     with open(image_path, "rb") as image_file:
#         encoded_image = base64.b64encode(image_file.read()).decode()

#     # Background image styling via CSS
#     st.markdown(f"""
#         <style>
#         .background {{
#             background-image: url("data:image/jpg;base64,{encoded_image}");
#             background-size: cover;
#             background-position: center;
#             position: absolute;
#             top: 0;
#             left: 0;
#             width: 100%;
#             height: 100%;
#             z-index: -1;
#         }}
#         .overlay-text {{
#             font-size: 3em;
#             color: white;
#             font-weight: bold;
#             text-align: center;
#             margin-top: 200px;
#         }}
#         </style>
#         <div class="background"></div>
#     """, unsafe_allow_html=True)

#     st.markdown("<div class='overlay-text'>Sample Text</div>", unsafe_allow_html=True)

#     # Centered button
#     col1, col2, col3 = st.columns([3, 1, 3])
#     with col2:
#         if st.button("Get Started"):
#             st.session_state.page = "Get Started"

# # Navigation logic using session state
# if "page" not in st.session_state:
#     st.session_state.page = page

# if st.session_state.page == "About Us":
#     st.title("About Us")
#     st.write("Welcome to our decarbonization journey platform. Here we aim to support...")

# elif st.session_state.page == "Methodology":
#     st.title("Methodology")
#     st.write("We use advanced analytics, stakeholder engagement, and policy modeling to...")

# elif st.session_state.page == "Get Started":
#     st.title("Get Started")
#     st.write("Follow these steps to begin your journey...")

# else:
#     display_home()

# # Allow direct navigation via button
# if page != st.session_state.page:
#     st.session_state.page = page
#     st.experimental_rerun()
