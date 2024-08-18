class SortedArray:
    def __init__(self, arr=[]):
        self.arr = arr

    def search(self, arr, x):
        if len(arr) == 0:
            return -1
        if len(arr) == 1:
            if arr[0] == x:
                return 0
            else:
                return -1
        mid = len(arr) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return self.search(arr[mid:], x)
        elif self.arr[mid] > x:
            return self.search(arr[:mid], x)
        else:
            return -1
