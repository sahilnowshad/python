def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Test with hard-coded values
is_leap_year(2400)   # True
is_leap_year(1989)   # False
is_leap_year(2024)   # True
