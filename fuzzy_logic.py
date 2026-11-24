# fuzzy_logic.py

def evaluate_fuzzy(student):
    results = {}
    math = student["math"]
    prog = student["prog"]
    
    # Handle missing data (e.g., Ivan missing prog)
    if math is None: math = 10 # Assume average if missing
    if prog is None: prog = 10
    
    # Convert to percentages (0.0 to 1.0)
    math_score = math / 20.0
    prog_score = prog / 20.0
    
    # FUZZY RULES:
    # AI needs high math AND high prog
    ai_degree = (math_score * 0.6) + (prog_score * 0.4) 
    
    # Software needs mostly prog
    software_degree = (prog_score * 0.8) + (math_score * 0.2)
    
    # Cyber needs math and interest in security
    # We add a bonus if they actually like it
    cyber_degree = (math_score * 0.7) + (0.3 if student["interest"] == "Cyber" else 0.0)
    
    # Format as percentages
    results["Artificial Intelligence"] = f"{ai_degree * 100:.1f}% Adequacy"
    results["Software Engineering"] = f"{software_degree * 100:.1f}% Adequacy"
    results["Cybersecurity"] = f"{cyber_degree * 100:.1f}% Adequacy"
    
    return results