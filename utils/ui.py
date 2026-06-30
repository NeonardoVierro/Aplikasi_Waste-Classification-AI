"""Shared user-interface components for the Streamlit application."""

import streamlit as st


def setup_page(title: str) -> None:
    """Configure page metadata and the responsive visual system."""
    st.set_page_config(page_title=title, page_icon="♻️", layout="wide", initial_sidebar_state="expanded")
    st.markdown(
        """
        <style>
        :root { --green:#169b62; --ink:#13241d; --muted:#61736b; --line:#dbe9e1; }
        .stApp { background:linear-gradient(135deg,#f3faf6 0%,#fff 48%,#eef7f2 100%); }
        .block-container { max-width:1180px; padding:2.4rem 2.4rem 1.5rem; }
        /* Main content uses explicit colors so light/dark browser themes cannot reduce contrast. */
        [data-testid="stMain"] { color:#172820; }
        [data-testid="stMain"] h1,
        [data-testid="stMain"] h2,
        [data-testid="stMain"] h3 { color:#103e2e !important; }
        [data-testid="stMain"] .stMarkdown p,
        [data-testid="stMain"] .stMarkdown li { color:#31483e; }
        [data-testid="stMain"] .stMarkdown strong { color:#173f30; }
        [data-testid="stMain"] [data-testid="stMetric"] {
          color:#172820; background:rgba(255,255,255,.86); border-color:#cfe3d8; border-radius:16px;
          box-shadow:0 8px 24px rgba(17,78,51,.06);
        }
        [data-testid="stMain"] [data-testid="stMetricLabel"] p { color:#52675e !important; }
        [data-testid="stMain"] [data-testid="stMetricValue"] { color:#0b6543 !important; }
        [data-testid="stMain"] [data-testid="stCaptionContainer"] p { color:#5a6d64 !important; }
        [data-testid="stMain"] [data-testid="stAlert"] p { color:#173f30 !important; }
        .hero { position:relative; overflow:hidden; padding:2.6rem 2.7rem; border-radius:28px; color:#fff;
          background:linear-gradient(120deg,#092f23 0%,#0d6847 64%,#1aa96e 100%); margin-bottom:1.6rem;
          box-shadow:0 24px 60px rgba(9,72,47,.18); }
        .hero:after { content:""; position:absolute; width:260px; height:260px; right:-70px; top:-110px;
          border:42px solid rgba(255,255,255,.09); border-radius:50%; }
        [data-testid="stMain"] .stMarkdown .hero h1 {
          position:relative; color:#ffffff !important; font-size:clamp(2.25rem,5vw,3.8rem);
          line-height:1.04; margin:.6rem 0 .8rem; letter-spacing:-.045em;
          text-shadow:0 2px 18px rgba(0,0,0,.18);
        }
        [data-testid="stMain"] .stMarkdown .hero p {
          position:relative; color:#d9f7e8 !important; font-size:1.08rem;
          line-height:1.65; max-width:720px; margin:0;
        }
        .eyebrow { position:relative; font-size:.72rem; letter-spacing:.19em; font-weight:800; color:#9fe4c1; }
        .section-label { color:var(--ink); font-size:1rem; font-weight:750; margin:1.25rem 0 .5rem; }
        /* Explicit panel titles avoid inheriting an unreadable Streamlit theme color. */
        .panel-title {
          color:#0a4f36 !important; font-size:1.2rem; line-height:1.4;
          font-weight:800; letter-spacing:-.015em; margin:.15rem 0 .8rem;
        }
        .hint-card { display:flex; gap:.8rem; align-items:flex-start; padding:1rem 1.15rem; margin-top:.8rem;
          border:1px solid var(--line); border-radius:15px; color:var(--muted); background:rgba(255,255,255,.74); }
        .result-card { padding:1.5rem; border:1px solid #cde8da; border-radius:20px; background:#fff; margin-bottom:1rem;
          box-shadow:0 14px 40px rgba(10,86,48,.09); }
        .result-card span { color:var(--muted); font-size:.72rem; letter-spacing:.12em; font-weight:700; }
        .result-card h2 { color:var(--ink); margin:.3rem 0; font-size:2rem; }
        .result-card strong { color:var(--green); }
        .prob-row { display:flex; justify-content:space-between; color:var(--ink); margin:.8rem 0 .25rem; font-size:.94rem; }
        .footer { text-align:center; color:#718078; border-top:1px solid #dae9e1; margin-top:3.5rem; padding:1.7rem 0 .4rem; font-size:.88rem; }
        [data-testid="stSidebar"] { background:linear-gradient(180deg,#0c2c22 0%,#103d2e 100%); border-right:0; }
        [data-testid="stSidebar"] * { color:#eefaf4; }
        [data-testid="stSidebar"] [data-testid="stCaptionContainer"] p { color:#a9c9bb; }
        [data-testid="stSidebar"] [data-testid="stMetric"] { background:rgba(255,255,255,.07); border-color:rgba(255,255,255,.12); border-radius:14px; }
        [data-testid="stFileUploaderDropzone"] { border:1.5px dashed #52ae82; border-radius:18px; background:rgba(255,255,255,.8); padding:1.25rem; }
        [data-testid="stFileUploaderDropzone"] button { background:#e4f5ec; color:#0c6845; border:0; }
        [data-testid="stImage"] img { border-radius:18px; box-shadow:0 12px 35px rgba(22,60,43,.12); }
        .stProgress > div > div > div > div { background:linear-gradient(90deg,#1bb874,#0d8053); }
        /* Reset button: strong contrast in normal, hover, focus, and active states. */
        .stButton button {
          min-height:2.8rem; border-radius:12px; font-weight:750;
          color:#0b6543 !important; background:#e6f5ed !important; border:1px solid #75bf9b !important;
          transition:background-color .18s ease,color .18s ease,border-color .18s ease,transform .18s ease;
        }
        .stButton button:hover {
          color:#fff !important; background:#117a50 !important; border-color:#117a50 !important;
          transform:translateY(-1px); box-shadow:0 8px 20px rgba(17,122,80,.20);
        }
        .stButton button:focus { color:#fff !important; background:#117a50 !important; border-color:#7ad7ad !important; }
        .stButton button:active { background:#0b5c3c !important; transform:translateY(0); }
        .stButton button p { color:inherit !important; }
        /* Dedicated Reset selector wins over theme-specific button rules. */
        .st-key-reset_button button {
          color:#0a4f36 !important; background:#dff3e8 !important; border:1px solid #54ad80 !important;
        }
        .st-key-reset_button button:hover {
          color:#ffffff !important; background:#075f3e !important; border-color:#075f3e !important;
          box-shadow:0 9px 22px rgba(7,95,62,.28);
        }
        .st-key-reset_button button:hover p { color:#ffffff !important; }
        .st-key-reset_button button:active { color:#ffffff !important; background:#043f2a !important; }
        @media (max-width:700px) {
          .block-container { padding:1.2rem 1rem; }
          .hero { padding:2rem 1.35rem; border-radius:21px; }
          .hero h1 { font-size:2.25rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    """Render concise project, dataset, and model information."""
    with st.sidebar:
        st.title("♻️ Waste AI")
        st.caption("Artificial Intelligence for Education")
        st.divider()
        st.markdown("**Nama Kelompok**  \nKelompok Tadinya Mesra")
        st.markdown("**Dataset - 150 gambar**  \n🌿 Organik  \n♻️ Anorganik  \n⚠️ B3")
        st.divider()
        st.markdown("**Perbandingan model**")
        st.metric("CNN From Scratch", "93%", border=True)
        st.metric("MobileNetV2", "100%", border=True)
        st.success("Model aktif: MobileNetV2")


def render_footer() -> None:
    """Render the development credit at the bottom of a page."""
    st.markdown(
        '<footer class="footer">Developed by <strong>Kelompok Tadinya Mesra</strong><br>Neonardo Vierro (K3523057)<br>Rifaldy Ilham (K3523058)<br>Universitas Sebelas Maret</footer>',
        unsafe_allow_html=True,
    )
