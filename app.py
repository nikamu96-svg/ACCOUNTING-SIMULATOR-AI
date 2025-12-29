import streamlit as st
from accounting import init_financials, profit_loss
from simulator import make_decision
from groq_ai import ai_feedback

st.set_page_config(page_title="Accounting Simulator AI", layout="centered")

st.title("🎮 Accounting Simulator AI")

if "financials" not in st.session_state:
    st.session_state.financials = init_financials()

st.subheader("📊 Dashboard Keuangan")
st.write("Kas:", f"Rp{st.session_state.financials['cash']:,}")
st.write("Pendapatan:", f"Rp{st.session_state.financials['revenue']:,}")
st.write("Beban:", f"Rp{st.session_state.financials['expense']:,}")
st.write("Laba / Rugi:", f"Rp{profit_loss(st.session_state.financials):,}")

st.divider()

st.subheader("🕹️ Ambil Keputusan")
decision = st.selectbox("Pilih keputusan:", ["Penjualan", "Biaya Operasional"])
amount = st.number_input("Masukkan nominal:", min_value=0, step=10000)

if st.button("Proses Keputusan"):
    st.session_state.financials, msg = make_decision(
        st.session_state.financials,
        decision,
        amount
    )
    st.success(msg)

st.divider()

st.subheader("🤖 AI Accounting Coach")
if st.button("Minta Analisis AI"):
    with st.spinner("AI sedang menganalisis..."):
        feedback = ai_feedback(st.session_state.financials)
    st.info(feedback)
