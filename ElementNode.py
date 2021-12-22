class ElementNode:
    """
    This class represents each node of the heap.

    Attributes
    ----------
    value:
        The value in the node.
    degree: int
        The degree of the node (height of the tree rooted at this node).
    rest: ElementNode
        The node next to this.
    children: [ElementNode]
        List of children of this node.

    Methods
    -------
    add_child(node):
        Add a child to this node.

    compute_degree():
        compute the degree of this node.
    """

    def __init__(self, value, degree=0, rest=None, children=None):
        """
        Create a node.

        :param value: the node value.
        :param degree: the node's degree. defaulted to 0
        :param rest: the next node.
        :param children: children node.
        """
        self.value = value
        self.degree = degree
        self.rest = rest
        self.children = children
        self.parent = None

    def add_child(self, node):
        """
        Add a child to the node.

        :param node: the child to be added.
        """
        if self.children is None:
            self.children = [node]
        else:
            self.children.append(node)
        node.parent = self

    def compute_degree(self):
        """
        Compute the degree of the node.
        """
        self.degree = self.__compute_degree(self)

    def __compute_degree(self, node):
        if node is None or node.children is None or len(node.children) == 0:
            return 0
        else:
            return 1 + max(map(self.__compute_degree, node.children))
