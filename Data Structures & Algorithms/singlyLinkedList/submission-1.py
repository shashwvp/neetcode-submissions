class LinkedList:
    
    def __init__(self):
        self.llist = []
    
    def get(self, index: int) -> int:
        if index >= 0 and index < len(self.llist):
            return self.llist[index]
        return -1

    def insertHead(self, val: int) -> None:
        newLList = [val]
        for i in range(len(self.llist)):
            newLList.append(self.llist[i])
        self.llist = newLList

    def insertTail(self, val: int) -> None:
        self.llist.append(val)

    def remove(self, index: int) -> bool:
        if len(self.llist) == 0 or index >= len(self.llist):
            return False
        if index == 0:
            self.llist = self.llist[1:] 
        elif index == len(self.llist)-1:
            self.llist = self.llist[0:len(self.llist)-1]
        elif index > 0 or index < len(self.llist):
            self.llist = self.llist[0:index] + self.llist[index+1:len(self.llist)]
        return True

    def getValues(self) -> List[int]:
        return self.llist
        
