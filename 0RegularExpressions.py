import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_639255.txt"
handle = open(name)

print(sum([int(number) for number in re.findall('[0-9]+', handle.read())]))
