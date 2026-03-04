import streamlit as st
import mysql.connector as mys
import datetime as d
import pandas as pd


def sql_connection():
    con = mys.connect(
        host = "localhost",
        user = "root",
        password = "NewPassword123",
        database = "VERNA"
    )
    return con ,con.cursor()


def insert():
    if f_name:
        con, cursor = sql_connection()
        cursor.execute("INSERT INTO students_info (FirstName, LastName, Department, DOB, MobileNumber) VALUES (%s,%s,%s,%s,%s);",(f_name, l_name, dep, dob, mob_num))
        con.commit()    
        con.close()
        st.success("Value Added sucessfully")
        st.balloons()
    else:
          st.error("Fill all the Values")

def view():
      con, cursor = sql_connection()
      df = pd.read_sql("select * from students_info;", con)
      con.close()

      return df

def delete():
    con, cursor = sql_connection()
    cursor.execute(f"DELETE FROM students_info WHERE SNo = {del_in};")
    con.commit()
    con.close()
    st.error(f"🗑️ Employee ID {del_in} deleted successfully!")
      
def update():
    con, cursor = sql_connection()
    cursor.execute(f"UPDATE students_info SET {mod1} = %s WHERE {head} = %s;",(new_val, name))
    con.commit()
    con.close()
    st.success("Updated SucessFully")
      
      

st.header("SQL Operations",text_alignment="center")
menu = ["View","Insert", "Update", "Delete"]
choice = st.selectbox("Select Operation", menu)


if choice == "Insert":
        con, cursor = sql_connection()
        departments = ["CSE","Mech","ECE","B-Tech","Bio-Medical","civil"]
        f_name = st.text_input("Enter Your first Name").title()
        l_name = st.text_input("Enter Your Second Name").title()
        dep = st.selectbox("Select your Departments",departments)
        dob = st.date_input("Select your DOB",min_value= d.date(1900,1,1),max_value=d.date.today())
        dob = dob.strftime("%Y-%m-%d")
        mob_num = st.text_input("Enter your number")
        if st.button("SUBMIT"):
            if not (f_name or l_name or dob or mob_num):
               st.error("INSERT ALL THE ELEMENTS")
            else:
                insert()


elif choice == "View":
        st.header("View Table",text_alignment="center")
        df = view()
        st.dataframe(df)
        
elif choice == "Update":
        st.header("Update")
        df = view()
        st.dataframe(df)
        header = ["SNo"]
        headers = ["SNo","FirstName", "LastName","DOB", "MobileNumber"]
        head = st.selectbox("Select the Uniqe header;",header)
        name = st.text_input(f"Enter the value for {head}")
        mod1 = st.selectbox("Select the header that you needs to Modify;",headers)
        new_val = st.text_input(f"Enter the New Value for {mod1}")
        if st.button("Update"):
              update()



elif choice == "Delete":
        st.header("Deleting",text_alignment="center")
        df = view()
        st.dataframe(df)
        del_in = st.number_input("Enter the Serial Number to Delete",min_value=0)
        if st.button("DELETE"):
              delete()


     
    






