
print("Grade classifier with a maximum of 100 points")


def classify_grade():
    """Classifies a student's grade based on a 100-point scale."""
    try:
        grade = int(input("Final grade: "))

        if 90 <= grade <= 100:
            print("Excellent, you are very smart!")

        elif 70 < grade < 90:
            print("Very good, you are hardworking!")

        elif 0 <= grade <= 70:
            print("You need to improve")

        else:
            print("Invalid grade")

    except ValueError:
        print("Error: Numbers only")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    classify_grade()
