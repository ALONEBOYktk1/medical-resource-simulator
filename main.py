# main.py

import streamlit as st
from src.allocation import knapsack
from src.visualization import plot_allocation

st.set_page_config(page_title="Medical Resource Allocation Simulator", page_icon="💉")
st.title("💉 Medical Resource Allocation Simulator")

# Number of patients slider
num_patients = st.slider("Number of patients", 3, 10, 5)

# Initialize session state for individual patient inputs
for i in range(num_patients):
    if f"value_{i}" not in st.session_state:
        st.session_state[f"value_{i}"] = 10
    if f"weight_{i}" not in st.session_state:
        st.session_state[f"weight_{i}"] = 5

# Collect patient data
values = []
weights = []
for i in range(num_patients):
    val = st.number_input(
        f"Patient {i+1} priority/benefit",
        min_value=1,
        max_value=100,
        value=st.session_state[f"value_{i}"],
        key=f"value_input_{i}"
    )
    wt = st.number_input(
        f"Patient {i+1} resource requirement",
        min_value=1,
        max_value=20,
        value=st.session_state[f"weight_{i}"],
        key=f"weight_input_{i}"
    )

    # Update session state
    st.session_state[f"value_{i}"] = val
    st.session_state[f"weight_{i}"] = wt

    # Add to lists for knapsack
    values.append(val)
    weights.append(wt)

# Input for total available resources
capacity = st.number_input("Total available resources", min_value=1, max_value=100, value=20)

# Compute allocation
if st.button("Compute Optimal Allocation"):
    max_val, selected = knapsack(values, weights, capacity)
    st.success(f"Maximum total benefit: {max_val}")
    st.write(f"Selected patients: {[i+1 for i in selected]}")

    # Plot allocation
    fig = plot_allocation(values, selected)
    st.pyplot(fig)
