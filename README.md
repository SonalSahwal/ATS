### **Smart ATS Resume Evaluator**  
**Enhance your resume for better ATS compatibility!**  

![ATS Resume Evaluator](https://img.shields.io/badge/ATS%20Resume%20Evaluator-Optimize%20Your%20Resume-blue)  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)  
![Gemini AI](https://img.shields.io/badge/Gemini%20AI-API-green)  



### **Overview**  
**Smart ATS Resume Evaluator** is a **Streamlit-powered web application** that helps job seekers **optimize** their resumes based on **job descriptions**. Using **Google Gemini AI**, the app:  

- Analyzes resumes against job descriptions  
- Assigns a **Job Description Match Score**   
- Identifies **Missing keywords** 
- Provides **personalized feedback** & improvement suggestions  

**Goal:** Improve ATS (Applicant Tracking System) compatibility and increase hiring chances!  



### **Tech Stack**  
- **Python** 
- **Streamlit**  
- **Google Gemini AI (Generative AI)** 
- **PyPDF2 (PDF Parsing)** 
- **JSON Processing & Regex Handling**  



### **Installation & Setup**  

#### **Clone the Repository**  
```sh
git clone https://github.com/your-username/smart-ats-resume-evaluator.git
cd smart-ats-resume-evaluator
```

#### **Create & Activate a Virtual Environment**  
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

#### **Install Dependencies**  
```sh
pip install -r requirements.txt
```

#### **Set Up Environment Variables**  
Create a `.env` file and add your **Google Gemini API key**:  
```sh
GOOGLE_API_KEY=your_api_key_here
```

#### **Run the Application**  
```sh
streamlit run app.py
```


### **Features**  
**Job Description Match Score** – Displays a **progress bar** with a % match  
**Missing Keywords** – Identifies important **keywords** to add  
**Profile Summary** – AI-generated **feedback** & improvement tips  
**PDF Resume Parsing** – Extracts text & analyzes content  
**User-Friendly Interface** – Built with **Streamlit** for easy use  


### **How It Works?**  
**Upload** your resume (PDF format)  
**Paste** the job description  
Click **"Evaluate Resume"**
**Get instant insights!**  

---

### **Troubleshooting**  

**Invalid API Key?**  
- Ensure `GOOGLE_API_KEY` is correct in `.env`  
- Restart the app: `streamlit run app.py`  

**Parsing Errors?**  
- Check the **Gemini AI response** (error logs will display raw output)  
- Adjust prompt formatting  

