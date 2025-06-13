import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing import image
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

# Mengatur layout dan menyembunyikan menu Streamlit
st.set_page_config(page_title="TrashGu", layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Logo dan Navigasi
col1, col2 = st.columns([1, 3])
with col1:
    st.image("logo-trashgu.png", width=150)

with col2:
    menu = """
    <div style='text-align:right; font-size:18px;'>
        <a href='#' style='margin:0 15px; color:#2c7a3e; text-decoration:none; font-weight:bold;'>Beranda</a>
        <a href='#' style='margin:0 15px; color:gray; text-decoration:none;'>Tentang</a>
        <a href='#' style='margin:0 15px; color:gray; text-decoration:none;'>Fitur</a>
        <a href='#' style='margin:0 15px; color:gray; text-decoration:none;'>Artikel</a>
        <a href='#' style='margin:0 15px; color:gray; text-decoration:none;'>Daftar</a>
        <a href='#' style='margin:0 15px; background-color:#2c7a3e; color:white; padding:6px 14px; border-radius:6px;'>Masuk</a>
    </div>
    """
    st.markdown(menu, unsafe_allow_html=True)

st.markdown("---")

# Konten utama
col_text, col_img = st.columns(2)

with col_text:
    st.markdown("""
    <h1 style='font-weight:900;'>Kenali Jenis Sampahmu<br>Seketika!</h1>
    <p style='font-size:18px;'>
        <strong>TrashGu</strong> hadir untuk bantu kamu melakukan<br>
        klasifikasi sampah organik dan anorganik dengan<br>
        cerdas dan mudah.
    </p>
    """, unsafe_allow_html=True)

    if st.button("Klasifikasi Sekarang", use_container_width=True):
        switch_page("klasifikasi")

with col_img:
    image = Image.open("mascot.png")  
    st.image(image, width=280)
