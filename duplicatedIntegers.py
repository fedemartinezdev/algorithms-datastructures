def duplicatedIntegers(integers):
    freq = {}
    duplicates = set()
    result = []

    for value in integers:
        if value not in freq:
            freq[value] = 0
        freq[value] += 1
        
        if value in duplicates:
            result.append(value)
        else:
            duplicates.add(value)

    return result

print(duplicatedIntegers([0, 1, 1]))
print(duplicatedIntegers([1, 1, 2, 3, 4, 2]))