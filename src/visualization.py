# src/visualization.py

import matplotlib.pyplot as plt

def plot_allocation(patients_allocation, patients_original):
    """
    Plot patient allocation using color-coded bars:
    - Green = fully allocated
    - Yellow = partially allocated
    - Red = no allocation

    Args:
        patients_allocation (list of dict): Output from allocate_resources
        patients_original (list of dict): Original patient data with needs
    """
    labels = [p['name'] for p in patients_allocation]
    total_needs = []
    allocated_totals = []
    colors = []

    # Create a mapping of patient names to their original needs
    needs_map = {p['name']: p['needs'] for p in patients_original}

    for p in patients_allocation:
        # Sum of all resources needed and allocated for this patient
        original_needs = needs_map[p['name']]
        need_sum = sum(original_needs.values())
        allocated_sum = sum(p['allocated'].values())

        total_needs.append(need_sum)
        allocated_totals.append(allocated_sum)

        # Determine color
        if allocated_sum == need_sum:
            colors.append('green')      # fully allocated
        elif allocated_sum > 0:
            colors.append('yellow')     # partially allocated
        else:
            colors.append('red')        # no allocation

    fig, ax = plt.subplots(figsize=(8,5))
    ax.bar(labels, allocated_totals, color=colors)
    ax.set_ylabel("Total Units Allocated")
    ax.set_title("Medical Resource Allocation (Green=Full, Yellow=Partial, Red=None)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

