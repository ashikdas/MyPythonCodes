class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        # Write your code here
        previous = None
        current = head

        # take an empty set to store linked list nodes for future reference
        s = set()

        # do till the linked list is empty
        while current:

            # if the current node is seen before, ignore it
            if current.data in s:
                previous.next = current.next

            # insert the current node into the set and proceed to the next node
            else:
                s.add(current.data)
                previous = current

            current = previous.next

        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
