from array import array
import string


chars = string.ascii_letters + string.digits
input_string = "ab*d*f"

results = [input_string]
while 1:
    if "*" not in results[0]:
        break
    new_results = list()
    for res in results:
        splitted_string = res.split('*')
        for i in chars:
            new_results.append(splitted_string[0]+ i + "*".join(splitted_string[1:]))
    results = new_results
print(results)
