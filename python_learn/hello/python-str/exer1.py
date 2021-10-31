# # message = str.capitalize('first message')
# # print(message)

# # message = 'second message'.capitalize()
# # print(message)

# # message = 'third message'
# # print(message.capitalize())
# message = 'hello world'
# print(message.lower())
# print(message.upper())

# message = message.title()
# print(message)
# print(message.swapcase())

# print(len('how many characters in this string?'))
# location = 'MiSsissippi'
# print(location.count('s'))

# message = '    middle     '
# print('.' + message.lstrip() + '.')
# print('.' + message.rstrip() + '.')
# print('.' + message.strip() + '.')

# message = 'howdy'
# print(message.rjust(20))
# print(message.rjust(20, '*'))
# print(message.ljust(20))
# print(message.ljust(20, '-'))

# medicine = 'Coughussin'
# dosage = 5
# duration = 4.5

# instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
# print(instructions)

# instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
# print(instructions)

# instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)

# print(instructions)

# name = 'World'
# message = f'Hello, {name}.'
# print(message)

# count = 10
# value = 3.14
# message = f'Count to {count}.  Multiply by {value}.'
# print(message)

# width = 5
# height = 10

# print(f'The perimeter is {(2 * width) + (2 * height)} and the area is {width * height}.')

value = 'hi'

print(f'.{value:<25}.')
print(f'.{value:>25}.')
print(f'.{value:^25}.')
print(f'.{value:-^25}.')