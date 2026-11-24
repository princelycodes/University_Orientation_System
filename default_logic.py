# default_logic.py

def evaluate_default(student):
    results = {}
    interest = student["interest"]
    math = student["math"]
    prog = student["prog"]
    
    # Default Rule 1: If they like AI, we ASSUME they are suited for it.
    if interest == "AI":
        results["Artificial Intelligence"] = "Provisionally Recommended (Default)"
        # Exception Check: If math is bad, we RETRACT the conclusion.
        if math is not None and math < 10:
            results["Artificial Intelligence"] = "Retracted (Exception: Math too low)"
            
    # Default Rule 2: If they like Software, assume they are good at coding.
    elif interest == "Software":
        results["Software Engineering"] = "Provisionally Recommended (Default)"
        if prog is not None and prog < 8:
            results["Software Engineering"] = "Retracted (Exception: Coding skills too low)"
            
    # Default Rule 3: If they like Cyber, assume they are good at it.
    elif interest == "Cyber":
        results["Cybersecurity"] = "Provisionally Recommended (Default)"
        if math is not None and math < 8:
            results["Cybersecurity"] = "Retracted (Exception: Math too low)"
            
    return results