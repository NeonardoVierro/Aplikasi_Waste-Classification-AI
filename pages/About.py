"""Halaman penjelasan proyek dan hasil evaluasi model."""

import streamlit as st

from utils.ui import render_footer, render_sidebar, setup_page


setup_page("Tentang | AI Waste Classification")
render_sidebar()

st.title("Tentang Project")
st.markdown(
    """
Proyek akhir mata kuliah **Artificial Intelligence for Education** ini mengembangkan sistem
klasifikasi gambar sampah berbasis deep learning. Seluruh foto pada dataset dikumpulkan sendiri
oleh kelompok, bukan diambil dari internet.
"""
)

col1, col2, col3 = st.columns(3)
col1.metric("Total dataset", "150 gambar", border=True)
col2.metric("Jumlah kelas", "3 kelas", border=True)
col3.metric("Model terpilih", "MobileNetV2", border=True)

st.subheader("Dataset")
st.markdown(
    """
- **Organik:** daun pepaya
- **Anorganik:** botol air mineral Le Minerale 600 ml
- **B3:** kemasan herbisida Roundup
"""
)

st.subheader("Perbandingan model")
cnn, transfer = st.columns(2)
cnn.metric("CNN From Scratch", "93% akurasi", border=True)
transfer.metric("Transfer Learning MobileNetV2", "100% akurasi", border=True)

st.subheader("Kesimpulan")
st.success(
    "Transfer Learning MobileNetV2 dipilih sebagai model implementasi karena memperoleh akurasi terbaik."
)
st.caption("Catatan evaluasi: test set pada notebook berisi 15 gambar.")

render_footer()
