import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_feedback(financials: dict) -> str:
    # Ubah data ke teks (WAJIB)
    data_text = "\n".join([f"{k}: {v}" for k, v in financials.items()])

    prompt = f"""
    Anda adalah seorang analis akuntansi profesional.

    Berikut adalah data keuangan sebuah usaha:
    {data_text}

    Tolong berikan:
    1. Analisis kondisi keuangan
    2. Penilaian kinerja usaha
    3. Saran perbaikan secara akuntansi
    Gunakan bahasa yang jelas dan edukatif.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ MODEL BARU
            messages=[
                {"role": "system", "content": "You are an accounting expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=400
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Groq API Error: {e}"
