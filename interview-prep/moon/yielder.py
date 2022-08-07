import string
# Since I learned about generators here I do some practice
def yielder(input):
    if len(input) == 1:
        yield "1"
    for i in list(input):
        yield i.upper()

print(list(yielder("Abc")))