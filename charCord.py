"""
"""
class Internal:
    def __init__(self, length = 0):
        self.right = None
        self.left = None
        self.length = length

class Leaf:
    def __init__(self, length = 0, chord = ""):
        self.length = length
        self.chord = chord

def getNthCharFromCord(node, N):
    if type(node) is Internal:
        if N >= node.length:
            return None
        if node.left is not None:
            if N < node.left.length:
                return getNthCharFromCord(node.left, N)
            newN = N - node.left.length
            if node.right is not None and newN <= node.right.length:
                return getNthCharFromCord(node.right, newN)
    elif type(node) is Leaf:
        return node.chord[N]

    return None

root = Internal(10)
root.left = Leaf(4, "ABCD")
root.right = Internal(6)
root.right.left = Leaf(6, "EFGHIJ")
root.right.right = None

print(getNthCharFromCord(root, 10))