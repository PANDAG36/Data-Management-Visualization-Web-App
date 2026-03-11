import streamlit as st
import pandas as pd

def cleaning(file):

    if file:
        rfile = pd.read_excel(file)
        st.subheader("File Uploaded")
        st.write(rfile)
    else:
        st.write("pass")


st.header("Data Visualization")
st.write("Call widget functions in your entrypoint file when you want a widget to be stateful across pages. Assign keys to your common widgets and access their values through Session State within your pages.")

st.subheader("Upload You data Here:")
fi = st.file_uploader("Upload your EXCEL file here",type=["xlsx","csv"])



def reading_file(file):
    if file is not None:
        try:
            st.session_state["file"] = pd.read_excel(file)
        except:
            st.session_state["file"] = pd.read_csv(file)

    return st.session_state["file"]

if fi is not None:
    file = reading_file(fi)
else:
    file = None

if file is not None:
    st.subheader("RAW DATA")
    st.dataframe(file)

    st.subheader("After Cleanng")
    c_data = file.dropna()
    st.dataframe(c_data)

    st.subheader("Removing Duplicates")
    rd_data = c_data.drop_duplicates()
    st.dataframe(rd_data)

    list_  = file.columns.to_list() #gets the colum name from the file 

    if list_:
        xaxis = st.selectbox("select the value for X- axis", list_)

        list_.remove(xaxis)

        yaxis = st.selectbox("select the value for X- axis", list_)

    chart = st.selectbox(
    "Chart Type",
    ["Bar", "Line", "Scatter"]
    )

    if chart == "Bar":
        st.bar_chart(rd_data, x=xaxis, y=yaxis)

    elif chart == "Line":
        st.line_chart(rd_data, x=xaxis, y=yaxis)

    else:
        st.scatter_chart(rd_data, x=xaxis, y=yaxis)




