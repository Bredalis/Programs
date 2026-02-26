
# Algorithm to determine
# whether a number is prime or not

def is_prime():
    try:
        number = int(input("Enter the number: "))

        if number <= 1:
            return "Not prime"

        for i in range(2, number):
            if number % i == 0:
                return "Not prime"

        return "Prime"

    except ValueError:
        return "Error: Numbers only"

    except Exception as e:
        return f"Unexpected error: {e}"
