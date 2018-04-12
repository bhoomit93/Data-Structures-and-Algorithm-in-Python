"""

@author: Bhoomit Patel
Data: 04/2018

"""

class Queue():

    #Constructor creats an empty list
    def __init__(self):
        self.queue = []

    #to add element to the queue
    def enqueue(self,data):
        self.queue.insert(0,data)

    #to remove the element from the queue
    def dequeue(self):
        self.queue.pop()

    #This function prints the queue
    def printQueue(self):
        print("rear ->",self.queue,"-> front")

    #This function returns the size of the queue
    def size(self):
        if len(self.queue) == 0:

            print("The Queue is Empty!")
        print(len(self.queue))

    #This function return the front element
    def qFront(self):
        print("Front element is",self.queue[0])

    #This function returns the rear element
    def qRear(self):
        print("Rear element is",self.queue[len(self.queue)-1])

#Driver program to check functions

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.printQueue()

q.size()

q.dequeue()
q.printQueue()

"""

rear -> [5, 4, 3, 2, 1] -> front
5
rear -> [5, 4, 3, 2] -> front

"""