def numeric_check(input_number):
    """Verification that a number is entered."""
    try:
        return float(input_number) > 0
    except ValueError:
        return False
