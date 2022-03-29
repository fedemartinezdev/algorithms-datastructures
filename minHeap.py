import random

class MinHeap:
    def __init__(self, array):
        self.heap = array.copy()
        self.buildHeap()

    def buildHeap(self):
        parentIdx = (len(self.heap) - 1) // 2
        for idx in reversed(range(parentIdx)):
            self.siftDown(idx, len(self.heap)-1)

    def siftDown(self, currentIdx, endIdx):
        while currentIdx <= endIdx // 2:
            childLeft = 2 * currentIdx + 1
            childRight = childLeft + 1
            if childLeft <= endIdx and self.heap[childLeft] < self.heap[currentIdx]:
                if childRight <= endIdx and self.heap[childRight] < self.heap[childLeft]:
                    self.heap[childRight], self.heap[currentIdx] = self.heap[currentIdx], self.heap[childRight]
                    currentIdx = childRight
                else:
                    self.heap[childLeft], self.heap[currentIdx] = self.heap[currentIdx], self.heap[childLeft]
                    currentIdx = childLeft
            elif childRight <= endIdx and self.heap[childRight] < self.heap[currentIdx]:
                self.heap[childRight], self.heap[currentIdx] = self.heap[currentIdx], self.heap[childRight]
                currentIdx = childRight
            else:
                break

    def siftUp(self, currentIdx):
        while currentIdx > 0:
            parentIdx = (currentIdx-1) // 2
            if self.heap[parentIdx] < self.heap[currentIdx]:
                break
            self.heap[parentIdx], self.heap[currentIdx] = self.heap[currentIdx], self.heap[parentIdx]
            currentIdx = parentIdx

    def peek(self):
        return self.heap[0]

    def remove(self):
        if not self.heap:
            print('Heap is empty', end=' ')
            return

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        value = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1)
        return value

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

#data = [61, 24, 77, 1, 99, 76, 100, 90, 10, 2, 9]
data = [61]
myheap = MinHeap(data)
print(myheap.remove())
print(myheap.remove())