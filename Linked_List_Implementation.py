# Node Class
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

# Linked_List class
class Linked_List:

    def __init__(self):
        self.head = None

    #prints the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    #add the node in the front of the linked list
    def push(self,new_data):
        new_node = Node(new_data)

        new_node.next=self.head
        self.head = new_node


    # Insert the node after the previous Node
    #if the node is not present print "not in the linked list"
    def insertAfter(self,prev_data,new_data):

        if prev_data is None:
            print("The previous node is not in the list")

        new_node = Node(new_data)
        new_node.next = prev_data.next
        prev_data.next = new_node

    # if the list is empty, then make the new node as head
    #if not add at the end.
    def append(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            new_node = self.head
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next=new_node


    # delete the node
    def deleteNode(self,key):

        temp = self.head

        #if head is the key
        #assigns the next node as head and deletes the node.
        if(temp is not None):
            if(temp.data==key):
                self.head = temp.next
                temp=None
                return

        while (temp is not None):
            if(temp.data==key):
                break
            prev=temp
            temp=temp.next

        if (temp == None):
            return

        prev.next=temp.next

        temp=None

#Code Execution

if __name__ == "__main__":

#   creating the list
    llist = Linked_List()

    llist.head=Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next=third

#   1->2->3

#adding nodes
    llist.push(5)
    llist.insertAfter(second,4)

    llist.append(9)
#5->1->2->4->3->9

    llist.deleteNode(9)
#5->1->2->4->3
    llist.printList()


