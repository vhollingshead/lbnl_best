# import streamlit as st
# from PIL import Image
# import base64
# import pandas as pd

# st.set_page_config(layout="wide")

# # Set custom background color
# # st.markdown("""
# #     <style>
# #     body, .main, .block-container, header, footer, .stSidebar {
# #         background-color: #1d392b !important;
# #     }
# #     </style>
# # """, unsafe_allow_html=True)

# # Load and encode image
# with open("best.png", "rb") as img_file:
#     encoded = base64.b64encode(img_file.read()).decode()

# with open("green_tree.png", "rb") as img_file:
#     encoded_tree = base64.b64encode(img_file.read()).decode()

# with open("landingpage_title.png", "rb") as img_file:
#     encoded_title = base64.b64encode(img_file.read()).decode()

# def home():
#     left, right = st.columns([1, 1])

#     # Left image
#     with left:
#         st.image("green_tree.png", use_column_width=True)

#     # Right text content
#     with right:
#         st.markdown("""
#             <h1 style='font-size: 3.5em; color: #103b20;'>
#                 Benchmarking<br>& Energy<br>Savings Tool
#             </h1>
#             <p style='font-size: 1.2em; color: #1d392b;'>
#                 The Benchmarking and Energy Savings Tool (BEST) Cement is a process-based tool based on commercially available<br>
#                 efficiency technologies used anywhere in the world applicable to the cement industry.
#             </p>
#         """, unsafe_allow_html=True)

#         center_col = st.columns([3, 1, 3])[1]
#         with center_col:
#             st.markdown("""
#                 <style>
#                 .stButton>button {
#                     background-color: #4CAF50;
#                     color: white;
#                     padding: 10px 24px;
#                     font-size: 16px;
#                     border: none;
#                     border-radius: 5px;
#                 }
#                 </style>
#             """, unsafe_allow_html=True)
#             if st.button("Get Started"):
#                 st.session_state.page = "Get Started"
#                 st.rerun()

# # def home():
# #     # Background image container with no padding
# #     col1, col2 = st.columns([5, 7])
# #     with col1:
# #         st.markdown(f"""
# #             <div style="
# #                 background-image: url('data:image/png;base64,{encoded_tree}');
# #                 background-size: cover;
# #                 background-position: center;
# #                 height: 125vh;
# #                 display: flex;
# #                 flex-direction: column;
# #                 justify-content: center;
# #                 align-items: center;">
# #             </div>
# #         """, unsafe_allow_html=True)

# #     with col2:
# #         st.markdown(f"""
# #             <div style="text-align: center; padding-top: 5vh;">
# #                 <img src="data:image/png;base64,{encoded_title}" style="max-width: 100%; height: auto;" />
# #                 <br><br>
# #             </div>
# #         """, unsafe_allow_html=True)

# #         # Streamlit button alternative (if desired)
# #         center_col = st.columns([4, 2, 4])[1]
# #         with center_col:
# #             st.markdown("""
# #                 <style>
# #                 .stButton>button {
# #                     background-color: #4CAF50;
# #                     color: white;
# #                     border: none;
# #                     padding: 10px 24px;
# #                     font-size: 16px;
# #                     border-radius: 5px;
# #                 }
# #                 </style>
# #             """, unsafe_allow_html=True)
# #             if st.button("Get Started"):
# #                 st.session_state.page = "Get Started"
# #                 st.rerun()

# def get_started():
#     st.title("Production Input Sheet 1 - Raw Materials and Clinker Production")
#     st.subheader("Raw materials")
#     st.write("1. Amount of limestone used. Enter annual amount of limestone in tonnes of material.")
#     st.write("2. Quantity of additives used. For each additive, enter annual amount in tonnes. If additives other than those listed are used, enter the additive type in the “other 1” or “other 2” box and its amount.")
#     st.write("3. Enter the amount of materials that are preblended, crushed, dried and ground. User may use default values (where provided) or may enter his/her own data if available.")

#     # Input fields
#     limestone = st.number_input("Limestone used (tonnes)", min_value=0.0, step=100.0, format="%e")
#     clay = st.number_input("Clay used (tonnes)", min_value=0.0, step=10.0, format="%e")
#     default_iron_ore = 9.0
#     iron_ore = st.number_input("Iron Ore used (tonnes)", min_value=0.0, step=10.0, format="%e", value=default_iron_ore, key="iron_ore")
#     st.markdown("""
#         <style>
#         div[data-testid="stNumberInput"]:has(input[aria-label='Iron Ore used (tonnes)']) input {
#             background-color: #d5f7dc !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)
    
#     default_fly_ash = 9.0
#     fly_ash = st.number_input("Fly Ash used (tonnes)", min_value=0.0, step=10.0, format="%e", value=default_fly_ash, key="fly_ash")
#     st.markdown("""
#         <style>
#         div[data-testid="stNumberInput"]:has(input[aria-label='Fly Ash used (tonnes)']) input {
#             background-color: #d5f7dc !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)
    
#     other1_type = st.text_input("Other 1 - Additive Type")
#     other1_amount = st.number_input("Other 1 - Amount (tonnes)", min_value=0.0, step=10.0, format="%e")
#     other2_type = st.text_input("Other 2 - Additive Type")
#     other2_amount = st.number_input("Other 2 - Amount (tonnes)", min_value=0.0, step=10.0, format="%e")

#     # Store inputs in temporary DataFrame
#     st.session_state.raw_materials_df = {
#         "Limestone": limestone,
#         "Clay": clay,
#         "Iron Ore": iron_ore,
#         "Fly Ash": fly_ash,
#         f"Other 1 - {other1_type}": other1_amount,
#         f"Other 2 - {other2_type}": other2_amount
#     }

#     # Display preview
#     st.subheader("Preview of Entered Data")
#     st.write(st.session_state.raw_materials_df)

#     # Next button to go to Energy Input Sheet
#     if st.button("Next: Energy Input Sheet"):
#         st.session_state.page = "Energy Input Sheet"
#         st.rerun()

# def graph_1():
#     raw_df = st.session_state.get("raw_materials_df", {})

#     # Extract relevant raw material values
#     material_keys = ["Limestone", "Clay", "Iron Ore", "Fly Ash"]
#     other_keys = [k for k in raw_df.keys() if k.startswith("Other")]
#     total = sum([raw_df.get(k, 0) for k in material_keys + other_keys if isinstance(raw_df.get(k, 0), (int, float))])
#     slice_value = total * 0.25

#     # Display pie chart
#     st.subheader("Graph 1: 25% of Total Raw Materials")
#     st.plotly_chart(
#         {
#             "data": [{
#                 "labels": ["25% Slice", "Remaining 75%"],
#                 "values": [slice_value, total - slice_value],
#                 "type": "pie"
#             }],
#             "layout": {"margin": {"t": 0, "b": 0}}
#         },
#         use_container_width=True
#     )

# def graph_2():
#     raw_df = st.session_state.get("raw_materials_df", {})

#     # Filter relevant fields
#     material_names = ["Limestone", "Clay", "Iron Ore", "Fly Ash"]
#     other_names = [k for k in raw_df.keys() if k.startswith("Other")]
#     data = {k: raw_df[k] for k in material_names + other_names if isinstance(raw_df.get(k), (int, float))}

#     if data:
#         st.subheader("Graph 2: Raw Material Usage (Bar Chart)")
#         df = pd.DataFrame.from_dict(data, orient='index', columns=['Tonnes'])
#         st.bar_chart(df)


# def graph_3():
#     raw_df = st.session_state.get("raw_materials_df", {})
#     energy_df = st.session_state.get("energy_inputs_df")

#     # Total all numeric values from both sources
#     raw_total = sum([v for v in raw_df.values() if isinstance(v, (int, float))])

#     try:
#         energy_total = energy_df.apply(pd.to_numeric, errors='coerce').fillna(0).values.sum()
#     except:
#         energy_total = 0

#     combined_total = raw_total + energy_total
#     slice_value = combined_total * 0.8

#     st.subheader("Graph 3: 80% of Combined Inputs (Raw + Energy)")
#     st.plotly_chart(
#         {
#             "data": [{
#                 "labels": ["80% Slice", "Remaining 20%"],
#                 "values": [slice_value, combined_total - slice_value],
#                 "type": "pie"
#             }],
#             "layout": {"margin": {"t": 0, "b": 0}}
#         },
#         use_container_width=True
#     )

# def energy_input_sheet():
#     st.title("Energy Input Sheet title")
#     st.subheader("Energy Inputs Table")

#     # columns = [f"Step_{i+1}" for i in range(6)]
#     # index = ["Electricity_Use", "Fuel_Use"]
#     # default_data = [["" for _ in columns] for _ in index]
#     # df = pd.DataFrame(default_data, index=index, columns=columns)

#     # edited_df = st.data_editor(df, num_rows="fixed", use_container_width=True)

#     # # Save for later use
#     # st.session_state.energy_inputs_df = edited_df

#     # # Upload CSV or XLSX file to populate table
#     # st.subheader("Upload Energy Inputs from File")
#     # uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

#     # if uploaded_file:
#     #     try:
#     #         if uploaded_file.name.endswith(".csv"):
#     #             uploaded_df = pd.read_csv(uploaded_file, index_col=0)
#     #         else:
#     #             uploaded_df = pd.read_excel(uploaded_file, index_col=0)

#     #         # Display uploaded and overwrite table if structure matches
#     #         if list(uploaded_df.columns) == columns and list(uploaded_df.index) == index:
#     #             st.session_state.energy_inputs_df = uploaded_df
#     #             st.success("Uploaded data successfully loaded into the table.")
#     #         else:
#     #             st.error("Uploaded file structure does not match expected format.")
#     #     except Exception as e:
#     #         st.error(f"Error reading file: {e}")

#     # # Generate Report button
#     # if st.button("Generate Report"):
#     #     import matplotlib.pyplot as plt
#     #     from fpdf import FPDF
#     #     import tempfile
#     #     import os

#     #     # Create plots for graphs and save as PNGs
#     #     def save_graph_as_png(fig, filename):
#     #         with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
#     #             fig.savefig(tmpfile.name, bbox_inches='tight')
#     #             tmpfile.close()
#     #             os.rename(tmpfile.name, filename)

#     #     raw_df = st.session_state.get("raw_materials_df", {})
#     #     material_keys = ["Limestone", "Clay", "Iron Ore", "Fly Ash"]
#     #     other_keys = [k for k in raw_df.keys() if k.startswith("Other")]
#     #     total = sum([raw_df.get(k, 0) for k in material_keys + other_keys if isinstance(raw_df.get(k, 0), (int, float))])
#     #     slice_value = total * 0.25

#     #     fig1, ax1 = plt.subplots()
#     #     ax1.pie([slice_value, total - slice_value], labels=["25% Slice", "Remaining 75%"], autopct='%1.1f%%')
#     #     ax1.set_title("Graph 1: 25% of Total Raw Materials")
#     #     save_graph_as_png(fig1, "graph1.png")

#     #     data = {k: raw_df[k] for k in material_keys + other_keys if isinstance(raw_df.get(k), (int, float))}
#     #     fig2, ax2 = plt.subplots()
#     #     ax2.bar(data.keys(), data.values())
#     #     ax2.set_title("Graph 2: Raw Material Usage")
#     #     plt.xticks(rotation=45)
#     #     save_graph_as_png(fig2, "graph2.png")

#     #     fig3, ax3 = plt.subplots()
#     #     ax3.pie([0.8, 0.2], labels=["80% Slice", "Remaining 20%"], autopct='%1.1f%%')
#     #     ax3.set_title("Graph 3: Placeholder Slice")
#     #     save_graph_as_png(fig3, "graph3.png")

#     #     # Create PDF
#     #     pdf = FPDF()
#     #     pdf.add_page()
#     #     pdf.set_font("Arial", size=12)

#     #     for i in range(1, 4):
#     #         pdf.cell(200, 10, txt=f"Graph {i}", ln=True, align='C')
#     #         pdf.image(f"graph{i}.png", x=10, w=180)
#     #         pdf.multi_cell(0, 10, txt="This summary sheet gives detailed information about the benchmark cement plant (both international and domestic). If the detailed assessment was performed, reference facility and actual facility data is given for each process step for comparison. If the quick assessment was carried out, data is only given for each process step for the reference facility; and total energy (for the entire facility) is given for both the reference and actual facilities. Both international and domestic best practice values, technologies, and references for those values and technologies are provided on this sheet for each process step. The user may continue on to the next page by pressing the next button.  Pressing the references button will show all references used to create the benchmark as well as those used for the efficiency measures. .")

#     #     pdf_output = os.path.join(tempfile.gettempdir(), "report.pdf")
#     #     pdf.output(pdf_output)

#     #     with open(pdf_output, "rb") as f:
#     #         st.download_button("Download Report PDF", f, file_name="energy_report.pdf")


# # Initial state
# if "page" not in st.session_state:
#     st.session_state.page = "Home"

# # Page routing
# if st.session_state.page == "Energy Input Sheet":
#     energy_input_sheet()
# elif st.session_state.page == "Get Started":
#     get_started()
# elif st.session_state.page == "Home":
#     home()

#### Two Image Background - Green ###

import streamlit as st
from PIL import Image
import base64
from datetime import date
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table
import tempfile

st.set_page_config(layout="wide")

        # Set custom background color
        # st.markdown("""
        #     <style>
        #     body, .main, .block-container, header, footer, .stSidebar {
        #         background-color: #1d392b !important;
        #     }
        #     </style>
        # """, unsafe_allow_html=True)



hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Load and encode image
with open("green_left_best_xhigh.png", "rb") as img_file:
    encoded_best_high = base64.b64encode(img_file.read()).decode()

def home():
    # ---- UP Container ----
    with st.container():

        st.markdown(f"""
            <div style="
                background-image: url('data:image/png;base64,{encoded_best_high}');
            background-size: cover;
            background-position: center;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;">
        </div>
    """, unsafe_allow_html=True)

    # ---- DOWN Container ----
    with st.container():
        left_col, right_col = st.columns([1.3, .7])

        with left_col:
            # st.write("")
            
            st.markdown(
                """
                <br>
                <div style="background-color: #f0f0f0; padding: 2em; border-radius: 5.5px;">
                    <p style="color: #666;"><span style="font-size: 1.5em;"><b>Your Privacy is Important to Us</b></span><br>
                    <br>
                    We understand that business data can be sensitive and proprietary. This tool is designed with your confidentiality in mind. All processing happens locally in your browser — <b> no data is collected or stored on our servers.</b>
                    <br>
                    <br>
                    For this reason, all data must be entered in <b>one sitting</b>. Once you close or refresh the page, your inputs will be cleared to ensure your information is never retained.
                    <br>
                    <br>
                    You can use the tool with full confidence that your <b> inputs stay secure and entirely under your control. </b> We do not track, share, or retain any information you enter.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Right Column - Form
        with right_col:
            st.write("")
            st.write("")
            # st.write("")
            
            with st.form(key="report_form", enter_to_submit=False):
                st.markdown("#### Begin BEST Assessment")

                # Removes auto hint on form fields
                st.markdown("""
                    <style>
                    .stTextInput > div > div > input:focus + div {
                        display: none;
                    }
                    </style>
                    """, unsafe_allow_html=True)
                
                assessment_title = st.text_input("BEST Assessment Title")
                # today = st.date_input("Date", value=date.today(), disabled=True)
                st.write("")
                assessment_type = st.selectbox("Assessment Type", ["Detailed Assessment", "Quick Assessment"])
                st.write("")
                left, center, right = st.columns([1, 1, 1])
                with center:
                    submitted = st.form_submit_button("Get Started")



            if submitted:
                st.session_state.report_title = assessment_title
                st.session_state.assessment_type = assessment_type
                st.session_state.page = "Get Started"

def get_started():
    # ---- First Container ----
    with st.container():
        st.markdown("### Raw Material Inputs")
        # create three columns
        left, center, right = st.columns([.15, .7, .15])
        with center:
            with st.form("raw_materials_form", enter_to_submit=False):
                

                # Input fields
                limestone = st.number_input("Limestone used (tonnes)", format="%e")
                clay = st.number_input("Clay used (tonnes)", format="%e")

                default_iron_ore = 9.0
                iron_ore = st.number_input("Iron Ore used (tonnes)", format="%e",
                                        value=default_iron_ore, key="iron_ore")

                default_fly_ash = 9.0
                fly_ash = st.number_input("Fly Ash used (tonnes)", format="%e",
                                        value=default_fly_ash, key="fly_ash")

                other1_type = st.text_input("Other 1 - Additive Type")
                other1_amount = st.number_input("Other 1 - Amount (tonnes)", format="%e")
                other2_type = st.text_input("Other 2 - Additive Type")
                other2_amount = st.number_input("Other 2 - Amount (tonnes)", format="%e")

                left_raw, center_raw, right_raw = st.columns([1,1,1])
                with center_raw:
                    submitted = st.form_submit_button("Submit Raw Material Data")

                if submitted:
                    # Store inputs in session state
                    st.session_state.raw_materials_df = {
                        "Limestone": limestone,
                        "Clay": clay,
                        "Iron Ore": iron_ore,
                        "Fly Ash": fly_ash,
                        f"Other 1 - {other1_type}": other1_amount,
                        f"Other 2 - {other2_type}": other2_amount
                    }

                    # Convert to DataFrame for display
                    df_preview = pd.DataFrame.from_dict(st.session_state.raw_materials_df, orient='index', columns=['Amount (tonnes)'])
                    df_preview.index.name = "Material"
                    df_preview = df_preview.reset_index()

                    # Display as pretty table
                    st.subheader("Preview of Entered Data")
                    st.dataframe(df_preview.style.format({"Amount (tonnes)": "{:,.2e}"}), use_container_width=True)

    # ---- Second Container ----
        with st.container():
            st.markdown("### Clinker Production")
            kiln_types = [
                "Select Kiln Type",
                "Wet Process Kiln",
                "Dry Process Kiln",
                "Preheater Kiln",
                "Precalciner Kiln",
                "Other (Specify)"
            ]

            left, center, right = st.columns([.15, .7, .15])
            
            with center:
                num_kilns = st.number_input("How many kilns are at your facility?", min_value=1, max_value=10, step=1, key="num_kilns")

                with st.form("clinker_production_form", enter_to_submit=False):
                

                    clinker_data = []

                    for i in range(num_kilns):
                        st.markdown(f"**Kiln {i + 1}**")
                        cols = st.columns([2, 2])
                        with cols[0]:
                            kiln = st.selectbox(f"Kiln Type {i + 1}", kiln_types, key=f"kiln_type_{i}")
                        with cols[1]:
                            amount = st.number_input(f"Clinker Produced (tonnes/year) for Kiln {i + 1}", min_value=0.0, step=100.0, key=f"clinker_amt_{i}")
                        clinker_data.append({
                            "Kiln #": i + 1,
                            "Kiln Type": kiln,
                            "Clinker Produced (tonnes/year)": amount
                        })
                        st.markdown("---")

                    left_clinker, center_clinker, right_clinker = st.columns([1,1,1])
                    with center_clinker:
                        clinker_submitted = st.form_submit_button("Submit Clinker Data")

                    if clinker_submitted:
                        df_clinker = pd.DataFrame(clinker_data)
                        st.subheader("Preview of Clinker Production Data")
                        st.dataframe(df_clinker.style.format({"Clinker Produced (tonnes/year)": "{:,.2f}"}), use_container_width=True)
                        st.session_state.clinker_df = df_clinker

    # ---- Third Container ----
    with st.container():
        left_col, spacer, right_col = st.columns([1, 6, 1])

        with left_col:
            back_clicked = st.button("Back")

        with right_col:
            next_clicked = st.button("Next")

        if back_clicked:
            st.session_state.page = "Home"
        elif next_clicked:
            st.session_state.page = "Energy Input Sheet"

def energy_input_sheet():
    st.markdown("### Energy Input Sheet")
    st.markdown("""
    
    """)

    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Score": [85, 90, 95]
    })

    st.dataframe(df)

    if st.button("Export to PDF"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
            doc = SimpleDocTemplate(tmpfile.name, pagesize=letter)
            table_data = [df.columns.tolist()] + df.values.tolist()
            table = Table(table_data)
            doc.build([table])

            with open(tmpfile.name, "rb") as f:
                st.download_button("Download PDF", f, file_name="dataframe_report.pdf")



##### Page Routing #####

# Initial state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Page routing
if st.session_state.page == "Get Started":
    get_started()
elif st.session_state.page == "Energy Input Sheet":
    energy_input_sheet()
elif st.session_state.page == "Home":
    home()




# #### One Image Background - Green ###

# import streamlit as st
# from PIL import Image
# import base64

# st.set_page_config(layout="wide")

# # Set custom background color
# st.markdown("""
#     <style>
#     body, .main, .block-container, header, footer, .stSidebar {
#         background-color: #1d392b !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Load and encode image
# with open("best.png", "rb") as img_file:
#     encoded = base64.b64encode(img_file.read()).decode()

# def home():
#     # Background image container with no padding
#     st.markdown(f"""
#         <div style="
#             background-image: url('data:image/png;base64,{encoded}');
#             background-size: cover;
#             background-position: center;
#             height: 100vh;
#             display: flex;
#             flex-direction: column;
#             justify-content: center;
#             align-items: center;">
#         </div>
#     """, unsafe_allow_html=True)

#     # Simulated overlay using centered column
#     col1, col2, col3 = st.columns([3, 1, 3])
#     with col2:
#         if st.button("Get Started"):
#             st.session_state.page = "Get Started"
#             st.rerun()

# def get_started():
#     st.title("Production Input Sheet 1 - Raw Materials and Clinker Production")
#     st.subheader("Raw materials")
#     st.write("1. Amount of limestone used. Enter annual amount of limestone in tonnes of material.")
#     st.write("2. Quantity of additives used. For each additive, enter annual amount in tonnes. If additives other than those listed are used, enter the additive type in the “other 1” or “other 2” box and its amount.")
#     st.write("3. Enter the amount of materials that are preblended, crushed, dried and ground. User may use default values (where provided) or may enter his/her own data if available.")

#     # Input fields
#     limestone = st.number_input("Limestone used (tonnes)", min_value=0.0, step=100.0, format="%e")
#     clay = st.number_input("Clay used (tonnes)", min_value=0.0, step=10.0, format="%e")
#     default_iron_ore = 9.0
#     iron_ore = st.number_input("Iron Ore used (tonnes)", min_value=0.0, step=10.0, format="%e", value=default_iron_ore, key="iron_ore")
#     st.markdown("""
#         <style>
#         div[data-testid="stNumberInput"]:has(input[aria-label='Iron Ore used (tonnes)']) input {
#             background-color: #d5f7dc !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)
    
#     default_fly_ash = 9.0
#     fly_ash = st.number_input("Fly Ash used (tonnes)", min_value=0.0, step=10.0, format="%e", value=default_fly_ash, key="fly_ash")
#     st.markdown("""
#         <style>
#         div[data-testid="stNumberInput"]:has(input[aria-label='Fly Ash used (tonnes)']) input {
#             background-color: #d5f7dc !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)
    
#     other1_type = st.text_input("Other 1 - Additive Type")
#     other1_amount = st.number_input("Other 1 - Amount (tonnes)", min_value=0.0, step=10.0, format="%e")
#     other2_type = st.text_input("Other 2 - Additive Type")
#     other2_amount = st.number_input("Other 2 - Amount (tonnes)", min_value=0.0, step=10.0, format="%e")

#     # Store inputs in temporary DataFrame
#     st.session_state.raw_materials_df = {
#         "Limestone": limestone,
#         "Clay": clay,
#         "Iron Ore": iron_ore,
#         "Fly Ash": fly_ash,
#         f"Other 1 - {other1_type}": other1_amount,
#         f"Other 2 - {other2_type}": other2_amount
#     }

#     # Display preview
#     st.subheader("Preview of Entered Data")
#     st.write(st.session_state.raw_materials_df)

# # Initial state
# if "page" not in st.session_state:
#     st.session_state.page = "Home"

# # Page routing
# if st.session_state.page == "Get Started":
#     get_started()
# elif st.session_state.page == "Home":
#     home()
