import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import re  # For extracting JSON from AI response

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini AI
def get_gemini_response(input_prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input_prompt)
    return response.text.strip()  # Strip extra spaces/newlines

# Function to extract text from a PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += str(reader.pages[page].extract_text())
    return text

# Function to extract JSON from AI response using regex
def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)  # Extracts content between first and last {}
    if match:
        return match.group(0)
    return None  # Return None if no valid JSON found

# Streamlit UI
st.title("📄 Smart ATS Resume Evaluator")
st.markdown("**Enhance your resume for better ATS compatibility!**")

# Job description input
jd = st.text_area("📌 Paste the Job Description", height=200)

# Resume upload
uploaded_file = st.file_uploader("📂 Upload Your Resume (PDF only)", type=["pdf"], help="Upload your resume in PDF format.")

# Submit button
submit = st.button("🔍 Evaluate Resume")

if submit:
    if uploaded_file is not None:
        # Extract text from PDF
        resume_text = input_pdf_text(uploaded_file)

        # Create input prompt for AI
        input_prompt = f"""
        You are an advanced ATS (Applicant Tracking System) specializing in software engineering, 
        data science, analytics, and big data. Evaluate the resume against the job description and:
        - Assign a **Job Description (JD) Match Percentage**.
        - List **missing keywords** crucial for this job.
        - Provide a brief **profile summary** of the candidate's strengths and gaps.

        Respond in **EXACTLY this JSON format without extra text**:
        {{"JD Match":"%", "MissingKeywords":[], "Profile Summary":""}}

        Resume: {resume_text}
        Job Description: {jd}
        """

        # Get AI response
        response = get_gemini_response(input_prompt)

        # Extract JSON from response
        json_text = extract_json(response)

        if json_text:
            try:
                # Parse JSON response
                parsed_response = json.loads(json_text)

                # Extract response data
                jd_match = int(parsed_response.get("JD Match", "0").replace("%", ""))
                missing_keywords = parsed_response.get("MissingKeywords", [])
                profile_summary = parsed_response.get("Profile Summary", "No summary available.")

                # Display JD Match Percentage
                st.subheader("📊 Job Description Match Score")
                st.progress(jd_match / 100)  # Convert percentage to decimal for progress bar
                st.write(f"**Match Percentage:** {jd_match}%")

                # Display Missing Keywords
                if missing_keywords:
                    st.subheader("🔑 Missing Keywords")
                    st.warning("Consider adding these keywords to optimize your resume:")
                    st.markdown("- " + "\n- ".join(missing_keywords))  # Bullet-point format
                else:
                    st.success("✅ Your resume contains all necessary keywords!")

                # Display Profile Summary
                st.subheader("📌 Profile Summary")
                st.info(profile_summary)

            except json.JSONDecodeError:
                st.error("⚠️ Error: The AI response was not valid JSON. Please try again.")
                st.text("Raw AI Response:")  # Debugging step
                st.code(response, language="json")

        else:
            st.error("⚠️ Error: Could not extract JSON from AI response. Please try again.")
            st.text("Raw AI Response:")  # Debugging step
            st.code(response, language="json")

    else:
        st.warning("⚠️ Please upload a resume before submitting.")
