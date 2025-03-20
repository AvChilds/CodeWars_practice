"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""

number = str(82041)
digit_list = []# Outp
for digit in number:
    digit_list.append(int(digit))
sorted_list = sorted(digit_list, reverse=True)
sorted_number = int("".join(map(str,digit_list)))

print(sorted_number)

def desc_order(num):
    sorted_number = sorted(str(num), reverse=True)
    result = int("".join(sorted_number))
    return result

print (desc_order(24917))


