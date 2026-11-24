# app.py
import streamlit as st
import db_helper
import classical_logic
import default_logic
import fuzzy_logic

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="University Orientation Expert System", page_icon="🎓", layout="wide")

st.title("🎓 University Orientation Expert System")
st.markdown("""
Welcome to the AI-driven orientation system. This tool uses **Classical Logic**, **Default Logic**, and **Fuzzy Logic** to analyze a student's profile and recommend the best academic path.
""")

# --- SIDEBAR: INPUT PROFILE ---
st.sidebar.header("Student Profile Input")
st.sidebar.markdown("Enter the student's academic data below:")

# We create sliders for math and programming (0 to 20)
math_grade = st.sidebar.slider("Math Grade (/20)", min_value=0, max_value=20, value=15)
prog_grade = st.sidebar.slider("Programming Grade (/20)", min_value=0, max_value=20, value=12)

# We create a dropdown for interest
interest = st.sidebar.selectbox("Main Interest", ["AI", "Software", "Cyber"])

# Create the student dictionary based on input
student_profile = {
    "id": "S_custom",
    "name": "Custom Student",
    "math": math_grade,
    "prog": prog_grade,
    "interest": interest
}

# --- MAIN DASHBOARD ---
st.header("Analysis Results")

# Run all three engines
classic_res = classical_logic.evaluate_classical(student_profile)
default_res = default_logic.evaluate_default(student_profile)
fuzzy_res = fuzzy_logic.evaluate_fuzzy(student_profile)

# 1. FINAL RECOMMENDATION (The compare_and_recommend logic, simplified for web)
st.subheader("🏆 Final System Recommendation")

# Find best fuzzy score
fuzzy_scores = {spec: float(val.split('%')[0]) for spec, val in fuzzy_res.items()}
best_spec = max(fuzzy_scores, key=fuzzy_scores.get)
best_score = fuzzy_scores[best_spec]

# Create a nice visual card for the result
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Top Recommended Specialty", value=best_spec)
with col2:
    st.metric(label="Adequacy Score (Fuzzy Logic)", value=f"{best_score}%")
with col3:
    # Check if classical logic agrees
    is_classically_accessible = "Accessible" in classic_res.get(best_spec, "")
    status = "✅ Accessible" if is_classically_accessible else "❌ Strict Rules Failed"
    st.metric(label="Classical Rules Status", value=status)

# Show warnings if default logic retracted
if best_spec in default_res and "Retracted" in default_res[best_spec]:
    st.warning(f"⚠️ **Exception Detected:** {default_res[best_spec]}")

st.divider()

# --- DETAILED RESULTS (Expander) ---
st.subheader("🔍 Detailed Reasoning Breakdown")
st.markdown("See exactly how each AI paradigm evaluated the student.")

tab1, tab2, tab3 = st.tabs(["Strict Classical Logic", "Default Logic (Exceptions)", "Fuzzy Logic (Percentages)"])

with tab1:
    st.write("Classical logic uses hard rules (True/False). It acts as the gatekeeper.")
    for spec, res in classic_res.items():
        if "Accessible" in res:
            st.success(f"**{spec}:** {res}")
        else:
            st.error(f"**{spec}:** {res}")

with tab2:
    st.write("Default logic makes assumptions but revises them if an exception occurs.")
    if not default_res:
        st.info("No default rules were triggered based on the student's interests.")
    for spec, res in default_res.items():
        if "Retracted" in res:
            st.error(f"**{spec}:** {res}")
        else:
            st.info(f"**{spec}:** {res}")

with tab3:
    st.write("Fuzzy logic calculates a 'degree of adequacy' from 0% to 100%.")
    for spec, res in fuzzy_res.items():
        # Extract the number for the progress bar
        score = float(res.split('%')[0])
        st.write(f"**{spec}**")
        st.progress(int(score), text=f"{res}")

st.divider()

# --- DATABASE SECTION ---
st.subheader("🗄️ Database Overview (All Students)")
st.write("This data is loaded dynamically from the SQLite database (`university.db`).")

if st.button("Load Students from Database"):
    students = db_helper.get_all_students()
    
    # Convert dictionary to a list of dicts for a nice table
    table_data = []
    for s_id, s_info in students.items():
        table_data.append({
            "ID": s_id,
            "Name": s_info["name"],
            "Math": s_info["math"],
            "Programming": s_info["prog"],
            "Interest": s_info["interest"]
        })
    
    st.table(table_data)