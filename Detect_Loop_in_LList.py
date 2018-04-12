from Linked_List_Implementation import Linked_List

class features(Linked_List):

    def detectLoop(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while(slow_pointer and fast_pointer and fast_pointer.next):
            print(slow_pointer.data,fast_pointer.data,fast_pointer.next.data)
            slow_pointer= slow_pointer.next
            fast_pointer=fast_pointer.next.next
            if(slow_pointer==fast_pointer):
                print("Loop Found")
                return


llist = features()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(1)
llist.push(2)
llist.printList()
#creating a loop
llist.head.next.next.next.next = llist.head

llist.detectLoop()

"""
Current Loop:
Head
2
1
5
4
3
2
1
Tail


2 2 1
1 5 4
5 2 1
4 5 4
Loop Found
"""
