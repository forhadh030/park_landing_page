"""

odd_number = [1, 2, 1, 2, 3]
unique = []
seen = set ()
for x in odd_number:
    if x not in seen:
        unique.append(x)
        seen.add(x)

print(x)

"""

def array_diff(a, b):
    return [x for x in a if x not in b]

print(array_diff([1, 2], [1, 3]))