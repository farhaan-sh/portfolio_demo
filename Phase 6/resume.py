from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import fitz  # PyMuPDF

# st.set_page_config(page_title="My WebPage", page_icon=":tada:", layout="wide")


def fetch_and_display_pdf(pdf_link):
    try:
        # Fetch PDF content from the Google Drive link
        response = requests.get(pdf_link)
        response.raise_for_status()

        # Read the PDF content
        pdf_document = fitz.open(stream=response.content, filetype="pdf")

        # Display each page as an image
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            image_bytes = page.get_pixmap().get_image_data()
            st.image(image_bytes, use_container_width=True, caption=f"Page {page_num + 1}")
    except Exception as e:
        st.error(f"Error: {e}")


def app():
    st.title(f"You have selected Resume")

    # # Input for Google Drive PDF link
    # pdf_link = st.text_input("https://drive.google.com/file/d/1vec0fL0ZuD_Ifp4TzbD-uUQPLueXkVA-")
    #
    # if pdf_link:
    #     # Construct the Google Drive embed link
    #     embed_link = f"https://drive.google.com/viewerng/viewer?embedded=true&url={pdf_link}"
    #
    #     # Display the PDF using an iframe
    #     st.markdown(f'<iframe src="{embed_link}" width="900" height="600"></iframe>', unsafe_allow_html=True)
    #

    # Hardcoded Google Drive PDF link
    pdf_link = "https://drive.google.com/file/d/1vec0fL0ZuD_Ifp4TzbD-uUQPLueXkVA-/view"

    fetch_and_display_pdf(pdf_link)
