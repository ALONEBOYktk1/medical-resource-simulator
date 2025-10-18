# main.py

import streamlit as st
from src.allocation import knapsack
from src.visualization import plot_allocation

st.set_page_config(page_title="Medical Resource Allocation Simulator", page_icon="💉")
st.title("💉 Medical Resource Allocation Simulator")

# ----------- Streamlit Inputs -----------

# Slider for number of patients
num_patients = st.slider("Number of patients", 3, 10, 5)

# Initialize session state for patient data
if 'values' not in st.session_state or len(st.session_state.values) != num_patients:
    st.session_state.values = [10] * num_patients
if 'weights' not in st.session_state or len(st.session_state.weights) != num_patients:
    st.session_state.weights = [5] * num_patients

# Dynamic input fields
for i in range(num_patients):
    key_val = f"value_{i}"
    key_wt = f"weight_{i}"

    val = st.number_input(
        f"Patient {i+1} priority/benefit",
        min_value=1, max_value=100,
        value=st.session_state.values[i],
        key=key_val
    )
    wt = st.number_input(
        f"Patient {i+1} resource requirement",
        min_value=1, max_value=20,
        value=st.session_state.weights[i],
        key=key_wt
    )

    st.session_state.values[i] = val
    st.session_state.weights[i] = wt

# Input for total resources
capacity = st.number_input("Total available resources", min_value=1, max_value=100, value=20)

# ----------- Compute Allocation -----------
if st.button("Compute Optimal Allocation"):
    values = st.session_state.values
    weights = st.session_state.weights

    # Compute knapsack
    max_val, selected = knapsack(values, weights, capacity)

    # Display results
    st.success(f"Maximum total benefit: {max_val}")
    st.write(f"Selected patients: {[i+1 for i in selected]}")

    # Plot allocation
    fig = plot_allocation(values, selected)
    st.pyplot(fig)
