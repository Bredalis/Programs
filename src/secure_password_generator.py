
# Secure password generator

from faker import Faker

fake = Faker()


def generate_secure_password(length: int) -> str:
    """
    Generates a secure password with the specified length.
    Minimum length: 8
    Maximum length: 128
    """

    # Type validation FIRST (before comparisons)
    if not isinstance(length, int):
        return "Unexpected error: Length must be an integer."

    # Range validation
    if length < 8 or length > 128:
        return "Minimum length is 8 and maximum is 128."

    try:
        password = fake.password(length=length)
        return f"Your secure password: {password}"

    except Exception as error:
        return f"Unexpected error: {error}"


if __name__ == "__main__":
    print(generate_secure_password(12))
