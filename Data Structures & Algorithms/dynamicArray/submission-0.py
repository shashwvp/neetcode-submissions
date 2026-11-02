class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = []
        self.capacity = capacity 
        
    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i == self.getSize():
            self.array.append(n)
        else:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.set(self.getSize(), n)
        

    def popback(self) -> int:
        temp = []
        val = self.array[self.getSize()-1]
        for i in range(self.getSize()-1):
            temp.append(self.array[i])
        self.array = temp
        return val


    def resize(self) -> None:
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.capacity
