from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_feedback(financials):
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
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )

    return response.choices[0].message.content
