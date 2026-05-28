def multiply(a,b):
    return a*b
print(multiply(3,4))

def is_even(n):
    return n % 2 == 0
print(is_even(7))

def get_max(lst):
    max_value = lst[0]
    for i in lst:
        if i > max_value:
            max_value = i
    return max_value
print(get_max([3,1,8,2]))
