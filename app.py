"""Main page for the MobileNetV2 waste classification application."""

from pathlib import Path

import numpy as np
import streamlit as st
from PIL import Image, UnidentifiedImageError
from tensorflow import keras

from utils.preprocessing import CLASS_NAMES, DISPLAY_NAMES, prepare_image
from utils.ui import render_footer, render_sidebar, setup_page


MODEL_PATH = Path(__file__).parent / "models" / "model_transfer_learning_mobilenetv2_terbaik.keras"


@st.cache_resource(show_spinner=False)
def load_model(model_path: str):
    """Load and cache the trained model once per application process."""
    return keras.models.load_model(model_path, compile=False)


def reset_upload() -> None:
    """Clear the current image by rotating the uploader widget key."""
    st.session_state.upload_key += 1


def predict_image(model, image: Image.Image) -> np.ndarray:
    """Run inference and return one probability for every trained class."""
    prediction = np.asarray(model.predict(prepare_image(image), verbose=0)[0], dtype=np.float32)
    if prediction.size != len(CLASS_NAMES):
        raise ValueError(f"Output model berisi {prediction.size} kelas, bukan {len(CLASS_NAMES)} kelas.")
    if np.any(prediction < 0) or not np.isclose(float(prediction.sum()), 1.0, atol=1e-3):
        shifted = prediction - np.max(prediction)
        prediction = np.exp(shifted) / np.exp(shifted).sum()
    return prediction


setup_page("AI Waste Classification")
render_sidebar()
st.session_state.setdefault("upload_key", 0)

st.markdown(
    """
    <section class="hero">
      <span class="eyebrow">DEEP LEARNING &bull; MOBILENETV2</span>
      <h1>AI Waste Classification</h1>
      <p>Unggah gambar sampah dan dapatkan klasifikasinya secara instan menggunakan model transfer learning terbaik kami.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">Unggah gambar untuk dianalisis</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "Upload gambar sampah",
    type=("jpg", "jpeg", "png"),
    key=f"waste_image_{st.session_state.upload_key}",
    help="Format yang didukung: JPG, JPEG, dan PNG.",
    label_visibility="collapsed",
)

if uploaded_file is None:
    st.markdown(
        '<div class="hint-card"><span>💡</span><div><strong>Objek yang dikenali</strong><br>'
        'Daun pepaya, botol Le Minerale 600 ml, dan kemasan Roundup.</div></div>',
        unsafe_allow_html=True,
    )
else:
    try:
        image = Image.open(uploaded_file)
        image.load()
    except (UnidentifiedImageError, OSError, ValueError):
        st.warning("Gambar tidak dapat dibaca. Pastikan file tidak rusak dan berformat JPG, JPEG, atau PNG.")
    else:
        st.markdown("---")
        left, right = st.columns((1.08, 0.92), gap="large")
        with left:
            st.markdown('<div class="panel-title">Preview gambar</div>', unsafe_allow_html=True)
            st.image(image, use_container_width=True)
        with right:
            st.markdown('<div class="panel-title">Hasil prediksi</div>', unsafe_allow_html=True)
            if not MODEL_PATH.is_file():
                st.error(f"Model tidak ditemukan di `{MODEL_PATH}`.")
            else:
                try:
                    with st.spinner("Sedang menganalisis gambar..."):
                        probabilities = predict_image(load_model(str(MODEL_PATH)), image)
                    best_index = int(np.argmax(probabilities))
                    confidence = float(probabilities[best_index])
                    best_label = DISPLAY_NAMES[CLASS_NAMES[best_index]]
                    st.markdown(
                        f'<div class="result-card"><span>KATEGORI TERDETEKSI</span>'
                        f'<h2>{best_label}</h2><strong>{confidence:.2%} confidence</strong></div>',
                        unsafe_allow_html=True,
                    )
                    st.progress(confidence, text=f"Tingkat keyakinan: {confidence:.2%}")
                    if confidence < 0.70:
                        st.warning("Model kurang yakin terhadap hasil prediksi.")
                    st.markdown("##### Probabilitas seluruh kelas")
                    for class_name, probability in zip(CLASS_NAMES, probabilities):
                        st.markdown(
                            f'<div class="prob-row"><span>{DISPLAY_NAMES[class_name]}</span>'
                            f'<strong>{float(probability):.2%}</strong></div>',
                            unsafe_allow_html=True,
                        )
                        st.progress(float(probability))
                except (OSError, ValueError, TypeError) as exc:
                    st.error(f"Prediksi tidak dapat diproses: {exc}")
        st.button("↻ Reset", key="reset_button", on_click=reset_upload, use_container_width=True)

render_footer()
