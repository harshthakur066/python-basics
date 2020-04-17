li = ['a', 'b', 'b', 'd', 'e', 'f', 'f', 'f', 'g']

duplicates = []

for value in li:
    if li.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

# Comprehension way

duplicate = list(set([value for value in li if li.count(value) > 1]))

print(duplicate)
