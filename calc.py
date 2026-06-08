import msvcrt

def calc():
    print("\nCalculator")
    op = input("Operation (-,+,*,/): ").strip()
    if op not in ('-','+','*','/'):
        print("Unknown operation.")
        return
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
    except ValueError:
        print("Invalid number input.")
        return
    if op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero!")
        else:
            print(f"Result: {num1 / num2}")

def discr():
    print("\nDiscriminant (ax^2 + bx + c = 0)")
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
    except ValueError:
        print("Invalid number input.")
        return
    D = b**2 - 4*a*c
    if D > 0:
        print({"D": D},)
        sqrtD = D**0.5
        print({"sqrtD": sqrtD})
        x1 = (-b + sqrtD) / (2*a)
        x2 = (-b - sqrtD) / (2*a)
        print(f"Two real roots: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2*a)
        print(f"One real root: x = {x}")
    else:
        real = -b / (2*a)
        imag = (abs(D)**0.5) / (2*a)
        print(f"Complex roots: {real} ± {imag}i")

def main():
    print("Choose your math instrument: press 1 for Calculator, 2 for Discriminant. Press ESC to exit.")
    while True:
        print("\nPress 1 (calculator), 2 (discriminant), or ESC to quit.")
        key = msvcrt.getch()
        if key == b'\x1b':
            print("Exiting.")
            break
        elif key == b'1':
            calc()
        elif key == b'2':
            discr()
        else:
            print("Unknown key. Use 1, 2 or ESC.")

if __name__ == "__main__":
    main()
