# src/allocation.py

def allocate_resources(patients, resources, critical_threshold=50):
    """
    Dynamic hybrid allocation of multiple resources.

    Args:
        patients (list of dict): Each dict has:
            - "name": str
            - "priority": int
            - "needs": dict of resource_type -> units_needed
        resources (dict): resource_type -> total units available
        critical_threshold (int): Priority above which patient is critical

    Returns:
        allocation (list of dict): Each dict has:
            - "name": patient name
            - "allocated": dict of resource_type -> units allocated
            - "priority": int
    """

    # Sort patients by priority descending
    patients_sorted = sorted(patients, key=lambda x: x['priority'], reverse=True)

    # Initialize allocation
    allocation = []
    remaining_resources = resources.copy()

    # Step 1: Allocate critical patients first
    for patient in patients_sorted:
        allocated = {}
        if patient['priority'] >= critical_threshold:
            for res, need in patient['needs'].items():
                allocated[res] = min(need, remaining_resources.get(res, 0))
                remaining_resources[res] = remaining_resources.get(res, 0) - allocated[res]
        else:
            # Leave for step 2
            allocated = {res: 0 for res in patient['needs']}
        allocation.append({"name": patient['name'], "allocated": allocated, "priority": patient['priority']})

    # Step 2: Allocate remaining resources to non-critical patients by descending priority
    for i, patient in enumerate(patients_sorted):
        if patient['priority'] < critical_threshold:
            allocated = allocation[i]['allocated']
            for res, need in patient['needs'].items():
                if remaining_resources.get(res, 0) > 0:
                    allocated[res] = min(need, remaining_resources[res])
                    remaining_resources[res] -= allocated[res]
            allocation[i]['allocated'] = allocated

    return allocation
