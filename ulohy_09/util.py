def validate_days(days):
    if type(days) is int and int(days) > 0:
        return days
    raise ValueError("Number of days must be numeric.")
