import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Accounting Simulator AI",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Accounting Simulator AI")
st.caption("Simulasi laporan keuangan berbasis input pemain (Turn-Based)")

# =========================
# INISIALISASI GAME
# =========================
if "month" not in st.session_state:
    st.session_state.month = 1
    st.session_state.cash = 5_000_000
    st.session_state.history = []
    st.session_state.status = "BERJALAN"

# =========================
# STATUS GAME
# =========================
st.subheader("📌 Status Simulasi")

col1, col2, col3 = st.columns(3)
col1.metric("Bulan", st.session_state.month)
col2.metric("Kas", f"Rp {st.session_state.cash:,.0f}")
col3.metric("Status", st.session_state.status)

st.divider()

# =========================
# INPUT PEMAIN
# =========================
st.subheader("✍️ Input Data Keuangan Bulan Ini")

pendapatan = st.number_input(
    "Pendapatan (Rp)",
    min_value=0,
    step=100_000,
    value=1_000_000
)

beban = st.number_input(
    "Total Beban (Rp)",
    min_value=0,
    step=100_000,
    value=800_000
)

aset = st.number_input(
    "Total Aset (Rp)",
    min_value=0,
    step=500_000,
    value=8_000_000
)

liabilitas = st.number_input(
    "Total Liabilitas (Rp)",
    min_value=0,
    step=500_000,
    value=3_000_000
)

# =========================
# PROSES BULAN
# =========================
st.divider()

if st.button("▶️ Jalankan Bulan"):
    laba = pendapatan - beban
    ekuitas = aset - liabilitas

    # Update kas
    st.session_state.cash += laba

    # Simpan riwayat
    st.session_state.history.append({
        "Bulan": st.session_state.month,
        "Pendapatan": pendapatan,
        "Beban": beban,
        "Laba": laba,
        "Aset": aset,
        "Liabilitas": liabilitas,
        "Ekuitas": ekuitas,
        "Kas Akhir": st.session_state.cash
    })

    # Cek bangkrut
    if st.session_state.cash <= 0:
        st.session_state.status = "BANGKRUT"

    st.session_state.month += 1

# =========================
# HASIL BULAN TERAKHIR
# =========================
if st.session_state.history:
    st.subheader("📊 Hasil Bulan Terakhir")
    last = st.session_state.history[-1]

    col1, col2, col3 = st.columns(3)
    col1.metric("Laba Bersih", f"Rp {last['Laba']:,.0f}")
    col2.metric("Ekuitas", f"Rp {last['Ekuitas']:,.0f}")
    col3.metric("Kas Akhir", f"Rp {last['Kas Akhir']:,.0f}")

# =========================
# RIWAYAT SIMULASI
# =========================
if st.session_state.history:
    st.subheader("📜 Riwayat Simulasi")
    st.dataframe(st.session_state.history, use_container_width=True)

# =========================
# GAME OVER
# =========================
if st.session_state.status == "BANGKRUT":
    st.error("💀 Kas habis. Usaha dinyatakan bangkrut.")
