# main.py

import streamlit as st
import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.absolute()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

try:
    from src.allocation import allocate_resources
    from src.visualization import plot_allocation
except ImportError as e:
    st.error(f"Import error: {e}")
    st.error("Please check that all required files are present in the deployment.")
    st.stop()

st.set_page_config(page_title="Medical Resource Allocation Simulator", page_icon="💉")
st.title("Medical Resource Allocation Simulator")

# Number of patients
num_patients = st.slider("Number of patients", 3, 5, 3)

# Input patient data
patients = []
for i in range(num_patients):
    name = f"Patient {i+1}"
    priority = st.number_input(f"{name} priority", min_value=1, max_value=100, value=10, key=f"priority_{i}")
    beds = st.number_input(f"{name} beds needed", min_value=0, max_value=5, value=1, key=f"beds_{i}")
    ventilators = st.number_input(f"{name} ventilators needed", min_value=0, max_value=3, value=1, key=f"vent_{i}")
    monitors = st.number_input(f"{name} monitors needed", min_value=0, max_value=3, value=1, key=f"mon_{i}")
    patients.append({
        "name": name,
        "priority": priority,
        "needs": {"Beds": beds, "Ventilators": ventilators, "Monitors": monitors}
    })

# Total available resources
st.subheader("Total Resources in ICU")
beds_total = st.number_input("Beds", min_value=1, max_value=20, value=5)
vent_total = st.number_input("Ventilators", min_value=0, max_value=10, value=4)
mon_total = st.number_input("Monitors", min_value=0, max_value=10, value=3)
resources = {"Beds": beds_total, "Ventilators": vent_total, "Monitors": mon_total}

# Allocate resources
if st.button("Compute Allocation"):
    allocation = allocate_resources(patients, resources)
    st.success("Resource allocation computed!")

    # Display allocation table
    for p in allocation:
        st.write(f"{p['name']} (Priority {p['priority']}): {p['allocated']}")

    # Plot allocation
    fig = plot_allocation(allocation, patients)
    st.pyplot(fig)
