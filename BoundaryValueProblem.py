import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp


# Define the differential equation for beam deflection under various loads
def beam_deflection(x, y, load_type):
    if load_type == 'sin':
        q_x = np.sin(x)  # Sinusoidal load
    elif load_type == 'constant':
        q_x = 1.0  # Constant load
    elif load_type == 'triangular':
        q_x = x  # Triangular load
    else:
        raise ValueError("Invalid load type. Choose 'sin', 'constant', or 'triangular'")

    return [y[1], -q_x]  # d^2y/dx^2 = -q(x)


# Define boundary conditions for clamped beam (y(0) = 0, dy/dx(0) = 0, y(L) = 0, dy/dx(L) = 0)
def clamped_boundary_conditions(ya, yb):
    return [ya[0], ya[1], yb[0], yb[1]]  # Clamped at both ends


# Function to solve the BVP
def solve_beam_bvp(L, load_type, num_points=100):
    x_vals = np.linspace(0, L, num_points)
    initial_guess = np.zeros((2, x_vals.size))  # Initial guess for [y, dy/dx]

    # Solve using solve_bvp
    solution = solve_bvp(lambda x, y: beam_deflection(x, y, load_type), clamped_boundary_conditions, x_vals,
                         initial_guess)

    if solution.success:
        return solution.x, solution.y[0]
    else:
        raise RuntimeError("Boundary value problem solver failed to converge")


# Function to plot the solution
def plot_beam_deflection(x_vals, y_vals, title="Beam Deflection under Load"):
    plt.plot(x_vals, y_vals, label='Deflection (y)', color='b')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('Deflection (y)')
    plt.grid(True)
    plt.legend()
    plt.show()


# Main function to choose load type and solve the BVP
def main():
    print("Choose a load type for the beam:")
    print("1. Sinusoidal load")
    print("2. Constant load")
    print("3. Triangular load")

    load_choice = input("Enter choice (1/2/3): ")
    if load_choice == '1':
        load_type = 'sin'
    elif load_choice == '2':
        load_type = 'constant'
    elif load_choice == '3':
        load_type = 'triangular'
    else:
        print("Invalid choice, using default sinusoidal load.")
        load_type = 'sin'

    # Beam properties
    L = float(input("Enter the length of the beam (L): "))

    # Solve the BVP
    x_vals, y_vals = solve_beam_bvp(L, load_type)

    # Plot the solution
    plot_beam_deflection(x_vals, y_vals, title=f"Beam Deflection under {load_type.capitalize()} Load")


# Run the main function
if __name__ == "__main__":
    main()
