import streamlit as st

st.title("Belajar Python")
st.write("Penambahan")

value_name = st.text_input("Masukkan nama user: ")
value_a = st.number_input("Angka Pertama", step=1)
value_b = st.number_input("Angka Kedua", step=1)

submit_btn = st.button("Tambahkan")

if submit_btn:
    st.write(f'Totalnya: {value_a + value_b}')
    st.write(f'Made by: {value_name}')