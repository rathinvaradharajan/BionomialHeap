from ElementNode import ElementNode


class BinomialHeap:
    def __init__(self):
        self.head = None

    def insert(self, value: int):
        if self.head is None:
            self.head = ElementNode(value)
        else:
            node = ElementNode(value, 0, self.head)
            self.head = node
        self.__validate()

    @staticmethod
    def __union(node1: ElementNode, node2: ElementNode) -> ElementNode:
        if node1.value < node2.value:
            node1.add_child(node2)
            node1.compute_degree()
            node1.rest = node2.rest
            node2.rest = None
            return node1
        else:
            node2.add_child(node1)
            node2.compute_degree()
            node1.rest = None
            return node2

    def __validate(self):
        previous = None
        node = self.head
        while node.rest is not None:
            if node.degree == node.rest.degree:
                new_node = self.__union(node, node.rest)
                if previous is None:
                    self.head = new_node
                    node = self.head
                else:
                    previous.rest = new_node
                    new_node.rest = node.rest.rest
                    previous = new_node
                    node = new_node.rest
            else:
                previous = node
                node = node.rest

    def min(self) -> int:
        if self.head is None:
            return -1
        node = self.head
        minimum = self.head.value
        while node is not None:
            if minimum > node.value:
                minimum = node.value
            node = node.rest
        return minimum

    def extract_min(self) -> int:
        if self.head is None:
            return -1
        node = self.head
        ptr_to_min = None
        minimum = self.head.value
        while node.rest is not None:
            if minimum > node.rest.value:
                minimum = node.rest.value
                ptr_to_min = node
            node = node.rest
        children = ptr_to_min.rest.children
        for i in range(0, len(children) - 1):
            children[i].rest = children[i + 1]
        if ptr_to_min is not None:
            ptr_to_min.rest = children[0]
        else:
            self.head = children[0]
        self.__validate()
        return minimum

    def __str__(self) -> str:
        node = self.head
        result = ""
        while node is not None:
            result += str(node.value) + "|" + str(node.degree) + "\t"
            node = node.rest
        return result
