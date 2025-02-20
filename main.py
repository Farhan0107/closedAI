from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Updated list of private universities in India
universities = [
    {"university": "Woxsen University", "location": "Hyderabad", "ranking": 50, "type": "Business, Management, AI, Data Science", "fees": "₹3,50,000", "website": "https://www.woxsen.edu.in"},
    {"university": "Mahindra University", "location": "Hyderabad", "ranking": 55, "type": "Engineering, AI, Robotics", "fees": "₹3,80,000", "website": "https://www.mahindrauniversity.edu.in"},
    {"university": "Vellore Institute of Technology (VIT)", "location": "Vellore", "ranking": 15, "type": "Engineering, AI, Data Science", "fees": "₹2,50,000", "website": "https://www.vit.ac.in"},
    {"university": "Amity University", "location": "Noida", "ranking": 20, "type": "Business, Management, AI, Data Science", "fees": "₹3,00,000", "website": "https://www.amity.edu"},
    {"university": "SRM Institute of Science and Technology", "location": "Chennai", "ranking": 18, "type": "Engineering, AI, Data Science", "fees": "₹2,80,000", "website": "https://www.srmist.edu.in"},
    {"university": "Shiv Nadar University", "location": "Uttar Pradesh", "ranking": 25, "type": "Engineering, Business, AI, Data Science", "fees": "₹3,20,000", "website": "https://www.snu.edu.in"},
    {"university": "Ashoka University", "location": "Sonipat", "ranking": 30, "type": "Liberal Arts, AI, Data Science", "fees": "₹3,40,000", "website": "https://www.ashoka.edu.in"},
    {"university": "BML Munjal University", "location": "Gurgaon", "ranking": 35, "type": "Business, Management, AI", "fees": "₹2,90,000", "website": "https://www.bmu.edu.in"},
    {"university": "Christ University", "location": "Bangalore", "ranking": 40, "type": "Commerce, Business, Data Science", "fees": "₹2,70,000", "website": "https://www.christuniversity.in"},
    {"university": "FLAME University", "location": "Pune", "ranking": 45, "type": "Liberal Arts, Business, AI", "fees": "₹3,60,000", "website": "https://www.flame.edu.in"},
    {"university": "NMIMS University", "location": "Mumbai", "ranking": 22, "type": "Management, AI, Data Science", "fees": "₹3,90,000", "website": "https://www.nmims.edu"},
    {"university": "Symbiosis International University", "location": "Pune", "ranking": 28, "type": "Business, AI, Law", "fees": "₹3,70,000", "website": "https://www.siu.edu.in"},
    {"university": "O.P. Jindal Global University", "location": "Sonipat", "ranking": 33, "type": "Law, Business, AI", "fees": "₹4,00,000", "website": "https://www.jgu.edu.in"},
    {"university": "MIT World Peace University", "location": "Pune", "ranking": 38, "type": "Engineering, AI, Robotics", "fees": "₹3,30,000", "website": "https://mitwpu.edu.in"},
    {"university": "Manav Rachna University", "location": "Faridabad", "ranking": 42, "type": "Engineering, Management, AI", "fees": "₹2,95,000", "website": "https://manavrachna.edu.in"},
    {"university": "Jain University", "location": "Bangalore", "ranking": 48, "type": "Business, Management, AI", "fees": "₹2,85,000", "website": "https://www.jainuniversity.ac.in"},
    {"university": "Kalinga Institute of Industrial Technology (KIIT)", "location": "Bhubaneswar", "ranking": 26, "type": "Engineering, AI, Data Science", "fees": "₹3,40,000", "website": "https://kiit.ac.in"},
    {"university": "UPES University", "location": "Dehradun", "ranking": 31, "type": "Business, AI, Law", "fees": "₹3,20,000", "website": "https://www.upes.ac.in"},
    {"university": "Lovely Professional University (LPU)", "location": "Punjab", "ranking": 27, "type": "Engineering, AI, Data Science", "fees": "₹3,10,000", "website": "https://www.lpu.in"}
]

# ✅ Define UserProfile Model
class UserProfile(BaseModel):
    name: str
    interests: List[str]

# ✅ API Route to Recommend Universities
@app.post("/recommend")
def recommend_universities(user: UserProfile):
    """Recommends universities based on user interests."""
    recommendations = []
    user_interests = set(interest.lower().strip() for interest in user.interests)

    for university in universities:
        uni_type = university["type"].lower()

        # If any user interest matches the university type, add to recommendations
        if any(interest in uni_type for interest in user_interests):
            recommendations.append(university)

    return {"recommendations": recommendations}

# ✅ Root Endpoint to Check Server Status
@app.get("/")
def home():
    return {"message": "University Recommender API is running!"}
