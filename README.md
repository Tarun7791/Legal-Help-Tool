# 🌐 Legal Help Tool – Local Language Based Legal Assistance

A simple and powerful web application that helps users get legal assistance in their local language (Hinglish/Hindi/English).  
User enters their query → backend translates it → identifies case type → generates a proper legal document format.

This project is created for Hackathons / College Projects / Real-World Prototypes.

---

## 🚀 Features

### 🔹 1. Local Language Input  
Users can type in:
- Hinglish  
- Hindi  
- English  

### 🔹 2. Automatic Translation  
Backend (FastAPI) converts user input into proper English using Google Translate API.

### 🔹 3. Case Classification  
App identifies the type of case:
- FIR / Complaint  
- Consumer Issue  
- Family Law  
- Property Dispute  
- Employment Issue  
- Criminal Defense  
- And more…

### 🔹 4. Legal Document Generator  
Generates a clean legal application/letter:
- Proper format  
- Professional language  
- Easy to download/use  

### 🔹 5. Interactive UI  
- Clean modern website  
- Search box  
- Service cards  
- Multi-language support (English/Hindi)

### 🔹 6. One-Click Card Suggestions  
Clicking on any "Available Service" card auto-fills relevant example query.

---

## 🛠 Tech Stack

### *Frontend*
- HTML  
- CSS  
- JavaScript  
- Fully responsive UI  
- Multi-language support (English/Hindi)

### *Backend*
- Python  
- FastAPI  
- Googletrans (Translation)
- Simple NLP logic

### *Deployment (Optional)*
- Frontend → Vercel  
- Backend → Railway  
- GitHub for version control  

---

## 📁 Project Structure

legalproject/ │ ├── index.html        # Frontend UI │ └── backend/ └── main.py     # FastAPI backend

---

## ▶ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/legal-help-tool
cd legal-help-tool/backend

2. Install Dependencies

pip install fastapi uvicorn googletrans==4.0.0-rc1

3. Run Backend Server

python -m uvicorn main:app --reload

Backend starts at:

http://127.0.0.1:8000

4. Open Frontend

Simply open index.html in your browser.


---

🌐 API Endpoint

POST /process

Request:

{
  "text": "mujhe police me complaint likhni hai"
}

Response:

{
  "translated": "I have to file a complaint with the police",
  "case_type": "FIR / Complaint",
  "legal_text": "Generated formatted legal application..."
}


---

📸 Demo (For Hackathon Presentation)

🔹 Step 1 – User enters query

"Hinglish or Hindi text"

🔹 Step 2 – Backend processes

✔ Translation
✔ Case detection
✔ Legal template created

🔹 Step 3 – Output

A clean professional legal application.


---

👥 Team Roles (Add Your Members)

Name	Role

Aaditya	Backend + Integration
Member 2	Frontend
Member 3	UI/UX
Member 4	Presentation



---

⭐ Future Improvements

PDF download option

Voice-to-text input

More languages (Marathi, Tamil, Telugu)

Machine learning model for case classification



---

❤ Thanks for Checking Our Project!

This tool is created to help common people understand and generate basic legal applications using their preferred language.
