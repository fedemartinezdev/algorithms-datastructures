class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = self.tail.next

    def moveToEnd(self, node):
        if node.next is None:
            return
        elif node.prev is None:
            self.head = node.next
            node.next.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = None
        node.next = None
        self.add(node)

    def popHead(self):
        key = self.head.key

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

        return key

    def print(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodesMap = {}
        self.linkedList = LinkedList()
    
    def get(self, key: int) -> int:
        if key in self.nodesMap:
            node = self.nodesMap[key]
            self.linkedList.moveToEnd(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:        
        if key in self.nodesMap:
            node = self.nodesMap[key]
            node.value = value
            self.linkedList.moveToEnd(node)
            return
        
        if len(self.nodesMap) < self.capacity:
            node = Node(key, value)
            self.nodesMap[key] = node
            self.linkedList.add(node)
            return
        
        oldestKey = self.linkedList.popHead()
        self.nodesMap.pop(oldestKey)
        node = Node(key, value)
        self.nodesMap[key] = node
        self.linkedList.add(node)

# myNodes = {
#     5: Node("Feder"),
#     1: Node("F"),
#     2: Node("Fe"),
#     3: Node("Fed")
# }

# myList = LinkedList()
# myList.add(myNodes[5])
# myList.add(myNodes[1])
# myList.add(myNodes[2])
# myList.add(myNodes[3])

# print(myNodes[5].prev)
# print(myNodes[5].next)

# myList.moveToEnd(myNodes[5])
# myList.popHead()
# myList.popHead()
# myList.print()

# lRUCache = LRUCache(2)
# lRUCache.put(1, 1)     # cache is {1=1}
# lRUCache.put(2, 2)     # cache is {1=1, 2=2}
# print(lRUCache.get(1)) # return 1
# lRUCache.put(3, 3)     # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache.get(2)) # returns -1 (not found)
# lRUCache.put(4, 4)     # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(lRUCache.get(1)) # return -1 (not found)
# print(lRUCache.get(3)) # return 3
# print(lRUCache.get(4)) # return 4

# ["LRUCache","put","get","put","get","get"]
# [[1],[2,1],[2],[3,2],[2],[3]]
lRUCache = LRUCache(1)
lRUCache.put(2, 1)
print(lRUCache.get(2))
lRUCache.put(3, 2)
print(lRUCache.get(2))
print(lRUCache.get(3))