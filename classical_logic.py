# classical_logic.py
from pyswip import Prolog

prolog = Prolog()
prolog.consult("logic.pl") 

def evaluate_classical(student):
    results = {}
    
    # Get the actual values from the sliders
    m = student["math"]
    p = student["prog"]
    i = student["interest"]
    
    # We will query Prolog directly using the rules, bypassing the need for a student ID
    all_majors = ["Artificial Intelligence", "Software Engineering", "Cybersecurity"]
    
    # Check AI
    # Query: Does Prolog's is_accessible_ai rule return true for these grades?
    if list(prolog.query(f"is_accessible_ai({m}, {p})")):
        results["Artificial Intelligence"] = "Accessible (Derived by Prolog Engine)"
    else:
        results["Artificial Intelligence"] = "Not Accessible (Prolog rules failed)"
        
    # Check Software
    if list(prolog.query(f"is_accessible_software({p})")):
        results["Software Engineering"] = "Accessible (Derived by Prolog Engine)"
    else:
        results["Software Engineering"] = "Not Accessible (Prolog rules failed)"

    # Check Cyber
    # Note: We need to put quotes around the interest string for Prolog
    if list(prolog.query(f"is_accessible_cyber({m}, '{i}')")):
        results["Cybersecurity"] = "Accessible (Derived by Prolog Engine)"
    else:
        results["Cybersecurity"] = "Not Accessible (Prolog rules failed)"

    return results