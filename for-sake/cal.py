def calculator():
    """A simple command-line calculator."""

    print("Simple Calculator")
    print("-----------------")
    print("Available operations: +, -, *, /, ^ (exponent), sqrt (square root)")
    print("Enter 'exit' to quit.")

    while True:
        expression = input("Enter expression: ")

        if expression.lower() == 'exit':
            break

        try:
            #Handles square root
            if "sqrt" in expression:
                parts = expression.split("sqrt")
                if len(parts) != 2:
                    raise ValueError("Invalid square root format. Please use 'sqrt(number)'")
                num_str = parts[1].strip("()")
                num = float(num_str)
                if num < 0:
                    raise ValueError("Cannot take square root of a negative number")
                result = num ** 0.5
                print("Result:", result)
                continue

            #Handles standard operations
            result = eval(expression) #eval is generally unsafe for user input, safer alternatives exist.
            print("Result:", result)

        except (ValueError, SyntaxError, ZeroDivisionError) as e:
            print("Error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)

if __name__ == "__main__":
    calculator()