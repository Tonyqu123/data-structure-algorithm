class Set:
    """ 使用list实现set ADT
    Set()
    length()
    contains(element)
    add(element)
    remove(element)
    equals(element)
    isSubsetOf(setB)
    union(setB)
    intersect(setB)
    difference(setB)
    iterator()
    """
    def __init__(self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)

    def __contains__(self, element):
        return element in self._theElements

    def add(self, element):
        if element not in self:
            self._theElements.append(element)

    def remove(self, element):
        assert element in self, 'The element must be set'
        self._theElements.remove(element)

    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet