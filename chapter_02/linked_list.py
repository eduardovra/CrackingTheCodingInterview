class LinkedListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, values: list) -> None:
        self.head = None
        self.tail = None

        if isinstance(values, LinkedListNode):
            self.head = values
        elif values:
            self.head = cur_node = LinkedListNode(values.pop(0))

            for value in values:
                cur_node.next = LinkedListNode(value)
                cur_node = cur_node.next

        # Find tail
        node = self.head
        while node:
            self.tail = node
            node = node.next

    def to_list(self) -> list:
        l = []
        node = self.head
        while node:
            l.append(node.data)
            node = node.next
        return l
