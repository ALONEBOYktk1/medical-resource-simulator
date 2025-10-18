# 🩺 Medical Resource Allocation Simulator

## Project Overview
This project simulates **dynamic allocation of medical resources** (ICU beds, ventilators, monitors) to patients in a hospital, using a **humane hybrid approach** inspired by real-world triage scenarios. Critical patients are prioritized, while remaining resources are distributed to the highest-priority non-critical patients.

The simulator helps visualize **how hospitals can optimize limited resources** efficiently under constraints, making it relevant for **medical technology and automation applications**.

---

## Features

- **Dynamic multi-resource allocation**: Handles multiple types of medical resources simultaneously.  
- **Humane hybrid logic**: Critical patients are prioritized, non-critical patients get remaining resources.  
- **Partial allocation**: Patients receive as much of their required resources as available.  
- **Interactive UI**: Built with Streamlit for real-time input and visualization.  
- **Color-coded visualization**: Green = fully allocated, Yellow = partially allocated.  
- **Resume/demo ready**: Clean, professional UI to showcase Python automation and problem-solving skills.  

---

## How It Works

1. Users specify:  
   - Number of patients  
   - Priority/benefit for each patient  
   - Resource needs (Beds, Ventilators, Monitors)  
   - Total available resources in ICU  

2. The **allocation algorithm**:  
   - Allocates resources to **critical patients first**  
   - Distributes remaining resources to **highest-priority non-critical patients**  
   - Updates dynamically as inputs change  

3. **Visualization**:  
   - Each patient is shown as a bar  
   - Bar height = total units allocated  
   - Color indicates full vs partial allocation  

---

## Technologies Used

- Python 3.13  
- Streamlit (interactive web UI)  
- Matplotlib (visualization)  
- Pandas & NumPy (data handling)  

---

## Folder Structure

medical_resource_simulator/
├── src/
│   ├── __init__.py
│   ├── allocation.py       # Core allocation logic
│   └── visualization.py    # Plotting logic
├── main.py                 # Streamlit entry point
├── requirements.txt        # Project dependencies
├── README.md               # Project description
└── .gitignore              # Ignored files

## Live Demo
Try the interactive web app here: [Medical Resource Allocation Simulator](https://share.streamlit.io/yourusername/medical-resource-simulator/main)
