import streamlit as st
from streamlit_option_menu import option_menu
import homepage, experience, resume, contact

st.set_page_config(
    page_title="My WebPage", 
    page_icon=":tada:", 
    layout="wide")

# # Option Menu 1
# with st.sidebar:
#     selected = option_menu(
#         menu_title="Sazzad H. Farhaan",
#         options=["Home", "Experience", "Resume", "Contact"],
#         # "Awards", "Education", "Certificates", "Technical Skills"
#         # "Competitions", "Volunteering", "Blog"]
#         icons=["person-bounding-box", "hourglass-split",  # From https://icons.getbootstrap.com/
#                "file-earmark-person-fill", "envelope-at"],
#         menu_icon="Mortorboard",
#         default_index=0,
#     )
# if selected == "About Me":
#     st.title(f"You have selected {selected}")
# if selected == "Experience":
#     st.title(f"You have selected {selected}")
# if selected == "Resume":
#     st.title(f"You have selected {selected}")
# if selected == "Contact":
#     st.title(f"You have selected {selected}")
# 

class MultiApp:

    def __init__(self):
        self.apps = []

    # def add_app(self, title, func):
    #
    #     self.apps.append({
    #         "title": title,
    #         "function": func
    #     })

    def run():
        # app = st.sidebar(
        with st.sidebar:
            selected = option_menu(
                menu_title="Sazzad H. Farhaan",
                options=["Home", "Experience", "Resume", "Contact"],
                # "Awards", "Education", "Certificates", "Technical Skills"
                # "Competitions", "Volunteering", "Blog"]
                icons=["person-bounding-box", "hourglass-split",  # From https://icons.getbootstrap.com/
                       "file-earmark-person-fill", "envelope-at"],
                menu_icon="Mortorboard",
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }

            )

        if selected == "Home":
            homepage.app()
        if selected == "Experience":
            experience.app()
        if selected == "Resume":
            resume.app()
        if selected == "Contact":
            contact.app()

    run()
