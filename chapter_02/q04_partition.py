from linked_list import LinkedList

# O(n)
def partition(linked_list: LinkedList, value: int) -> LinkedList:
    # Start a new linked list with the first element from the input list
    head = linked_list.head
    tail = linked_list.head
    node = linked_list.head

    while node:
        next_node = node.next
        # If the node has a value less then the threshould, then insert it to the head
        if node.data < value:
            node.next = head
            head = node
        else: # Else append it to the tail
            tail.next = node
            tail = node

        node = next_node

    tail.next = None

    return LinkedList(head)

assert partition(LinkedList([3,5,8,5,10,2,1]), 5).to_list() == [1,2,3,5,8,5,10]
