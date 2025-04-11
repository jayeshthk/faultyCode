# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # ✅ Previously buggy, now fixed

def multiply(a, b):
    # ❌ Bug: Accidentally returning the square of 'a' instead of a * b
    return a * a

def main():
    print("Simple Calculator")
    print("Select operation: add, subtract, multiply")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operation = input("Enter operation: ").strip().lower()

    if operation == "add":
        print("Result:", add(a, b))
    elif operation == "subtract":
        print("Result:", subtract(a, b))
    elif operation == "multiply":
        print("Result:", multiply(a, b))
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    main()
