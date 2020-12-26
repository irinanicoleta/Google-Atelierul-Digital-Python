from Fraction import Fraction

fraction = Fraction(1, 3)
# str
print('Afisare fractie:', fraction)

another_fraction = Fraction(2, 3)
print('Afisare fractie:', another_fraction)
# add
new_fraction = fraction.__add__(another_fraction)
print('Adunare 2 fractii:', new_fraction)

# sub
new_fraction = fraction.__sub__(another_fraction)
print('Scadere 2 fractii:', new_fraction)

# inverse
print('Inversarea unei fractii:', new_fraction.inverse())
