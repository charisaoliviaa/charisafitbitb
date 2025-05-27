import streamlit as st

st.title("Charisa FITB-ITB")
st.write(
    "Yuk berdoa dan belajar bareng niat masuk itb"
)
st.image("3e27ae0aaf708820d0ff0225fe3e1085-removebg-preview.png",width=200)


st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else: 
st.write(f"{angka} adalah Bilangan Ganjil")
