import string


chars = string.ascii_letters + string.digits
chars = string.digits
input_string = "ab*d*f"

results = [input_string]
while "*" in results[0]:
    new_results = list()
    for res in results:
        splitted_string = res.split('*')
        for i in chars:
            new_results.append(splitted_string[0]+ i + "*".join(splitted_string[1:]))
    results = new_results
print(results)
