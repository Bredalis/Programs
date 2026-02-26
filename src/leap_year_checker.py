
# Algorithm to determine whether a year is a leap year or not

def is_leap_year():
    """Prompts the user for a year and determines if it is a leap year."""
    try:
        year = int(input("Enter the year: "))

        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return "It is a leap year"

        return "It is not a leap year"

    except ValueError:
        return "Error: Please enter numbers only"

    except Exception as error:
        return f"Unexpected error: {error}"


if __name__ == "__main__":
    print(is_leap_year())
