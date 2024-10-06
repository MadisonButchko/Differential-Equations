def get_ode_type():
    print("Welcome to the ODE Solver Guide!")
    print("Let's start by identifying the type of your ODE.\n")

    # Step 1: First-order or Second-order
    order = input("Is your ODE first-order or second-order? (Enter '1' for first-order, '2' for second-order): ")

    if order == '1':
        print("\nYou have a first-order ODE.")
        return solve_first_order()
    elif order == '2':
        print("\nYou have a second-order ODE.")
        return solve_second_order()
    else:
        print("Invalid input. Please restart the program and enter '1' or '2'.")
        return None


def solve_first_order():
    print("\nGreat! Let's narrow down the type of first-order ODE.")

    # Step 2: Type of first-order ODE
    print("Please select the type of first-order ODE:")
    print("1. Linear (dy/dx + P(x)y = Q(x))")
    print("2. Separable (dy/dx = g(y)h(x))")
    print("3. Exact (M(x, y)dx + N(x, y)dy = 0)")
    print("4. Homogeneous (dy/dx = F(y/x))")

    ode_type = input("Enter the number corresponding to your ODE type (1/2/3/4): ")

    if ode_type == '1':
        print("\nYour ODE is linear.")
        print("You can solve it using the integrating factor method.")
        print("1. Rewrite the equation in the form dy/dx + P(x)y = Q(x).")
        print("2. Calculate the integrating factor: μ(x) = exp(∫P(x)dx).")
        print("3. Multiply through by μ(x) and integrate both sides.")
    elif ode_type == '2':
        print("\nYour ODE is separable.")
        print("You can solve it by separating variables.")
        print(
            "1. Rearrange the equation so that all terms involving y are on one side, and all terms involving x are on the other.")
        print("2. Integrate both sides.")
    elif ode_type == '3':
        print("\nYour ODE is exact.")
        print("To solve, check if the equation is exact (i.e., ∂M/∂y = ∂N/∂x).")
        print("If it is exact, solve by finding the potential function Ψ(x, y) such that:")
        print("∂Ψ/∂x = M(x, y) and ∂Ψ/∂y = N(x, y).")
        print("Integrate to find Ψ(x, y) and set Ψ(x, y) = C (a constant).")
    elif ode_type == '4':
        print("\nYour ODE is homogeneous.")
        print("You can solve it by making the substitution v = y/x, which converts the ODE into a separable form.")
        print("Then solve as a separable ODE.")
    else:
        print("Invalid choice. Please restart and try again.")
        return None


def solve_second_order():
    print("\nLet's narrow down the type of second-order ODE.")

    # Step 3: Type of second-order ODE
    print("Please select the type of second-order ODE:")
    print("1. Linear with constant coefficients (a d²y/dx² + b dy/dx + c y = f(x))")
    print("2. Nonlinear or variable coefficients")
    print("3. You are not sure")

    ode_type = input("Enter the number corresponding to your ODE type (1/2/3): ")

    if ode_type == '1':
        print("\nYour ODE is linear with constant coefficients.")
        print("You can solve it using the characteristic equation:")
        print("1. Write the characteristic equation: a r² + b r + c = 0.")
        print("2. Solve for the roots r1 and r2:")
        print("    - If the roots are real and distinct: y(x) = C₁e^(r₁x) + C₂e^(r₂x).")
        print("    - If the roots are real and repeated: y(x) = (C₁ + C₂x)e^(r₁x).")
        print("    - If the roots are complex: y(x) = e^(αx)(C₁cos(βx) + C₂sin(βx)), where r₁, r₂ = α ± iβ.")
    elif ode_type == '2':
        print("\nYour ODE is nonlinear or has variable coefficients.")
        print("Consider using numerical methods like Euler’s method or the Runge-Kutta method.")
        print(
            "Alternatively, you can try special solution methods like reduction of order or variation of parameters if applicable.")
    elif ode_type == '3':
        print(
            "\nNo worries! If you're unsure about the type of your second-order ODE, start by checking for linearity:")
        print("1. Check if it can be written as a linear equation with constant or variable coefficients.")
        print("2. If it's nonlinear, numerical methods or power series methods might be suitable.")
    else:
        print("Invalid choice. Please restart and try again.")
        return None


# Main function to guide through solving ODE
def main():
    print("This is an interactive guide to help you determine how to solve your ODE.")
    get_ode_type()
    print("\nThank you for using the ODE Solver Guide!")


# Run the program
if __name__ == "__main__":
    main()
