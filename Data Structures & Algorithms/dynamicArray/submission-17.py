class DynamicArray:
    
    def __init__(self, capacity: int):
        # Initialize the array with the given capacity and set length to 0
        self.arr = [0] * capacity
        self.length = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
       return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # Set the value at the index i to n
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # If the array is full, resize it to accommodate more elements
        if self.length == self.capacity:
            self.resize()
        
        # Add the new element at the end of the array and increment the length
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        # If there are elements in the array, decrement the length and return the last element
        if self.length > 0:
            self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        # Double the capacity of the array
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity

        # Copy the existing elements to the new array
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        # Return the current number of elements in the array
        return self.length
    
    def getCapacity(self) -> int:
        # Return the current capacity of the array
        return self.capacity
