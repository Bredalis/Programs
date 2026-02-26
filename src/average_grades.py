
# Average of 4 grades
def average(grades):
    try:
        if len(grades) != 4:
            return "Enter a list of 4 grades"

        return round(sum(grades) / 4)

    except Exception as e:
        print(f"Unexpected error: {e}")
