# plotting/graphs for visualization
# src/visualization.py

import matplotlib.pyplot as plt

def plot_allocation(values, selected, labels=None):
    """
    Plot resource allocation results as a bar chart.
    
    Args:
        values (list): List of patient benefits
        selected (list): Indices of selected patients
        labels (list): Optional patient labels
    """
    n = len(values)
    if labels is None:
        labels = [f"Patient {i+1}" for i in range(n)]

    colors = ['green' if i in selected else 'red' for i in range(len(values))]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=colors)
    ax.set_ylabel("Priority / Benefit")
    ax.set_title("Medical Resource Allocation (Green = Selected)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return fig
