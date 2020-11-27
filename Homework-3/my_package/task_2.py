def sum_numbers_recursion(n):
    if n == 0:
        return 0

    return n + sum_numbers_recursion(n - 1)


def sum_even_numbers_recursion(n):
    if n == 0:
        return 0

    return n + sum_even_numbers_recursion(n - 1) if n % 2 == 0 \
        else sum_even_numbers_recursion(n - 1)


def sum_odd_numbers_recursion(n):
    if n == 0:
        return 0

    return n + sum_odd_numbers_recursion(n - 1) if n % 2 != 0 \
        else sum_odd_numbers_recursion(n - 1)
