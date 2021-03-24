from linked_list import LinkedList, LinkedListNode

def detect_loop(ll: LinkedList) -> LinkedListNode:
    first_count = 0
    node_slow = ll.head.next
    node_fast = ll.head.next.next

    # Use the runner technique to find the first repeated node
    while node_slow and node_fast:
        if node_slow is node_fast:
            break

        first_count + 1
        node_slow = node_slow.next
        node_fast = node_fast.next.next if node_fast.next else None

    if node_slow is None or node_fast is None:
        return None

    node_slow = ll.head
    while True:
        if node_slow is node_fast:
            return node_slow

        node_slow = node_slow.next
        node_fast = node_fast.next


ll = LinkedList(['A', 'B', 'C', 'D', 'E'])

assert detect_loop(ll) is None

c = ll.head
for __ in range(2):
    c = c.next

ll.tail.next = c

assert detect_loop(ll) == c
