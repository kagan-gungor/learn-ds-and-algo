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
    image_array = Image.open("sources/python_objects/arrays.png")
    image_types = Image.open("sources/python_objects/dimensions.png")

    st.title("Arrays and Other Python Objects")
    st.write(
        "In this section, we will examine how arrays work, what Python Lists have almost\
              the same usage, what Dictionary and Tuples are, and their uses."
    )
    st.write(
        "In these data structures, there are basic operations that can be performed on the elements.\
              These; They are **creating, inserting, traversing, searching, accessing and deleting** operations.\
              Let's examine how these processes are applied in the following tabs."
    )

    tab_1, tab_2, tab_3, tab_4 = st.tabs(["Arrays", "Lists", "Dictionaries", "Tuples"])

    with tab_1:
        st.header("Arrays")
        st.write(
            "An array is a data structure which can store collection of elements of the same type.\
                 Arrays are not native in Python. Instead we use lists, which are similar but more flexible.\
                 We can use Numpy module or Array module for creating arrays."
        )
        st.write(
            "Here is an example of an array. Array can store data of specified type and each\
                  element of an array has a unique index. Also elements of an array are located in\
                  a contiguous order."
        )
        st.image(image_array, use_column_width="always", caption="Array")
        st.header("Types of Array")
        st.write(
            "Types of arrays vary according to the size of the arrays. One-dimensional arrays\
                  can be thought of as a data type that can be held in a single row. Two-dimensional\
                  arrays form a mathematical matrix. Multidimensional arrays are an advanced version of\
                  a single-dimensional array that can be nested up to multilevel."
        )
        st.image(image_types, use_column_width="always", caption="Types of Arrays")
        st.write(
            "Now let's look at how the applications we mentioned above will be realized in the array."
        )
        array_creation = """#creation of array \nimport array \nmy_array = (i, [1,2,3,4,5])
                         """
        st.code(array_creation, language="python")
        array_traverse = """#traversing \nfor i in my_array: \n   print(i)"""
        st.code(array_traverse, language="python")
        array_access = """#accessing elements\n my_array[3]\n my_array[2:4]"""
        st.code(array_access, language="python")
        array_insert = """#inserting elements can be done by three different ways \n#append() method adds elements the end of the list \nmy_array.append(6)\n\
#insert() methods adds element by its index\nmy_array.insert(3, 11)\n#extend() method extends the list with another list\nmy_array1 = array('i', [10,11,12])\n\
my_array.extend(my_array1) """
        st.code(array_insert, language="python")
        array_search = """#for searching elements we use linear search for now\ndef linear_search(array, target):\n\
    for i in range(len(arr)):\n         if arr[i] == target:\n              return i\n     return -1"""
        st.code(array_search, language="python")
        array_delete = """#deleting elements\n#remove() method\nmy_array.remove(11)\n#pop() methods deletes an element from the last and hold it if we want to use it\n\
my_array.pop()"""
        st.code(array_delete, language="python")

        st.header("When to Use/Avoid Arrays")
        st.write(
            "**Use:**\n - To store multiple variables of same data type\n - For random accessing\n\
        \n**Avoid:**\n - If you don't have the same data type\n - Reserved memory would be a problem"
        )


def main():
    """
    Main Function
    """
    default_page_config()
    page_content()


if __name__ == main():
    main()
