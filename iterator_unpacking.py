
# def f():
#     rem = (3,4,5)
#     a = 1,2, *rem
#     return a
#
# b = f()
# print(b)


def f():
    rem = (3.4,5)
    # in 3.7 this would have created a syntax error.
    return 1,2, *rem

f()
b = f()
print(b)

# The same is the case with yield
def f():
    rem = (3.4,5)
    # in 3.7 this would have created a syntax error, however, with variable it will work fine. In 3.8 it works well in both cases.
    yield 1,2, *rem

f()
b = f()
print(b)
