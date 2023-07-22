import streamlit as st
from PIL import Image


def default_page_config():
    """
    This function is for setting up the
    basic page configuration such as title, icon exc.
    """
    st.set_page_config(
        page_title="Learn DS' and Algos",
        page_icon="💻",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    hide_st_style = """
            <style>P
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

    st.markdown(hide_st_style, unsafe_allow_html=True)


def page_content():
    """
    This function includes all of the page content
    such as information texts, code blocks exc.
    """


def main():
    """
    Main Function
    """

    default_page_config()
    page_content()


if __name__ == main():
    main()
