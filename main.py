from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from deep_translator import GoogleTranslator


app = FastAPI()

# CORS so frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# ----------------- TEMPLATES (ENGLISH) -----------------
templates_en = {
    "FIR / Complaint": """
To,
The Officer-in-Charge,
[Police Station Name]

Subject: Complaint Regarding: {translated}

Respected Sir/Madam,

I would like to bring the following matter to your attention:

{translated}

Therefore, I request you to kindly take appropriate legal action as per the provisions of the law.

Sincerely,
User
Date: __________
""",
    "Property Issue": """
To,
The Rent Control Authority / Property Department,
[City/State]

Subject: Property Related Issue

Respected Sir/Madam,

I would like to submit the following issue for your consideration:

{translated}

Kindly take the necessary action as per the applicable property laws.

Sincerely,
User
Date: __________
""",
    "General Legal Issue": """
To,
The Concerned Authority,

Subject: Request for Legal Assistance

Respected Sir/Madam,

I wish to bring the following matter to your notice:

{translated}

I request you to kindly provide guidance and take action as per the law.

Sincerely,
User
Date: __________
"""
}

# ----------------- TEMPLATES (HINDI) -----------------
templates_hi = {
    "FIR / Complaint": """
सेवा में,
थाना प्रभारी,
[थाने का नाम]

विषय: शिकायत – {translated} संबंधी

महोदय/महोदया,

मैं आपका ध्यान निम्नलिखित प्रकरण की ओर आकर्षित करना चाहता/चाहती हूँ:

{translated}

अतः आपसे विनम्र निवेदन है कि कृपया प्रचलित कानून के अनुसार आवश्यक कानूनी कार्यवाही करने की कृपा करें।

भवदीय,
उपयोगकर्ता
दिनांक: __________
""",
    "Property Issue": """
सेवा में,
किराया नियंत्रण प्राधिकरण / संपत्ति विभाग,
[शहर/राज्य]

विषय: संपत्ति से संबंधित समस्या के संबंध में आवेदन

महोदय/महोदया,

मैं निम्नलिखित संपत्ति संबंधी समस्या आपके संज्ञान में लाना चाहता/चाहती हूँ:

{translated}

आपसे निवेदन है कि कृपया प्रचलित संपत्ति कानूनों के अनुसार आवश्यक कार्यवाही करने की कृपा करें।

भवदीय,
उपयोगकर्ता
दिनांक: __________
""",
    "General Legal Issue": """
सेवा में,
संबंधित अधिकारी महोदय/महोदया,

विषय: कानूनी सहायता के लिए निवेदन

महोदय/महोदया,

मैं निम्नलिखित विषय के संबंध में कानूनी सहायता चाहता/चाहती हूँ:

{translated}

कृपया प्रचलित कानूनों के अनुसार मार्गदर्शन करने एवं आवश्यक कार्यवाही करने की कृपा करें।

भवदीय,
उपयोगकर्ता
दिनांक: __________
"""
}

# ----------------- CASE CLASSIFICATION -----------------
def classify_case(text: str) -> str:
    t = text.lower()
    if "police" in t or "complaint" in t or "fir" in t or "dhamki" in t or "threat" in t:
        return "FIR / Complaint"
    if "property" in t or "land" in t or "zameen" in t or "plot" in t:
        return "Property Issue"
    return "General Legal Issue"

# ----------------- REQUEST MODEL -----------------
class InputText(BaseModel):
    text: str
    lang: Optional[str] = "en"   # "en" ya "hi"

# ----------------- MAIN API -----------------
@app.post("/process")
def process_text(data: InputText):
    raw_text = data.text
    lang = (data.lang or "en").lower()

    # Hinglish/local → English
   translated = GoogleTranslator(source='auto', target='en').translate(raw_text)

    case_type = classify_case(raw_text)

    if lang == "hi":
        template = templates_hi.get(case_type, templates_hi["General Legal Issue"])
    else:
        template = templates_en.get(case_type, templates_en["General Legal Issue"])

    legal_text = template.format(translated=translated)

    return {
        "translated": translated,
        "case_type": case_type,
        "legal_text": legal_text
    }

# ----------------- ROOT TEST -----------------
@app.get("/")
def home():

    return {"message": "Legal Help Tool Backend is Running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)

