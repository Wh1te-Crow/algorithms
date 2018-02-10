def power(number,exponent):
    if number == 1 or exponent == 0 :
        return 1
    else:
        return number*power(number,exponent -1)
print power(2,5)
print power(6,3)
