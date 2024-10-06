import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Define the system of first-order ODEs
def second_order_ode_system(x, vars):
    y, z = vars  # vars contains y and z where z = dy/dx
    dydx = z
    dzdx = np.sin(x) - 2 * z - 3 * y
    return [dydx, dzdx]


# Function to solve the second-order ODE
def solve_second_order_ode(x_span, y0, z0, num_points=100):
    # Define the initial conditions
    initial_conditions = [y0, z0]  # [y(x0), dy/dx(x0)]

    # Define the range of x values to solve over
    x_eval = np.linspace(x_span[0], x_span[1], num_points)

    # Solve the system of ODEs using solve_ivp
    solution = solve_ivp(second_order_ode_system, x_span, initial_conditions, t_eval=x_eval)

    return solution.t, solution.y


# Function to plot the solution
def plot_solution(x_vals, y_vals, title="Second-Order ODE Solution"):
    plt.plot(x_vals, y_vals[0], label='y(x)', color='b')
    plt.plot(x_vals, y_vals[1], label="dy/dx (z)", color='r', linestyle='--')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('Solution')
    plt.grid(True)
    plt.legend()
    plt.show()


# Example usage
if __name__ == "__main__":
    # Initial conditions and x range
    x_span = (0, 10)  # Range of x values
    y0 = 1  # Initial value of y(x0)
    z0 = 0  # Initial value of dy/dx(x0)

    # Solve the ODE
    x_vals, y_vals = solve_second_order_ode(x_span, y0, z0)

    # Plot the solution
    plot_solution(x_vals, y_vals, title="Solution to Second-Order ODE")

