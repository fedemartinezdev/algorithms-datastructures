def wordInGrid(board, word):
    instack = set()
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if foundWord(board, i, j, word, 0, instack):
                return True

    return False
    
def foundWord(board, i, j, word, position, instack):
    if position + 1 == len(word):
        return True
    
    key = str(i) + '-' + str(j)
    if key not in instack:
        if board[i][j] != word[position]:
            return False

        instack.add(key)
        
        for neighbor in getNeighbors(board, i, j):
            ni, nj = neighbor
            nkey = str(ni) + '-' + str(nj)
            if nkey in instack:
                continue
            if foundWord(board, ni, nj, word, position + 1, instack):
                return True
                
    instack.remove(key)
    return False
    
def getNeighbors(board, i, j):
    neighbors = []
    
    if i - 1 >= 0:
        neighbors.append((i-1, j))
    if i + 1 < len(board):
        neighbors.append((i+1, j))
    if j - 1 >= 0:
        neighbors.append((i, j-1))
    if j + 1 < len(board[0]):
        neighbors.append((i, j+1))
        
    return neighbors

result = wordInGrid([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]],"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
print(result)