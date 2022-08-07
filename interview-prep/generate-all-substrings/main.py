#!/usr/bin/env python3
str="abcd"
l_pointer=0
all_substrs=[]
for l_pointer,_ in enumerate(str):
    for r_pointer,_ in enumerate(str[l_pointer:]):
        r_pointer+=l_pointer
        all_substrs.append(str[l_pointer:r_pointer+1])
print(all_substrs)