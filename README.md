# ♻️ AI Waste Classification

Aplikasi Streamlit untuk mengklasifikasikan **daun pepaya (organik)**, **botol Le Minerale 600 ml (anorganik)**, dan **kemasan Roundup (B3)** menggunakan Transfer Learning MobileNetV2.

## Persyaratan

- Python 3.12
- Model `models/model_transfer_learning_mobilenetv2_terbaik.keras`

## Cara install

```bash
python -m venv .venv
```

Aktifkan virtual environment di Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Kemudian instal dependensi:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Cara menjalankan

```bash
streamlit run app.py
```

Browser akan membuka aplikasi pada `http://localhost:8501`.

## Deploy ke Streamlit Community Cloud

1. Push seluruh proyek, termasuk folder `models`, ke repository GitHub.
2. Masuk ke Streamlit Community Cloud dan pilih **Create app**.
3. Pilih repository, branch, dan isi main file path dengan `app.py`.
4. Pastikan versi Python deployment adalah 3.12, lalu deploy.

Model berukuran sekitar 12 MB sehingga masih dapat disimpan langsung dalam repository GitHub. Aplikasi menggunakan `@st.cache_resource` agar model hanya dimuat sekali per proses.

## Struktur proyek

```text
.
├── app.py
├── models/
│   └── model_transfer_learning_mobilenetv2_terbaik.keras
├── pages/
│   └── About.py
├── utils/
│   ├── __init__.py
│   ├── preprocessing.py
│   └── ui.py
├── requirements.txt
├── runtime.txt
└── README.md
```

Urutan kelas (`daun_pepaya`, `le_minerale`, `roundup_b3`) dan preprocessing MobileNetV2 (`224×224` + `preprocess_input`) mengikuti notebook training.
