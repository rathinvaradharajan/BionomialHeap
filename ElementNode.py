class ElementNode:
    def __init__(self, value, degree=0, rest=None, children=None):
        self.value = value
        self.degree = degree
        self.rest = rest
        self.children = children

    def add_child(self, node):
        if self.children is None:
            self.children = [node]
        else:
            self.children.append(node)

    def compute_degree(self):
        self.degree = self.__compute_degree(self)

    def __compute_degree(self, node):
        if node is None or node.children is None or len(node.children) == 0:
            return 0
        else:
            return 1 + max(map(self.__compute_degree, node.children))
