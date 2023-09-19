from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My WebPage", page_icon=":tada:", layout="wide")


def load_lottieurl2(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


img_project1 = Image.open("images/stenosis_img.jpg")
load_greeting = load_lottieurl2("https://lottie.host/03174646-5d44-473e-a082-e8a8d9038222/mXbnb7EyzL.json")

st.subheader("Hi, I am Farhaan :wave:")
st.title("A Newbie ML Engineer from Bangladesh")
st.write("I am An enthusiastic AI and ML "
         "researcher with a strong open-source "
         "contribution drive. Effective communicator "
         "& a natural writer. Seeking opportunities in "
         "the field of AI for innovation and collaboration")
st.write("[Get Connected via LinkedIn >](https://www.linkedin.com/in/shfarhaan/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(load_greeting, height=400, key="greet2")
    with right_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            As a newbie Machine Learning and Data Science Engineer, I am on a passionate journey to delve deep into the world of AI and research. Here's a glimpse of what I do:

            - **Machine Learning Enthusiast:** My enthusiasm for Machine Learning is unwavering, and I'm committed to mastering the art of algorithms and data-driven insights.

            - **Continuous Learner:** I thrive on acquiring new knowledge and skills, staying up-to-date with the latest trends and techniques in the field. Learning is not just a phase but a perpetual adventure for me.

            My path is just beginning, and I'm excited about the endless possibilities that lie ahead in the realm of Machine Learning and Data Science. Every day is an opportunity to learn, explore, and contribute to this exciting field.
            """
        )
        st.write("[GitHub >](https://github.com/farhaan-sh)")
        # st.write("[Facebook >](https://www.facebook.com/fb.shfarhaan/)")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project1)
    with text_column:
        st.subheader("Stenosis Detection from Angiographic Images")
        st.write(
            """
            **Project Description:**

            - **Early CAD Detection:** Our project focuses on detecting Coronary Artery Disease (CAD) at its early stages, which is crucial for timely treatment and improved patient outcomes.

            - **Innovative Approach:** We've pioneered an innovative approach that leverages advanced technology and precision to identify specific markers or indicators of CAD within the body.

            - **New Predictive Method:** Our goal is to provide a novel way of predicting CAD in its earliest phases, enabling doctors to intervene and provide necessary care before the disease progresses to a more critical stage.

            - **Reshaping Diagnosis:** This project has the potential to revolutionize how CAD is diagnosed and managed, potentially reducing the impact of the disease on patients' lives.
            """
        )
        st.write(
            """
            **Keywords:** `Coronary Artery Disease (CAD)`, `Stenosis detection`, `Bayesian Probability analysis`, `Early diagnosis`, `Computer vision`
            """
        )