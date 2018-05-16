# Node Class
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

#LinkedList
# functions included:
#   push, printList, rotate the list

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next=self.head
        self.head = new_node

    def printList(self):
        temp = self.head

        while(temp):
            print(temp.data)
            temp=temp.next


    def rotate(self,k):
        if k ==0:
            return

        curr = self.head

        count = 1

        while (count <k and curr is not None):
            curr = curr.next
            count = count +1

        # if k is greater than the size of list return
        if curr is None:
            return

        kthNode = curr

        while (curr.next is not None):
            curr = curr.next

        curr.next = self.head

        self.head = kthNode.next
        kthNode.next = None


"""
Input :
[1,2,3,4,5]
2

output:
[3,4,5,1,2]
"""