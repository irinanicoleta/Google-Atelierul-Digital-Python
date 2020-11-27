def check_if_integer():
    value = input('Enter value here: ')
    try:
        return int(value)
    except ValueError as e:
        return 0
