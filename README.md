
# 📄 ATS Resume Expert

An **AI-powered Applicant Tracking System (ATS) Resume Analyzer** built with **Streamlit** and **OpenAI GPT-4o-mini**.  
This app evaluates resumes (PDFs) against job descriptions and provides:

- ✅ Resume evaluation (strengths & weaknesses)  
- 📊 ATS percentage match  
- 🔑 Missing keywords & improvement suggestions  

![ATS Tracking System Screenshot](https://github.com/Bilal11123/ATS_System/blob/main/docs/screenshot.jpg)
---

## 🚀 Features
- Upload a **PDF resume** (multi-page supported)  
- Paste a **job description**  
- Get an **AI-powered evaluation** from an HR perspective  
- See the **ATS percentage match** and missing keywords  

---

## 🛠️ Tech Stack
- [Python 3.9+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – UI framework  
- [pdf2image](https://pypi.org/project/pdf2image/) – Convert PDFs to images  
- [Pillow](https://pillow.readthedocs.io/) – Image processing  
- [OpenAI Python SDK](https://github.com/openai/openai-python) – GPT-4o-mini API  
- [python-dotenv](https://pypi.org/project/python-dotenv/) – Manage environment variables  

---

## 📂 Project Structure

ATS\_System/
│── app.py          # Main Streamlit app
│── README.md       # Project documentation
│── requirements.txt# Python dependencies
│── .env            # API key storage (not committed to Git)


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/ats-resume-expert.git
cd ats-resume-expert
```

### 2️⃣ Create & activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 5️⃣ Run the app

```bash
streamlit run app.py
```

---

## 📦 Requirements

Example `requirements.txt`:

```
streamlit
openai
pdf2image
pillow
python-dotenv
```

---

## 🖼️ Demo Workflow

1. Paste the job description
2. Upload your resume (`.pdf`)
3. Click **"Tell Me About the Resume"** → AI HR evaluation
4. Click **"Percentage Match"** → ATS score, missing keywords, final thoughts

---

## ⚠️ Notes

* GPT-4o-mini is **multimodal** (understands text + images).
* You should have **poppler** in your system. If you do not have it install from https://github.com/oschwartz10612/poppler-windows/releases/tag/v25.07.0-0 and then add bin path to your system PATH in environment variables.
* Resumes are converted to **images** and passed to the model.
* Currently, only **image-based extraction** is used. (Optional: add OCR for better text accuracy).

---

## 🙌 Acknowledgements

* [OpenAI](https://openai.com/) for GPT-4o-mini
* [Streamlit](https://streamlit.io/) for UI
* [pdf2image](https://github.com/Belval/pdf2image) for PDF conversion

```
