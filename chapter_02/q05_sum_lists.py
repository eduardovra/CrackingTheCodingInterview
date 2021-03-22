from linked_list import LinkedList, LinkedListNode

def sum_lists(list_a: LinkedList, list_b: LinkedList) -> LinkedList:
    num_a, num_b = 0, 0

    node = list_a.head
    multiplier = 1
    while node:
        num_a += node.data * multiplier
        multiplier *= 10
        node = node.next

    node = list_b.head
    multiplier = 1
    while node:
        num_b += node.data * multiplier
        multiplier *= 10
        node = node.next

    sum_result = num_a + num_b

    node = None
    head = None
    digit_index = 0
    while True:
        digit = sum_result // 10 ** digit_index % 10
        if digit == 0:
            break
        digit_index += 1

        new_node = LinkedListNode(digit)
        if node:
            node.next = new_node
        else:
            head = new_node

        node = new_node

    node.next = None

    return LinkedList(head)

assert sum_lists(LinkedList([7,1,6]), LinkedList([5,9,2])).to_list() == [2,1,9]
