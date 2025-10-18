# src/allocation.py

def knapsack(values, weights, capacity):
    """
    Solve the 0/1 Knapsack problem for resource allocation.

    Args:
        values (list): Priority/benefit of each patient
        weights (list): Resource units required per patient
        capacity (int): Total available resources

    Returns:
        max_value (int): Maximum total benefit achievable
        selected (list): Indices of selected patients
    """
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected items
    w = capacity
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    selected.reverse()
    max_value = dp[n][capacity]
    return max_value, selected
