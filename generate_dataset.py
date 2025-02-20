import pandas as pd
import random

# Sample university names
universities = [
    "Indian Institute of Technology Bombay", "Indian Institute of Science Bangalore", 
    "Delhi University", "Jawaharlal Nehru University", "Banaras Hindu University",
    "University of Mumbai", "Indian Institute of Technology Madras", 
    "Indian Institute of Technology Delhi", "University of Calcutta", 
    "Jadavpur University", "University of Hyderabad", "Anna University", 
    "Panjab University", "Savitribai Phule Pune University", "Aligarh Muslim University",
    "Jamia Millia Islamia", "Vellore Institute of Technology", "Amity University",
    "Indian Institute of Management Ahmedabad", "BITS Pilani"
]

# Sample cities
cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune", "Ahmedabad", "Lucknow", "Patna"]

# Sample course categories
course_categories = [
    "Engineering, Computer Science, AI & ML", 
    "Medicine, Pharmacy, Biotechnology", 
    "Business, Management, Finance", 
    "Arts, Humanities, Literature", 
    "Law, Political Science, Public Policy",
    "Science, Physics, Chemistry, Biology"
]

# Generate 200 sample university data
data = []
for _ in range(200):
    university = random.choice(universities) + " " + str(random.randint(1, 20))  # Unique variations
    city = random.choice(cities)
    ranking = random.randint(1, 200)  # Random ranking
    courses = random.choice(course_categories)  # Random course category
    fees = random.randint(50000, 500000)  # Random tuition fees in INR
    website = f"https://{university.replace(' ', '').lower()}.edu.in"  # Mock website

    data.append([university, city, ranking, courses, fees, website])

# Create DataFrame
df = pd.DataFrame(data, columns=["University Name", "City", "Ranking", "Courses Offered", "Tuition Fees", "Website"])

# Save as Excel file
df.to_excel("universities_dataset.xlsx", index=False)

print("universities_dataset.xlsx has been created successfully!")
