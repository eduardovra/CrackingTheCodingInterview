from linked_list import LinkedList, LinkedListNode

# O(n)
# Assuming the last element as index 0
def kth_to_last(linked_list: LinkedList, kth: int) -> LinkedListNode:
    p1 = linked_list.head
    p2 = linked_list.head

    # Move p1 k elements forward
    for __ in range(kth + 1):
        p1 = p1.next

    # When p1 reaches the end, p2 will be the kth to last element
    while p1:
        p1 = p1.next
        p2 = p2.next

    return p2

assert kth_to_last(LinkedList([1,2,3]), 0).data == 3
assert kth_to_last(LinkedList([1,2,3]), 1).data == 2
assert kth_to_last(LinkedList([1,2,3]), 2).data == 1
