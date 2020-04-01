def math_operations(x, y, z, /, print_this="Hello World"):
    print(print_this)
    return x * y + z

print(math_operations(3,5,2, print_this="2nd Hello"))

# def math_operations(x, y, z, /, print_this="Hello World"):
#     print(print_this)
#     return x * y + z
#
# print(math_operations(x=3,z=5,y=2))
