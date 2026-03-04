import streamlit as st

st.header("HOME",text_alignment="center")

st.divider()

col_1,col_2,col_3= st.columns(3)
with col_2:
    st.page_link("X:\PROGRAMS\.vscode\BS PROjECT\page_2.py",label="SQL operations",icon="🌐")
    st.page_link("X:\PROGRAMS\.vscode\BS PROjECT\page_1.py",label="Data Visualization",icon="📊")
