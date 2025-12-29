import streamlit as st
from groq_ai import ai_feedback

st.set_page_config(
    page_title="Accounting Simulator AI",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Accounting Simulator AI")
st.caption("Simulasi laporan keuangan sederhana dengan analisis AI")

# =========================
# Inisialisasi Session State
# =========================
if "financials" not in st.session_state:
    st.session_state.financials = {}

if "ai_result" not in st.session_state:
    st.session_state.ai_result = ""

# =========================
# Input Data Keuangan
# =========================
st.subheader("🧾 Input Data Keuangan")

revenue = st.number_input(
    "Pendapatan (Revenue)",
    min_value=0.0,
    step=100000.0,
    format="%.2f"
)

expenses = st.number_input(
    "Beban (Expenses)",
    min_value=0.0,
    step=100000.0,
    format="%.2f"
)

assets = st.number_input(
    "Total Aset",
    min_value=0.0,
    step=100000.0,
    format="%.2f"
)

liabilities = st.number_input(
    "Total Liabilitas",
    min_value=0.0,
    step=100000.0,
    format="%.2f"
)

# =========================
# Simpan Data
# =========================
if st.button("💾 Simpan Data Keuangan"):
    st.session_state.financials = {
        "Pendapatan": revenue,
        "Beban": expenses,
        "Laba Bersih": revenue - expenses,
        "Total Aset": assets,
        "Total Liabilitas": liabilities,
        "Ekuitas": assets - liabilities
    }
    st.success("Data keuangan berhasil disimpan")

# =========================
# Tampilkan Ringkasan
# =========================
if st.session_state.financials:
    st.subheader("📈 Ringkasan Keuangan")
    st.json(st.session_state.financials)

# =========================
# Analisis AI
# =========================
st.subheader("🤖 Analisis AI Akuntansi")

if st.button("🔍 Analisis dengan AI"):
    if not st.session_state.financials:
        st.warning("Silakan input dan simpan data keuangan terlebih dahulu.")
    else:
        with st.spinner("AI sedang menganalisis laporan keuangan..."):
            try:
                feedback = ai_feedback(st.session_state.financials)
                st.session_state.ai_result = feedback
            except Exception as e:
                st.error("Terjadi kesalahan saat memanggil AI.")
                st.exception(e)

# =========================
# Hasil AI
# =========================
if st.session_state.ai_result:
    st.markdown("### 📌 Hasil Analisis AI")
    st.markdown(st.session_state.ai_result)
