import string

alphanum = string.ascii_letters + string.digits
alphanum = string.digits
input_string = "ab*d*f*h"

def expand_one_star(input_str):
    if '*' in input_str:
        for x in alphanum:
            replacement = input_str.replace('*', x, 1)
            if '*' in replacement:
                for sub_replacement in expand_one_star(replacement):
                    yield sub_replacement
            else:
                yield replacement
    yield input_str # the interviewer made a mistake here, this should be under an else statement bcuz otherwise strings containing * will be printed

#This is my reimplementaion (for practice - made without looking)
def expand_star(input_str):
    if "*" not in input_str:
        yield input_str
    
    for i in alphanum:
        replaced = input_str.replace("*", i, 1)
        if '*' not in replaced:
            yield replaced
        else:
            for i in expand_star(replaced):
                yield i
                

print(list(expand_one_star(input_string))) # interviewer
# print(list(expand_star(input_string))) # me
