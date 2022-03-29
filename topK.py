def topK(nums, k):
    freqs = {}
    indices = []

    for num in nums:
        if num not in freqs:
            freqs[num] = 0
            indices.append(num)
        freqs[num] += 1

    print(indices)

    #return buildHeap(freqs, k)
    KIdx = quickSelect(indices, k, freqs)
    return indices[KIdx:]

def buildHeap(freqs, k):
    heap = []
    for freq in freqs.items():
        insert(heap, freq, freqs, k)
    return heap

def insert(heap, freq, freqs, k):
    if len(heap) < k:
        heap.append(freq[0])
        siftUp(heap, len(heap)-1, freqs)
    elif freq[1] > freqs[heap[0]]:
        heap[0] = freq[0]
        siftDown(heap, 0, k-1, freqs)

def siftUp(heap, currentIdx, freqs):
    while currentIdx > 0:
        parentIdx = (currentIdx-1) // 2
        if freqs[heap[parentIdx]] < freqs[heap[currentIdx]]:
            break
        heap[parentIdx], heap[currentIdx] = heap[currentIdx], heap[parentIdx]
        currentIdx = parentIdx

def siftDown(heap, currentIdx, endIdx, freqs):
    while currentIdx <= endIdx // 2:
        childLeft = 2 * currentIdx + 1
        childRight = childLeft + 1
        if childLeft <= endIdx and freqs[heap[childLeft]] < freqs[heap[currentIdx]]:
            if childRight <= endIdx and freqs[heap[childRight]] < freqs[heap[childLeft]]:
                heap[childRight], heap[currentIdx] = heap[currentIdx], heap[childRight]
                currentIdx = childRight
            else:
                heap[childLeft], heap[currentIdx] = heap[currentIdx], heap[childLeft]
                currentIdx = childLeft
        elif childRight <= endIdx and freqs[heap[childRight]] < freqs[heap[currentIdx]]:
            heap[childRight], heap[currentIdx] = heap[currentIdx], heap[childRight]
            currentIdx = childRight
        else:
            break

def quickSelect(nums, k, freqs):
    k = len(nums) - k
    return quickSelectHelper(nums, k, 0, len(nums)-1, freqs)

def quickSelectHelper(nums, k, leftIdx, rightIdx, freqs):
    P = nums[rightIdx]
    L = leftIdx
    for i in range(leftIdx, rightIdx):
        if freqs[nums[i]] <= freqs[P]:
            nums[i], nums[L] = nums[L], nums[i]
            L += 1

    nums[L], nums[rightIdx] = nums[rightIdx], nums[L]

    if L > k:
        return quickSelectHelper(nums, k, leftIdx, L - 1, freqs)
    elif L < k:
        return quickSelectHelper(nums, k, L + 1, rightIdx, freqs)
    else:
        return L

print(topK([1], 1))