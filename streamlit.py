import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

image = Image.open("best.png")
st.image(image, use_column_width=True)

def get_started():
    st.title("Get Started")
    st.write("Follow these steps to begin your journey...")


if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    col1, col2, col3 = st.columns([3, 1, 3])
    with col2:
        if st.button("Get Started"):
            st.session_state.page = "Get Started"
            st.rerun()

# Show Get Started content
if st.session_state.page == "Get Started":
    get_started()



# import streamlit as st
# from streamlit_option_menu import option_menu
# import base64

# st.set_page_config(layout="wide")

# def about_us():
#     st.title("About Us")
#     st.write("Welcome to our decarbonization journey platform. Here we aim to support...")

# def methodology():
#     st.title("Methodology")
#     st.write("We use advanced analytics, stakeholder engagement, and policy modeling to...")

# def get_started():
#     st.title("Get Started")
#     st.write("Follow these steps to begin your journey...")

# def home():
#     image_path = "placeholder_image.png"
#     with open(image_path, "rb") as image_file:
#         encoded_image = base64.b64encode(image_file.read()).decode()

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

#     col1, col2, col3 = st.columns([3, 1, 3])
#     with col2:
#         if st.button("Get Started"):
#             st.session_state.page = "Get Started"
#             st.rerun()

# def main():
#     # Display a banner image above the navigation menu
#     banner_image_path = "banner_placeholder.png"
#     with open(banner_image_path, "rb") as image_file:
#         encoded_banner = base64.b64encode(image_file.read()).decode()

#     st.markdown(f"""
#         <div style='text-align: center; padding-bottom: 10px;'>
#             <img src='data:image/png;base64,{encoded_banner}' style='width: 100%; height: auto;'>
#         </div>
#     """, unsafe_allow_html=True)

#     if "page" not in st.session_state:
#         st.session_state.page = "Home"

#     selected = option_menu(
#         menu_title=None,
#         options=["Home", "About Us", "Methodology", "Get Started"],
#         icons=["house", "info-circle", "graph-up-arrow", "clipboard-data"],
#         orientation="horizontal",
#         default_index=["Home", "About Us", "Methodology", "Get Started"].index(st.session_state.page),
#     )

#     # Only update session state if selection has changed
#     if selected != st.session_state.page:
#         st.session_state.page = selected
#         st.rerun()

#     # Render the selected page
#     if st.session_state.page == "Home":
#         home()
#     elif st.session_state.page == "About Us":
#         about_us()
#     elif st.session_state.page == "Methodology":
#         methodology()
#     elif st.session_state.page == "Get Started":
#         get_started()

# if __name__ == "__main__":
#     main()
