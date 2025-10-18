# StreamLit entry point for medical resource allocation simulator
# main.py

import streamlit as st
from src.allocation import knapsack
from src.visualization import plot_allocation

st.set_page_config(page_title="Medical Resource Allocation Simulator", page_icon="💉")
st.title("💉 Medical Resource Allocation Simulator")

# Example patient data
num_patients = st.slider("Number of patients", 3, 10, 5)

values = []
weights = []

for i in range(num_patients):
    values.append(st.number_input(f"Patient {i+1} priority/benefit", min_value=1, max_value=100, value=10))
    weights.append(st.number_input(f"Patient {i+1} resource requirement", min_value=1, max_value=20, value=5))

capacity = st.number_input("Total available resources", min_value=1, max_value=100, value=20)

if st.button("Compute Optimal Allocation"):
    max_val, selected = knapsack(values, weights, capacity)
    st.success(f"Maximum total benefit: {max_val}")
    st.write(f"Selected patients: {[i+1 for i in selected]}")

    # Plot allocation
    fig = plot_allocation(values, selected)
    st.pyplot(fig)
