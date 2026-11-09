class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

def add(head, value, index):
    new_node = Node(value)

    if index == 0 or head == None:
        new_node.next = head
        return new_node

    current = head
    counter = 0

    while current.next is not None and counter < index - 1:
        current = current.next
        counter += 1

    
    new_node.next = current.next
    current.next = new_node

    return head

def prnt(head):
    current = head
    while current != None:
        print(current.value)
        current = current.next

def remove(head, value):
    if head.value == value:
        return head.next

    current = head
    while current.next != None:
        if current.next.value == value:
            current.next = current.next.next
        current = current.next
    return head

def sequence(head):
    current = head
    while current.next is not None:
        current = current.next
    an = current.value

    current = head
    while current is not None:
        print(current.value - an)
        current = current.next
