from dotenv import load_dotenv
import openai
import os
import base64
import io
import pdf2image
import streamlit as st
from PIL import Image

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ---- PDF Setup (multi-page support) ----
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert PDF to images
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        pdf_parts = []
        for page in images:
            img_byte_arr = io.BytesIO()
            page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts.append({
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            })
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# ---- OpenAI Response ----
def get_openai_response(instruction, pdf_content, job_description):
    client = openai.OpenAI()

    # Build user message content with job description + all resume pages
    user_content = [{"type": "text", "text": job_description}]
    for page in pdf_content:
        user_content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{page['data']}"}
        })

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # GPT-4o-mini supports text + vision
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": user_content}
        ]
    )

    return response.choices[0].message.content

# ---- Streamlit App ----
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("✅ PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")

# Prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager. 
Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. 
Give me the percentage of match if the resume matches the job description. 
First the output should come as percentage, then keywords missing, and finally final thoughts.
"""

# Actions
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_openai_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("⚠ Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_openai_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("⚠ Please upload the resume")