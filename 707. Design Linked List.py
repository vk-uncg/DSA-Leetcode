class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        curr = self.head
        if curr is None:
            self.head = node
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        curr = self.head
        if index<0 or index > self.size:
            return -1
        if index == 0:
            self.addAtHead(val)
        else:
            for i in range(index-1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index >= self.size:
            return -1
        curr = self.head
        if index==0:
            self.head = curr.next
        else:
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)