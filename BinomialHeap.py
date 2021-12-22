from ElementNode import ElementNode


class BinomialHeap:
    """
    This class represents a binomial heap.

    Attributes
    ----------
    head: ElementNode
        The start node of the binomial heap.

    Methods
    -------
    insert(value: int):
        Insert a value into the heap.

    min() -> int:
        Get the min value in the heap.

    extract_min() -> int:
        Remove the min element from the heap.

    decrease_key(key: int):
        Decrease the value of the key by 1.

    delete(key: int):
        Delete the key from the heap.

    make_heap(values: [int]):
        add the values into the heap.

    union(another: BinomialHeap):
        Combine another heap with this one.
    """

    def __init__(self):
        self.head = None

    def insert(self, value: int):
        """
        Insert an element into the heap.

        :param value: the value to be inserted.
        """
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
        while node and node.rest is not None:
            if node.degree == node.rest.degree:
                new_node = self.__union(node, node.rest)
                if previous is None:
                    self.head = new_node
                    node = self.head
                else:
                    previous.rest = new_node
                    new_node.rest = node.rest.rest if node.rest is not None else None
                    previous = new_node
                    node = new_node.rest
            else:
                previous = node
                node = node.rest

    def min(self) -> int:
        """
        Find the min value in the heap.

        :return: the min value in the heap. -1 if the heap is empty.
        """
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
        """
        Return the min value and remove it from the heap.

        :return: the min value in the heap. -1 if the heap is empty.
        """
        if self.head is None:
            return -1
        node = self.head
        ptr_to_min = ElementNode(-99, 0, self.head)
        minimum = self.head.value
        while node.rest is not None:
            if minimum > node.rest.value:
                minimum = node.rest.value
                ptr_to_min = node
            node = node.rest
        children = ptr_to_min.rest.children
        for i in range(0, len(children) - 1):
            children[i].rest = children[i + 1]
        if ptr_to_min.value != -99:
            ptr_to_min.rest = children[0]
        else:
            self.head = children[0]
        self.__validate()
        return minimum

    def __find_in_tree(self, node, key):
        if node.children is None:
            return None
        queue = [i for i in node.children]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.value == key:
                return node
            if node.children is not None:
                for i in node.children:
                    queue.append(i)

    def __find_key(self, node, key) -> ElementNode:
        while node is not None:
            if node.value == key:
                return node
            if node.children is not None:
                for i in node.children:
                    if i.value == key:
                        return i
                    else:
                        found = self.__find_in_tree(i, key)
                        if found is not None:
                            return found
            node = node.rest
        return None

    def decrease_key(self, key):
        """
        Decrease the value of the key by 1.

        :param key: the value in the heap to be decreased.
        """
        node = self.__find_key(self.head, key)
        if node is None:
            return None
        node.value = node.value - 1
        while node.parent is not None and node.parent.value > node.value:
            temp = node.value
            node.value = node.parent.value
            node.parent.value = temp
            node = node.parent

    def delete(self, key):
        """
        Delete the key from the heap.

        :param key: the key to be deleted.
        """
        node = self.__find_key(self.head, key)
        if node is None:
            return None
        node.value = 0
        while node.parent is not None and node.parent.value > node.value:
            temp = node.value
            node.value = node.parent.value
            node.parent.value = temp
            node = node.parent
        self.extract_min()

    def make_heap(self, values: [int]):
        """
        Insert the values into the heap.

        :param values: the values to be inserted.
        """
        for i in values:
            self.insert(i)

    def __print_children(self, node) -> str:
        if node.children is None:
            return ""
        queue = [i for i in node.children]
        res = ""
        while len(queue) > 0:
            x = queue.pop(0)
            res += " " + str(x.value)
            if x.children is not None:
                for i in x.children:
                    queue.append(i)
        return res

    def union(self, another):
        """
        Combine two binomial heaps into one.

        :param another: other binomial heap
        """
        node = self.head
        while node.rest is not None:
            node = node.rest
        node.rest = another.head
        self.__validate()

    def __str__(self) -> str:
        node = self.head
        result = ""
        while node is not None:
            result += str(node.value) + "|" + str(node.degree) + ": " + self.__print_children(node) + "\n"
            node = node.rest
        return result
