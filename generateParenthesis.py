def generateParenthesis(n):
    stack = ["()"]
    seenString = set()
    
    counter = 0
    while len(stack) and counter < 6:
        if len(stack[0]) == n*2:
            break

        base = stack.pop(0)
        
        for i in range(len(base) + 1):
            newString = base[:i] + "()" + base[i:]
            addString(newString, seenString, stack)
    
        counter += 1
    return stack
    
def addString(newString, seenString, stack):
    if newString not in seenString:
        stack.append(newString)
        seenString.add(newString)

print(generateParenthesis(3))