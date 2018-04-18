from Linked_List_Implementation import Linked_List

#This function removes the Nth last element from the list
def removeNthFromListEnd(llist,n):
    #mail pointer used as reference
    full_p = llist.head

    #pointer to remove the element
    n_pointer = llist.head

    #giving head start to the reference pointer
    while n:
        full_p=full_p.next
        n -=1

    while (full_p is not None):
        full_p = full_p.next
        n_pointer=n_pointer.next

    print("Removing element with key:",n_pointer.data)
    llist1.deleteNode(n_pointer.data)






#Driver Program

llist1 = Linked_List()
llist1.push(1)
llist1.append(2)
llist1.append(3)
llist1.append(4)
llist1.append(5)

print("Before Removig:")
llist1.printList()

removeNthFromListEnd(llist1,2)

print("After Removing 2nd element from the end")
llist1.printList()


"""
Output for above Driver Program:

Before Removig:
Head ->1 ->2 ->3 ->4 ->5 ->Tail

Removing element with key: 4
After Removing 2nd element from the end
Head ->1 ->2 ->3 ->5 ->Tail

"""