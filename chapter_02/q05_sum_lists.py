from linked_list import LinkedList, LinkedListNode

def sum_lists(list_a: LinkedList, list_b: LinkedList) -> LinkedList:
    out_node = LinkedListNode(0)

    def recursive_sum(node_a, node_b, carry, out_node):
        if not node_a and not node_b:
            if carry:
                out_node.next = LinkedListNode(carry)
            return

        d_a = node_a.data if node_a else 0
        d_b = node_b.data if node_b else 0
        res = d_a + d_b + carry
        carry = 0
        if res > 9:
            res = res - 10
            carry = 1

        new_node = LinkedListNode(res)
        if out_node:
            out_node.next = new_node
        out_node = new_node

        next_a = node_a.next if node_a else None
        next_b = node_b.next if node_b else None

        return recursive_sum(next_a, next_b, carry, out_node)

    recursive_sum(list_a.head, list_b.head, 0, out_node)

    return LinkedList(out_node.next)

def sum_lists_forward_order(list_a: LinkedList, list_b: LinkedList) -> LinkedList:
    head_a = list_a.head
    head_b = list_b.head

    # Make sure the two lists have the same length
    len_a = 0
    node = head_a
    while node:
        len_a += 1
        node = node.next
    len_b = 0
    node = head_b
    while node:
        len_b += 1
        node = node.next

    if len_a != len_b:
        bigger = max([len_a, len_b])
        smaller = min([len_a, len_b])

        zeros_to_add = bigger - smaller
        pad = [0] * zeros_to_add
        pad_list = LinkedList(pad)

        if len_a > len_b:
            pad_list.head.next = head_b
            head_b = pad_list.head
        else:
            pad_list.head.next = head_a
            head_a = pad_list.head

    def add_lists(node_a, node_b):
        if not node_a and not node_b:
            return [None, 0]

        ret = add_lists(node_a.next, node_b.next)
        node, carry = ret
        s = carry + node_a.data + node_b.data
        carry = 0
        if s > 9:
            s -= 10
            carry = 1

        new_node = LinkedListNode(s)
        if node:
            new_node.next = node

        node = new_node

        return node, carry

    node, carry = add_lists(head_a, head_b)

    if carry:
        new_node = LinkedListNode(carry)
        new_node.next = node
        node = new_node

    return LinkedList(node)


assert sum_lists(LinkedList([7,1,6]), LinkedList([5,9,2])).to_list() == [2,1,9]
assert sum_lists(LinkedList([9,7,8]), LinkedList([6,8,5])).to_list() == [5,6,4,1]

assert sum_lists_forward_order(LinkedList([1,3]), LinkedList([9,8,7])).to_list() == [1,0,0,0]
assert sum_lists_forward_order(LinkedList([6,1,7]), LinkedList([2,9,5])).to_list() == [9,1,2]
assert sum_lists_forward_order(LinkedList([8,7,9]), LinkedList([5,8,6])).to_list() == [1,4,6,5]
