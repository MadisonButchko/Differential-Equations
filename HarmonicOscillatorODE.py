import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Define the system of first-order ODEs
def harmonic_oscillator(t, vars, omega0, zeta):
    x, v = vars  # vars contains x and v where v = dx/dt
    dxdt = v
    dvdt = -2 * zeta * omega0 * v - omega0 ** 2 * x
    return [dxdt, dvdt]


# Function to solve the second-order ODE
def solve_harmonic_oscillator(x0, v0, omega0, zeta, t_span, num_points=100):
    # Initial conditions [x(0), dx/dt(0)]
    initial_conditions = [x0, v0]

    # Solve using solve_ivp
    t_eval = np.linspace(t_span[0], t_span[1], num_points)
    solution = solve_ivp(harmonic_oscillator, t_span, initial_conditions, args=(omega0, zeta), t_eval=t_eval)

    return solution.t, solution.y


# Function to plot the solution
def plot_harmonic_oscillator(t_vals, y_vals, title="Damped Harmonic Oscillator"):
    plt.plot(t_vals, y_vals[0], label='Displacement (x)', color='b')
    plt.plot(t_vals, y_vals[1], label='Velocity (v)', color='r', linestyle='--')
    plt.title(title)
    plt.xlabel('Time (t)')
    plt.ylabel('Solution')
    plt.grid(True)
    plt.legend()
    plt.show()


# Example usage
x0 = 1  # Initial displacement
v0 = 0  # Initial velocity
omega0 = 1  # Natural frequency
zeta = 0.1  # Damping ratio
t_span = (0, 20)  # Time range

t_vals, y_vals = solve_harmonic_oscillator(x0, v0, omega0, zeta, t_span)
plot_harmonic_oscillator(t_vals, y_vals, title="Damped Harmonic Oscillator")

