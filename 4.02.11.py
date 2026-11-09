class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def remove(head, value):
    if head == None:
        return None

    if head.value == value:
        head = head.next
        if head != None:
            head.prev = None
        return head

    current = head
    while current != None:
        if current.value == value:
            current.prev.next = current.next
            if current.next != None:
                current.next.prev = current.prev
            return head
        current = current.next
    return head