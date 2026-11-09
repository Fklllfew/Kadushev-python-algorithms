def sequence(head):
    if head == None:
        return

    tail = head
    while tail.next != None:
        tail = tail.next

    left = head
    right = tail

    while left != None and right != None and left != right and left.prev != right:
        print(left.value - right.value)
        left = left.next
        right = right.prev