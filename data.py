# data.py

# 10 different student profiles
# Scores are out of 20. 
# Note: Some are intentionally missing data (e.g., prog = None) to test the "Validate Profile" step!

STUDENT_PROFILES = {
    "S1": {"name": "Alice", "math": 18, "prog": 16, "interest": "AI"},
    "S2": {"name": "Bob", "math": 10, "prog": 12, "interest": "Cyber"},
    "S3": {"name": "Charlie", "math": 14, "prog": 14, "interest": "Software"},
    "S4": {"name": "David", "math": 8,  "prog": 18, "interest": "Software"}, # Good at coding, bad at math
    "S5": {"name": "Eve", "math": 19, "prog": 19, "interest": "AI"},
    "S6": {"name": "Frank", "math": 12, "prog": 9,  "interest": "Cyber"},
    "S7": {"name": "Grace", "math": 15, "prog": 10, "interest": "AI"},
    "S8": {"name": "Heidi", "math": 9,  "prog": 9,  "interest": "Software"},
    "S9": {"name": "Ivan", "math": 16, "prog": None, "interest": "Cyber"}, # Missing programming grade!
    "S10": {"name": "Judy", "math": 11, "prog": 15, "interest": "AI"}
}

# The specializations the school offers
SPECIALTIES = ["Artificial Intelligence", "Software Engineering", "Cybersecurity"]