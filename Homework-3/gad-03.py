from my_package.task_1 import *
from my_package.task_2 import *
from my_package.task_3 import *

# Task 1
print('Task 1')
my_sum = sum_variable_number_of_parameters(1, 5, -3, 'abc', [12, 56, 'cad'])
print('my_sum =', my_sum)
my_sum = sum_variable_number_of_parameters()
print('my_sum =', my_sum)
my_sum = sum_variable_number_of_parameters(2, 4, 'abc', param_1=2)
print('my_sum =', my_sum)
print()

# Task 2
print('Task 2')
my_sum = sum_numbers_recursion(10)
print('Sum numbers =', my_sum)
my_sum = sum_even_numbers_recursion(10)
print('Sum odd numbers =', my_sum)
my_sum = sum_odd_numbers_recursion(10)
print('Sum even numbers =', my_sum)
print()

# Task 3
print('Task 3')
print('Value =', check_if_integer())

