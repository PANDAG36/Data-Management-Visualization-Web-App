import streamlit as st
import pandas as pd



pages  = {
    "MENU" : [
        st.Page("Home.py",title = "HOME"),
        st.Page("page_1.py",title = "Data Visualization"),
        st.Page("page_2.py",title = "SQL Operations")
    ]
}

nav = st.navigation(pages)

nav.run()


