import pandas as pd
import streamlit as st

st.title("CSV Operation ")

user_id = st.text_input("User ID: ")
name = st.text_input("Name: ")
role = st.text_input("Role: ")
salary = st.number_input("Salary: ", step=5000)

submit_btn = st.button("Add Employee")

csv = pd.read_csv("data.csv")
st.write("### Data")
edited_df = st.data_editor(csv)

save_btn = st.button("Save Changes")

if save_btn:
    edited_df.to_csv("data.csv", index=False)
    st.rerun()

if submit_btn:
    new_data = pd.DataFrame([[user_id, name, role, salary]], columns=["id", "name", "role", "salary"])
    csv = pd.concat([csv, new_data], ignore_index=True)

    csv.to_csv("data.csv", index=False)

    st.rerun()

st.bar_chart(csv.set_index("role")["salary"])