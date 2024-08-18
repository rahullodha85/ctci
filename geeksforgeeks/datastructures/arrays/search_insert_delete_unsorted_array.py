class UnsortedArray:
    def __init__(self, arr):
        if len(arr) > 0:
            self.arr = arr
            return

        self.arr = []

    def search(self, x):
        for i in range(len(self.arr)):
            if self.arr[i] == x:
                return i
        return -1

    def insert(self, x):
        self.arr.append(x)

    def insert_at_index(self, x, index):
        self.arr.insert(index, x)

    def delete(self, x):
        index = self.search(x)
        if index != -1:
            self.arr.pop(index)
