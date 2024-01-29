def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or (year % 100 == 0 and year % 400 == 0):
        return True

    return False


print(is_leap(2100))
