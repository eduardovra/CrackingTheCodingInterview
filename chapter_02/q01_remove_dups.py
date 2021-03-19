from linked_list import LinkedList

def remove_dups(linked_list: LinkedList) -> LinkedList:
    values = set()
    previus = None
    node = linked_list.head

    while node:
        if node.data in values:
            previus.next = node.next
        else:
            values.add(node.data)
            previus = node

        node = node.next

    return linked_list

assert remove_dups(LinkedList([1,2,3])).to_list() == [1,2,3]
assert remove_dups(LinkedList([1,1,3])).to_list() == [1,3]
