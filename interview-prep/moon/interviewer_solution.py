import string

alphanum = string.ascii_letters + string.digits
alphanum = string.digits
input_string = "ab*d*f"

def expand_one_star(input_str):
    if '*' in input_str:
        for x in alphanum:
            replacement = input_str.replace('*', x, 1)
            if '*' in replacement:
                for sub_replacement in expand_one_star(replacement):
                    yield sub_replacement
            else:
                yield replacement
    yield input_str

print(list(expand_one_star(input_string)))