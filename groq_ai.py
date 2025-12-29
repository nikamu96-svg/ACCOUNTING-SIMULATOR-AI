import streamlit as st
from groq import Groq

def ai_feedback(financials):
    # 1. Pastikan API key ada
    if "GROQ_API_KEY" not in st.secrets:
        return "❌ GROQ_API_KEY belum diset di Streamlit Secrets."

    # 2. Buat client DI DALAM fungsi
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    # 3. Prompt SUPER SEDERHANA (ANTI BAD REQUEST)
    prompt = (
        f"Kas: {financials['cash']}\n"
        f"Pendapatan: {financials['revenue']}\n"
        f"Beban: {financials['expense']}\n\n"
        "Jelaskan kondisi keuangan secara singkat dan beri satu saran."
    )

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4,
            max_tokens=200
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Groq API Error: {str(e)}"
