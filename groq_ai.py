import streamlit as st
from groq import Groq

def ai_feedback(financials):
    if "GROQ_API_KEY" not in st.secrets:
        return "❌ GROQ_API_KEY belum diset di Streamlit Secrets."

    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    prompt = f"""
Anda adalah Accounting Coach yang ramah dan edukatif.

Data keuangan:
Kas: Rp{financials['cash']:,}
Pendapatan: Rp{financials['revenue']:,}
Beban: Rp{financials['expense']:,}

Tolong jelaskan kondisi keuangan dan beri 1 saran singkat.
"""

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "Anda adalah asisten akuntansi."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=250
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error Groq API: {e}"
