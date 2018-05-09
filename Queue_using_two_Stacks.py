"""

@author: Bhoomit Patel

"""

class stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.size() == 0

class QueueUsingTwoStacks:

    def __init__(self):
        self.stack1 = stack()
        self.stack2 = stack()

    # Use first stack to enqueue elements
    def enqueue(self,data):
        self.stack1.push(data)
        print(data,"enqueued")

    # to dequeue move all the elements to second stack
    # pop the element from the second stack
    # and put all the elements back to first stack
    def dequeue(self):
        if not self.stack1.is_empty():
            while self.stack1.size()>0:

                self.stack2.push(self.stack1.pop())

        res = self.stack2.pop()

        while self.stack2.size()>0:
            self.stack1.push(self.stack2.pop())

        return res



if __name__ == '__main__':


    q = QueueUsingTwoStacks()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    a = q.dequeue()

    print(a,"dequeued")


"""

output :

1 enqueued
2 enqueued
3 enqueued
1 dequeued

"""

