# main.py
import db_helper
import classical_logic
import default_logic
import fuzzy_logic

def validate_profile(student):
    missing = []
    if student["math"] is None: missing.append("Math Grade")
    if student["prog"] is None: missing.append("Programming Grade")
    
    if missing:
        return False, f"Missing data: {', '.join(missing)}"
    return True, "Profile Complete"

# NEW: The Comparison Engine
def compare_and_recommend(classic_res, default_res, fuzzy_res):
    final_report = []
    
    # Extract the numeric values from the fuzzy logic strings (e.g., "85.0% Adequacy" -> 85.0)
    fuzzy_scores = {}
    for spec, val in fuzzy_res.items():
        score = float(val.split('%')[0])
        fuzzy_scores[spec] = score
        
    # Sort the specialties by their Fuzzy score (highest first)
    sorted_specs = sorted(fuzzy_scores, key=fuzzy_scores.get, reverse=True)
    
    best_spec = sorted_specs[0]
    best_score = fuzzy_scores[best_spec]
    
    # Decision Matrix
    final_report.append(f"  [🏆] TOP RECOMMENDATION: {best_spec} (Adequacy: {best_score}%)")
    
    # Check Classical Logic for the Top Recommendation
    classic_status = classic_res.get(best_spec, "Unknown")
    if "Not Accessible" in classic_status:
        final_report.append(f"  [⚠️] WARNING: Despite high potential, strict academic rules say this is currently NOT accessible.")
        final_report.append(f"      -> Reason: {classic_status}")
    else:
        final_report.append(f"  [✅] Classical Rules: You meet the strict requirements for this major.")
        
    # Check Default Logic for Exceptions
    if best_spec in default_res:
        default_status = default_res[best_spec]
        if "Retracted" in default_status:
            final_report.append(f"  [⚠️] EXCEPTION DETECTED: {default_status}")
        else:
            final_report.append(f"  [✅] Default Assumption: You fit the typical profile for this major.")
            
    # Provide a backup option
    if len(sorted_specs) > 1:
        backup_spec = sorted_specs[1]
        final_report.append(f"\n  [🔄] SECONDARY OPTION: {backup_spec} (Adequacy: {fuzzy_scores[backup_spec]}%)")
        backup_status = classic_res.get(backup_spec, "")
        if "Not Accessible" not in backup_status:
            final_report.append(f"      -> This is a safe backup! You meet the classical requirements.")

    return "\n".join(final_report)

def run_system():
    print("===================================================")
    print("   UNIVERSITY ORIENTATION EXPERT SYSTEM (SQLite)")
    print("===================================================\n")

    students = db_helper.get_all_students()

    for student_id, profile in students.items():
        print(f"--- Analyzing Student: {profile['name']} ({student_id}) ---")
        print(f"Facts -> Math: {profile['math']}/20 | Prog: {profile['prog']}/20 | Interest: {profile['interest']}")
        
        is_valid, message = validate_profile(profile)
        if not is_valid:
            print(f"[!] WARNING: {message}. Results may be inaccurate.\n")
        else:
            print("[+] Profile Validated.\n")
            
        # 1. Run Engines
        classic_res = classical_logic.evaluate_classical(profile)
        default_res = default_logic.evaluate_default(profile)
        fuzzy_res = fuzzy_logic.evaluate_fuzzy(profile)
        
        # Print detailed raw results (for the technical report)
        print(">>> [1] Classical Reasoning Results:")
        for spec, res in classic_res.items():
            print(f"    - {spec}: {res}")
            
        print("\n>>> [2] Default Reasoning Results:")
        if not default_res:
             print("    - No default rules triggered.")
        for spec, res in default_res.items():
            print(f"    - {spec}: {res}")
            
        print("\n>>> [3] Fuzzy Logic Results:")
        for spec, res in fuzzy_res.items():
            print(f"    - {spec}: {res}")
            
        print("\n>>> [4] FINAL SYSTEM REPORT (Comparison Engine):")
        final_conclusion = compare_and_recommend(classic_res, default_res, fuzzy_res)
        print(final_conclusion)
            
        print("---------------------------------------------------\n")

if __name__ == "__main__":
    run_system()