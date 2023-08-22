"""Streamlit is a frontend framework of python ecosystem"""
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

    image_amazon = Image.open("sources/introduction/amazon.png")
    image_facebook = Image.open("sources/introduction/facebook.png")
    image_google = Image.open("sources/introduction/google.png")
    images = [image_amazon, image_facebook, image_google]

    st.title("Learn Data Structures and Algorithms")
    st.write(
        "Welcome to Learn DS' and Algos. Here we begin a process where we will learn\
              from the simplest concepts of Data Structures and Algorithms to increasingly complex topics."
    )
    st.write(
        "In this process, we will both follow the relevant issues and examine the\
              solutions to the questions about the technical coding interview questions, which are indispensable\
              in the applications of large companies."
    )
    st.write("**All codes are written in Python.**")

    st.header("Contents")
    st.write("You can find all the content to be added below.")
    expander = st.expander("See contents")
    expander.write(
        "1. Fundamentals(about data structures and algorithms) \n 2. Big O \n 3. OOP \n 4. Linked List\
                   \n 5. Stack \n 6. Queue \n 7. Recursion \n 8. Trees \n 9. Hashing \n 10. Sort Algorithms\
                   \n 11. Search Algorithms \n 12. Graph Algorithms \n 13. Greedy Algorithms\
                   \n 14. Divide and Conquer Algorithms"
    )

    st.header("About Technical Coding Interviews")
    st.write(
        "Data Structures and Algorithms are not only a basic and must-know part of computer science,\
              but also appear in business life."
    )
    st.write(
        "These topics, which we come across in technical coding interviews of important companies,\
              not only contribute to our progress in our business life, but are also fun!"
    )
    st.write(
        "Below you can see the distribution of the questions asked by 3 big companies in their \
              technical code interviews. You can also find the link below to the article where these \
              pictures were taken for more information."
    )
    st.image(
        images, use_column_width="always", caption=["Amazon", "Facebook", "Google"]
    )
    st.write("Source article [link](https://algo.monster/problems/stats)")


def main():
    """
    Main Function
    """
    default_page_config()
    page_content()


if __name__ == main():
    main()
