def sum_variable_number_of_parameters(*args, **kwargs):
    my_sum = 0
    for number in args:
        try:
            my_sum += number
        except TypeError as e:
            pass

    return my_sum
