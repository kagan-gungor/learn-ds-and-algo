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
    image_runtime = Image.open("sources/big_o/runtime.jpg")
    image_measure = Image.open("sources/big_o/measure_big_o.png")
    st.title("Big O")
    st.write(
        "Big O is the language and metric we use to describe the efficiency of algorithms. \
             Without understanding Big O Notation it's not possible to develop efficient algorithms.\
             We want the running time and memory to be measured according to the increase or\
              decrease of the input values. Let us explain the two concepts mentioned in this definition."
    )
    st.header("What is Input Size?")
    st.write(
        "We define the input size as the total number of items present in the input\
             If we increase the input size, the total number of operations performed by an algorithm\
            will increase. In other words, the time taken by an algorithm will increase with\
             the growth in the input size."
    )
    st.header("What is Running Time")
    st.write(
        "The running time of an algorithm for a given input size depends on the number of operations\
            executed. The greater the number of operations, the longer the running time of an algorithm."
    )
    st.header("Time Complexity")
    st.write(
        "Suppose we are comparing two different algorithms. Let the first of these algorithms be\
              completed in 30 seconds, and the second in 60 seconds. Based on this, we can conclude that\
              the first algorithm is more efficient. But when calculating time complexity, we measure the\
              number of operations, not the number of runs of algorithms. The reason we do this is that when\
              we run the same code on a faster computer, the algorithm will run faster, so we do not have the\
              opportunity to make a healthy measurement. But the number of operations does not change regardless\
              of the power of the computer, so we measure accordingly."
    )
    st.header("Space Complexity")
    st.write(
        "Space complexity is the amount of the memory that some code used. Here, we need to do a similar\
              calculation as we calculate time complexity.."
    )
    st.header("Asymptotic Notations")
    st.write(
        "1. **Big Omega Notation(Ώ)** is a notation to represent the best case time complexity of an algorithm.\
             \n 2. **Big Theta Notation(Θ)** is a notation to represent the average case time complexity of an algorithm.\
             \n 3. **Big O Notation(O)** is a notation to represent the worst-case time complexity of an algorithm.\
             In practice, we want to know how algorithms will perform in the worst case, so the complexity of an\
              algorithm is often represented by Big O."
    )
    st.header("Runtime Complexities")
    st.image(image_runtime, use_column_width="always", caption="Runtime Complexities")
    st.write("Let's give examples of some runtime complexities.")
    st.write(
        "1. **Constant time complexity O(1)**: Our algorithm performs a constant number of operations.\
             The time complexity does not depend on the input size.\
             \n 2. **Logarithmic time complexity O(logn)**: IN this complexity, input size decreases by some of \
             operations for the input size.(Binary search, divide and conquer solutions etc.)\
             \n 3. **Linear time complexity O(n)**: Here, time complexity will grow in direct proportion to the size of\
             input data. The best case is to try to keep our function running below or within this range of complexity.\
             \n 4. **Quadratic time complexity O(n^2)**: A quadratic time complexity often comes when there are two nested\
             loops in algorithm. Such situations occur mostly during matrix-based problems and brute force solutions\
             to explore all pairs of the input element."
    )
    st.write("Some tips to make our job easier when analyzing algorithms:")
    st.image(image_measure, use_column_width="always", caption="Tips")


def main():
    """
    Main Function
    """

    default_page_config()
    page_content()


if __name__ == main():
    main()
