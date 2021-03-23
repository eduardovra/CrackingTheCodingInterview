from linked_list import LinkedList, LinkedListNode

def get_len_tail(node):
    len_ll = 0
    tail = None

    while node:
        tail = node
        len_ll += 1
        node = node.next

    return len_ll, tail

def skip_nodes(node, length):
    while length:
        length -= 1
        node = node.next

    return node

# O(a + b)
def intersects(list_a: LinkedListNode, list_b: LinkedListNode) -> LinkedListNode:
    len_a, tail_a = get_len_tail(list_a)
    len_b, tail_b = get_len_tail(list_b)

    if tail_a is not tail_b:
        return None

    node_a, node_b = list_a, list_b
    if len_a > len_b:
        node_a = skip_nodes(node_a, len_a - len_b)
    else:
        node_b = skip_nodes(node_b, len_b - len_a)

    while node_a is not node_b:
        node_a = node_a.next
        node_b = node_b.next

    return node_a


ll_a = LinkedList([3,1,5,9])
ll_b = LinkedList([4,6])
ll_c = LinkedList([7,2,1])
ll_a.tail.next = ll_c.head
ll_b.tail.next = ll_c.head

assert intersects(ll_a.head, ll_b.head) is ll_c.head

ll_a = LinkedList([3,1,5,9,7,2,1]).head
ll_b = LinkedList([4,6,7,2,1]).head

assert intersects(ll_a, ll_b) is None
