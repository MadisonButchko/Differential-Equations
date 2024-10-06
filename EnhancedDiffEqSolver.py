import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def solve_first_order_linear_ode():
    print("Let's solve a first-order linear ODE of the form:")
    print("dy/dx + P(x)y = Q(x)")

    # Get user input for P(x) and Q(x)
    P_x = input("Enter P(x) as a function of x (e.g., '2*x'): ")
    Q_x = input("Enter Q(x) as a function of x (e.g., 'sin(x)'): ")

    # Get initial conditions
    x0 = float(input("Enter the initial value of x (e.g., 0): "))
    y0 = float(input(f"Enter the initial value of y at x = {x0} (e.g., 1): "))

    # Define symbols
    x = sp.symbols('x')
    y = sp.Function('y')(x)

    # Convert P(x) and Q(x) to sympy expressions
    P_x_expr = sp.sympify(P_x)
    Q_x_expr = sp.sympify(Q_x)

    # Formulate the equation
    ode = sp.Eq(sp.Derivative(y, x) + P_x_expr * y, Q_x_expr)

    # Display the equation
    print("\nYour equation is:")
    sp.pprint(ode)

    # Solve the ODE
    solution = sp.dsolve(ode, y)

    # Display the solution
    print("\nThe general solution is:")
    sp.pprint(solution)

    return solution


def solve_separable_ode():
    print("Let's solve a separable ODE of the form:")
    print("dy/dx = g(y)*h(x)")

    # Get user input for g(y) and h(x)
    g_y = input("Enter g(y) as a function of y (e.g., 'y'): ")
    h_x = input("Enter h(x) as a function of x (e.g., 'sin(x)'): ")

    # Get initial conditions
    x0 = float(input("Enter the initial value of x (e.g., 0): "))
    y0 = float(input(f"Enter the initial value of y at x = {x0} (e.g., 1): "))

    # Define symbols
    x, y = sp.symbols('x y')

    # Convert g(y) and h(x) to sympy expressions
    g_y_expr = sp.sympify(g_y)
    h_x_expr = sp.sympify(h_x)

    # Solve using separation of variables
    ode = sp.Eq(sp.Derivative(y, x), g_y_expr * h_x_expr)

    print("\nYour equation is:")
    sp.pprint(ode)

    # Solve for y
    separated_ode = sp.Eq(sp.integrate(1 / g_y_expr, y), sp.integrate(h_x_expr, x))

    # Display the solution
    print("\nThe general solution is:")
    sp.pprint(separated_ode)

    return separated_ode


def solve_exact_ode():
    print("Let's solve an exact ODE of the form:")
    print("M(x, y)dx + N(x, y)dy = 0")

    # Get user input for M(x, y) and N(x, y)
    M_x_y = input("Enter M(x, y) (e.g., '2*x*y + y^2'): ")
    N_x_y = input("Enter N(x, y) (e.g., 'x^2 + 2*x*y'): ")

    # Define symbols
    x, y = sp.symbols('x y')

    # Convert M(x, y) and N(x, y) to sympy expressions
    M_expr = sp.sympify(M_x_y)
    N_expr = sp.sympify(N_x_y)

    # Check if the equation is exact: dM/dy == dN/dx
    dM_dy = sp.diff(M_expr, y)
    dN_dx = sp.diff(N_expr, x)

    if dM_dy == dN_dx:
        print("\nThe equation is exact. Proceeding with the solution.")
        Psi = sp.integrate(M_expr, x) + sp.integrate(N_expr - sp.diff(M_expr, y), y)
        solution = sp.Eq(Psi, 0)

        print("\nThe general solution is:")
        sp.pprint(solution)
    else:
        print("\nThe equation is not exact.")

    return solution


def solve_second_order_linear_ode():
    print("Let's solve a second-order linear homogeneous ODE of the form:")
    print("a*d²y/dx² + b*dy/dx + c*y = 0")

    # Get the coefficients from the user
    a = float(input("Enter the coefficient a (e.g., 1): "))
    b = float(input("Enter the coefficient b (e.g., 2): "))
    c = float(input("Enter the coefficient c (e.g., 1): "))

    # Get initial conditions
    x0 = float(input("Enter the initial value of x (e.g., 0): "))
    y0 = float(input(f"Enter the initial value of y at x = {x0} (e.g., 1): "))
    dy0 = float(input(f"Enter the initial value of dy/dx at x = {x0} (e.g., 0): "))

    # Define symbols
    x = sp.symbols('x')
    y = sp.Function('y')(x)

    # Define the second-order ODE
    ode = sp.Eq(a * sp.Derivative(y, x, 2) + b * sp.Derivative(y, x) + c * y, 0)

    # Display the ODE
    print("\nYour equation is:")
    sp.pprint(ode)

    # Solve the ODE using sympy's dsolve function
    solution = sp.dsolve(ode, y)

    # Display the general solution
    print("\nThe general solution is:")
    sp.pprint(solution)

    return solution


def solve_second_order_nonhomogeneous_ode():
    print("Let's solve a second-order linear non-homogeneous ODE of the form:")
    print("a*d²y/dx² + b*dy/dx + c*y = f(x)")

    # Get the coefficients and forcing function from the user
    a = float(input("Enter the coefficient a (e.g., 1): "))
    b = float(input("Enter the coefficient b (e.g., 2): "))
    c = float(input("Enter the coefficient c (e.g., 1): "))
    f_x = input("Enter f(x) (e.g., 'sin(x)'): ")

    # Get initial conditions
    x0 = float(input("Enter the initial value of x (e.g., 0): "))
    y0 = float(input(f"Enter the initial value of y at x = {x0} (e.g., 1): "))
    dy0 = float(input(f"Enter the initial value of dy/dx at x = {x0} (e.g., 0): "))

    # Define symbols
    x = sp.symbols('x')
    y = sp.Function('y')(x)

    # Define the non-homogeneous ODE
    f_x_expr = sp.sympify(f_x)
    ode = sp.Eq(a * sp.Derivative(y, x, 2) + b * sp.Derivative(y, x) + c * y, f_x_expr)

    # Display the ODE
    print("\nYour equation is:")
    sp.pprint(ode)

    # Solve the ODE using sympy's dsolve function
    solution = sp.dsolve(ode, y)

    # Display the general solution
    print("\nThe general solution is:")
    sp.pprint(solution)

    return solution


def main():
    print("Welcome to the Enhanced Differential Equation Solver!")
    print("You can solve first-order or second-order differential equations here.")

    print("\nSelect the type of differential equation you want to solve:")
    print("1. First-order linear ODE")
    print("2. Separable ODE")
    print("3. Exact ODE")
    print("4. Second-order linear homogeneous ODE")
    print("5. Second-order linear non-homogeneous ODE")

    choice = input("\nEnter your choice (1/2/3/4/5): ")

    if choice == '1':
        solution = solve_first_order_linear_ode()
    elif choice == '2':
        solution = solve_separable_ode()
    elif choice == '3':
        solution = solve_exact_ode()
    elif choice == '4':
        solution = solve_second_order_linear_ode()
    elif choice == '5':
        solution = solve_second_order_nonhomogeneous_ode()
    else:
        print("Invalid choice. Please restart and select a valid option.")
        return

    print("\nThank you for using the Enhanced Differential Equation Solver!")


if __name__ == "__main__":
    main()
