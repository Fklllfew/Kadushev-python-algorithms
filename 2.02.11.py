class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def reverse(head):
    current = head

    while current.next != None:
        current = current.next

    while current.prev != None:
        print(current.value)
        current = current.prev
    print(current.value)