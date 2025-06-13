import streamlit as st
from PIL import Image
from predict import predict_image

st.set_page_config(page_title="Klasifikasi Sampah AI - TrashGu", layout="centered")
st.markdown("""
<style>
/* Menghilangkan header dan footer Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
/* Gaya tombol dan komponen */
.upload-box {
    border: 2px dashed #ccc;
    border-radius: 12px;
    padding: 40px;
    text-align: center;
    background-color: #fafafa;
}
.analyze-btn {
    background-color: #2c7a3e;
    color: white;
    font-weight: bold;
    font-size: 18px;
    padding: 10px 24px;
    border-radius: 12px;
}
.analyze-btn:hover {
    background-color: #1e5128;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.image("logo-trashgu.png", width=200)

st.markdown("""
<h3 style="text-align:center; font-weight:800;">
    Sistem Klasifikasi Sampah dengan Articial Intelligence
</h3>
<p style="text-align:center; font-size:18px;">
    Unggah gambar sampah untuk mengidentifikasi 10 kategori sampah<br>
    secara otomatis menggunakan teknologi AI
</p>
""", unsafe_allow_html=True)

# Upload gambar
uploaded_file = st.file_uploader(
    "Drag & drop gambar atau klik untuk memilih",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed"
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar diunggah', use_container_width=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    analyze = st.button("🔍 Analisis Gambar", key="analyze_button")

# css untuk tombol analisis
st.markdown("""
    <style>
    div.stButton > button#analyze_button {
        background-color: #3F7D58;
        color: white;
        font-weight: bold;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 12px;
        transition: 0.3s;
    }
    div.stButton > button#analyze_button:hover {
        background-color: #2e6c4a;
    }
    </style>
""", unsafe_allow_html=True)

if analyze and uploaded_file is not None:
    image_pil = Image.open(uploaded_file).convert("RGB")
    with st.spinner("Menganalisis gambar dengan model AI..."):
        label, jenis, confidence, info = predict_image(image_pil)

    st.success(f"📌 Nama Sampah: {label.capitalize()}")
    st.info(f"♻️ Jenis Sampah: {jenis.capitalize()}")
    st.warning(f"✅ Akurasi Prediksi: {confidence * 100:.2f}%")
    st.write(f"🛠️ Cara Daur Ulang: {info}")

elif analyze and uploaded_file is None:
    st.warning("⚠ Silakan unggah gambar terlebih dahulu.")