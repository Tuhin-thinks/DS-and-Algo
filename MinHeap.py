import sys

class MinHeap():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)  # creates a list of length (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        """
        function will return the position of the parent for the 
        element currently at pos
        """
        return pos//2
    
    def leftchild(self, pos):
        """
        Function will return the position of the left child for the
        node currently at pos
        """
        return (2* pos + 1)
    
    def rightchild(self, pos):
        """
        Function will return the position of the right child for the node
        currently at pos
        """
        return (2 * pos + 2)

    def isleaf(self, pos):
        """
        Function will return true if the node at pos is a leaf node
        """
        if self.size//2 <= pos <= self.size:
            return True
        else:
            return False
    
    def swap(self, fpos, spos):
        """
        This function will swap two nodes of the heap
        """
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
    
    def minHeapify(self, pos):
        """
        Function to heapify the node at pos
        """
        # if any of the node is a non-leaf node and greater than any of it's
        # child
        if not self.isleaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftchild(pos)]) or (self.Heap[pos] > self.Heap[self.rightchild(pos)]):

                # swap with the left child and heapify the left child tree
                if self.Heap[self.leftchild(pos)] < self.Heap[self.rightchild(pos)]:
                    self.swap(pos, self.leftchild(pos))
                    self.minHeapify(self.leftchild(pos))
                # swap with the right child and heapify the right child tree
                else:
                    self.swap(pos, self.rightchild(pos))
                    self.minHeapify(self.rightchild(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:  # max-heap rule, parent is greater than any of it's child
            self.swap(current, self.parent(current))
    
    def Print(self):
        for i in range(1, (self.size//2)+1):
            print("PARENT:"+str(self.Heap[i])+" LEFT CHILD: "+str(self.Heap[2*i])+" RIGHT CHILD: "+str(self.Heap[2*i+1]))

    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)
    
    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped

if __name__ == "__main__":
    print("The minHeap is ")
    minHeap = MinHeap(15)
    elements = [5,3,17,10,84,19,6,22,9]
    for i in elements:
        minHeap.insert(i)
    minHeap.minHeap()

    minHeap.Print()
    print("The Min val is "+ str(minHeap.remove()))