def get_multiplied_digits (number):
    str_number = str(number).replace('0', '', -1)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return  first

result = get_multiplied_digits(40203)
result1 = get_multiplied_digits(1)
result2 = get_multiplied_digits(1000065002)
result3 = get_multiplied_digits(10000650020)
result4 = get_multiplied_digits(100006500200000000)
print(result)
print(result1)
print(result2)
print(result3)
print(result4)