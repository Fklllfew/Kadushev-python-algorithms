class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

def search(head, element):
    current = head

    while current != None:
        if current.value == element:
            return True
        current = current.next
    return False
