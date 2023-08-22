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
    image_book1 = Image.open("sources/fundamentals/book1.jpg")
    image_book2 = Image.open("sources/fundamentals/book2.jpg")
    image_queue = Image.open("sources/fundamentals/queue.jpg")
    image_ds = Image.open("sources/fundamentals/types_of_ds.png")
    images = [image_book1, image_book2]

    st.title("Fundamentals")
    st.write(
        "In this chapter we will learn what data structures and algorithms\
              are and why they are important."
    )
    st.header("What is Data Structures?")
    st.write(
        "Data Structures is a method we use to organize data on the computer.\
            The purpose of this is to use data effectively. More specifically,\
            we use data to manage, process and access information in the most **effective** way."
    )
    st.write(
        "For example, since it will be difficult to find the book we want\
              among the scattered books in the image below, we would like to group\
              and order them in a certain way."
    )

    st.image(
        images,
        use_column_width="always",
        caption=[
            "Cluttured Books",
            "We want to organize the clutter in the data we have, as it is here.",
        ],
    )

    st.write(
        "The data structure we will use should change according to the data type\
              we have. To give another example, consider a crowd of people waiting to\
              enter a concert. In order for this group to enter the venue without a crowd,\
              we ask them to queue up by forming a queue. Unlike the scattered book example\
              above, they do not need to be grouped by topic or alphabetically. We would have\
              followed a different method to provide organization."
    )
    st.image(image_queue, use_column_width="always", caption="Queue")

    st.header("Types of Data Structures")
    st.write("We divide Data Structures into Primitive and Non Primitive.")
    st.write(
        "**Primitive Data Structures** are simple data types that cannot be broken down\
              into smaller data types. This is a predefined way of storing data of only\
             one type. In other words, this can hold a single value ina specificmemory location."
    )
    st.write(
        "**Non Primitive Data Structures** are derived from Primitive Data Structures. It can be\
              broken down into smaller parts and is more complex."
    )
    st.write(
        "We divide Non Primitive Data Structures into Linear and Non Linear. Linear Data Structures is a\
              data structure that contains a sequence and is bound to a neighboring value. The\
              order of the values is important here. Non Linear Data Structures, on the other hand,\
              are data structures that we can create without the need for any hierarchical order."
    )
    st.image(image_ds, use_column_width="always", caption="Types of Data Structures")
    st.header("What is an Algorithm?")
    st.write(
        "An algorithm is a set of instructions to perform a task. To explain a little more,\
              an algorithm is a well-defined, step-by-step rule for finding the desired output value from a given input value."
    )
    st.write(
        "If we go through the book example above, we can construct an algorithm consisting of a few\
              steps to line up the scattered books."
    )
    st.write(
        "1. Group books by topic \
        \n 2. Arrange the grouped books in alphabetical order among themselves \
        \n3. Buy a library\
        \n  4. Arrange the books on the bookshelf"
    )


def main():
    """
    Main Function
    """

    default_page_config()
    page_content()


if __name__ == main():
    main()
