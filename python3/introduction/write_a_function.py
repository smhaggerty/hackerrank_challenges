def is_leap(year):
    leap = False
    dividable_by_four = year % 4 == 0
    dividable_by_100 = year % 100 == 0
    dividable_by_400 = year % 400 == 0

    if dividable_by_four:
        leap = True
        if dividable_by_100 and dividable_by_400:
            leap = True
        elif dividable_by_100:
            leap = False

    return leap
