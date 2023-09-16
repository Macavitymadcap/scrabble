# https://word.tips/unscramble/_/length/8/

from string import digits

with open('eight.txt', 'r') as input, open('nonums.txt', 'w') as output:
    for line in input.readlines():
        new_line = ''
        for character in line:
            if character not in digits:
                new_line += character
        output.write(new_line)