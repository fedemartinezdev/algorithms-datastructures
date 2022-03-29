def letterCombinations(digits):
    digit2letters = {
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z']
    }

    if len(digits) == 0:
        return []

    combinations = digit2letters[digits[0]].copy()

    for i in range(1, len(digits)):
        digit = digits[i]
        chars = digit2letters[digit].copy()
        for j in range(len(combinations)):
            prefix = combinations.pop(0)
            for char in chars:
                combinations.append(prefix + char)

    return combinations

print(letterCombinations('222'))