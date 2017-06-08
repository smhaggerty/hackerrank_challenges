def swap_case(s):
    swaped_s = [char.upper() if char.islower() else char.lower() for char in s]
    return ''.join(swaped_s)
