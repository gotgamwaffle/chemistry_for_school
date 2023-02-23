import streamlit as st

from page1 import page1
from page2 import page2
from page3 import page3
from page4 import page4

# Define a dictionary to map page numbers to functions
pages = {
    1: page1,
    2: page2,
    3: page3,
    4: page4
}

# Get the current page number from session state
current_page = st.session_state.get('current_page', 1)

# Display the current page
pages[current_page]()

# Display a "Go to the first page" button if it's the last page
if current_page == 4:
    if st.button("Go to the first page", key="first_page_button"):
        current_page = 1
        st.session_state['current_page'] = current_page
else:
    # Display a "Next" button to go to the next page
    if st.button("Next", key="next_button_page_plz_work"):
        current_page += 1
        st.session_state['current_page'] = current_page
