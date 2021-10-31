first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value.capitalize()

# Second challenge
second_value.rjust(20)

# Third challenge
third_value

print(first_value.title())
print(second_value.replace('-', ' ').strip().capitalize())
print(third_value.replace(' ', '').replace('-', ' ').capitalize().rjust(20))

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'\n\t{fourth_value:^25}\n\t{fifth_value:^25}\n\t{sixth_value:^25}')