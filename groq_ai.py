from groq import Groq
import streamlit as st

def ai_feedback(financials):
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    prompt = f"""
    Anda adalah Accounting Coach.
    Data keuangan saat ini:
    Kas: {financials['cash']}
    Pendapatan: {financials['revenue']}
    Beban: {financials['expense']}

    Jelaskan kondisi keuangan ini secara sederhana dan beri saran.
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "Anda adalah asisten akuntansi yang ramah dan edukatif."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=300
    )

    return response.choices[0].message.content
