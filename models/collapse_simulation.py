import numpy as np
import matplotlib.pyplot as plt

def simulate_entropy_dynamics(steps=100, B0=1.0, P=0.1, V=0.05):
    """
    Simulates the evolution of Support Breadth (B) over time.
    B_next = B_current - (P * B_current) + V
    """
    breadth = [B0]
    for t in range(steps):
        current_B = breadth[-1]
        # Calculate next state
        next_B = current_B - (P * current_B) + V
        # Support cannot be negative
        breadth.append(max(0, next_B))
    return breadth

# Scenario 1: High Pressure, Low Entropy (Collapse)
collapse = simulate_entropy_dynamics(P=0.15, V=0.02)

# Scenario 2: Balanced Pressure and Entropy (Stability)
stability = simulate_entropy_dynamics(P=0.15, V=0.10)

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(collapse, label='Collapse Regime (P > V)', color='red', linewidth=2)
plt.plot(stability, label='Stable Regime (V approach P)', color='green', linewidth=2)
plt.axhline(y=0, color='black', linestyle='--')
plt.title('The Entropic Zoo: Support Contraction Dynamics', fontsize=14)
plt.xlabel('Optimization Steps (t)', fontsize=12)
plt.ylabel('Support Breadth (B)', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()

print("Simulation complete. Visualizing the 'Hybrid Axis' threshold.")