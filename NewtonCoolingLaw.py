import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the ODE based on Newton's Law of Cooling
def cooling_ode(t, T, T_ambient, k):
    return -k * (T - T_ambient)

# Function to solve the ODE
def solve_newtons_cooling(T0, T_ambient, k, t_span, num_points=100):
    t_eval = np.linspace(t_span[0], t_span[1], num_points)
    solution = solve_ivp(cooling_ode, t_span, [T0], args=(T_ambient, k), t_eval=t_eval)
    return solution.t, solution.y[0]

# Plot the solution
def plot_solution(t_vals, T_vals, title="Newton's Law of Cooling"):
    plt.plot(t_vals, T_vals, label="Temperature (T)", color='b')
    plt.title(title)
    plt.xlabel('Time (t)')
    plt.ylabel('Temperature (T)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage
T0 = 100  # Initial temperature of the object
T_ambient = 20  # Ambient temperature
k = 0.1  # Cooling constant
t_span = (0, 100)  # Time range

t_vals, T_vals = solve_newtons_cooling(T0, T_ambient, k, t_span)
plot_solution(t_vals, T_vals, title="Newton's Law of Cooling")
