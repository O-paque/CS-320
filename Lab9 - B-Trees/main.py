class BTree:
    def __init__(self, keys=[], children=[], max_size=4):
        self._keys = keys
        self._children = children
        self.max_size = 4

    def __repr__(self):
        return self.__str__()

    def string(self, level=0):
        ret = "\t" * level + repr(self._keys) + ", level: " + str(level) + "\n"

        if self._children == [] or self._children[0] is None:
            return ret

        for child in self._children:
            ret += child.string(level + 1)
        return ret
    
    def __str__(self):
        return self.string()

    def keys(self):
        return self._keys

    def children(self):
        if self._children is None or self.children == []:
            return None
        if self._children[0] is None:
            return None
        return self._children
        
