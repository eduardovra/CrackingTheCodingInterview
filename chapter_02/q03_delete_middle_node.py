from linked_list import LinkedList, LinkedListNode

# O(1)
def delete_middle_node(node: LinkedListNode) -> None:
    if not node or not node.next:
        return
    
    node.data = node.next.data
    node.next = node.next.next


linked_list = LinkedList(['a', 'b', 'c', 'd', 'e', 'f'])
node = linked_list.head
while node:
    if node.data == 'c':
        break
    node = node.next

delete_middle_node(node)

assert linked_list.to_list() == ['a', 'b', 'd', 'e', 'f']
