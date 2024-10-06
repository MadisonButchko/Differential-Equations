import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Define function to solve the differential equation
def solve_single_first_order(eq_func, x0, y0, x_span, num_points=100):
    # Solve the first-order differential equation using solve_ivp
    x_eval = np.linspace(x_span[0], x_span[1], num_points)
    solution = solve_ivp(eq_func, x_span, [y0], t_eval=x_eval)

    # Return solution for further customization
    return solution.t, solution.y[0]


# Define function to solve a system of first-order ODEs
def solve_system_first_order(eq_func, x0, y0, x_span, num_points=100):
    # Solve the system of first-order differential equations using solve_ivp
    x_eval = np.linspace(x_span[0], x_span[1], num_points)
    solution = solve_ivp(eq_func, x_span, y0, t_eval=x_eval)

    # Return solution for further customization
    return solution.t, solution.y


# Example equation 1: single ODE
def equation1(x, y):
    # dy/dx = -2y + x (you can change this function)
    return -2 * y + x


# Example equation 2: system of ODEs
def system_of_equations(x, vars):
    y1, y2 = vars
    dy1_dx = y2
    dy2_dx = -y1
    return [dy1_dx, dy2_dx]


# Function to plot single solution
def plot_single_solution(x_vals, y_vals, title="First-Order ODE Solution"):
    plt.plot(x_vals, y_vals, label="y(x)", color='b')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.grid(True)
    plt.legend()
    plt.show()


# Function to plot system solution
def plot_system_solution(x_vals, y_vals, labels=["y1(x)", "y2(x)"], title="System of First-Order ODEs Solution"):
    for i, y in enumerate(y_vals):
        plt.plot(x_vals, y, label=labels[i])
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('Solution Variables')
    plt.grid(True)
    plt.legend()
    plt.show()


# Function to save solution to a file
def save_solution_to_file(x_vals, y_vals, filename="solution.txt"):
    with open(filename, 'w') as file:
        for i in range(len(x_vals)):
            file.write(f"{x_vals[i]}, {y_vals[i]}\n")
    print(f"Solution saved to {filename}")


# Main function for selecting type of equation and solving
def main():
    print("Choose the type of equation to solve:")
    print("1. Solve single first-order ODE")
    print("2. Solve system of first-order ODEs")

    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        print("Solving a single first-order ODE...")

        # Initial condition and range
        x0 = float(input("Enter the initial x value (x0): "))
        y0 = float(input("Enter the initial y value (y0): "))
        x_end = float(input("Enter the final x value: "))
        x_span = (x0, x_end)

        # Solve the ODE
        x_vals, y_vals = solve_single_first_order(equation1, x0, y0, x_span)

        # Plot and save the solution
        plot_single_solution(x_vals, y_vals, title="Single First-Order ODE Solution")
        save_solution_to_file(x_vals, y_vals)

    elif choice == '2':
        print("Solving a system of first-order ODEs...")

        # Initial conditions for system
        x0 = float(input("Enter the initial x value (x0): "))
        y0_1 = float(input("Enter the initial y1 value (y0_1): "))
        y0_2 = float(input("Enter the initial y2 value (y0_2): "))
        x_end = float(input("Enter the final x value: "))
        x_span = (x0, x_end)
        y0 = [y0_1, y0_2]

        # Solve the system of ODEs
        x_vals, y_vals = solve_system_first_order(system_of_equations, x0, y0, x_span)

        # Plot and save the solution
        plot_system_solution(x_vals, y_vals, labels=["y1(x)", "y2(x)"], title="System of First-Order ODEs Solution")
        for i, y_var in enumerate(y_vals):
            save_solution_to_file(x_vals, y_var, filename=f"solution_y{i + 1}.txt")

    else:
        print("Invalid choice. Please restart the program and choose 1 or 2.")


# Run the main function
if __name__ == "__main__":
    main()
