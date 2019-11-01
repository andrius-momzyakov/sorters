class Tree:
    '''
    Sorting array by binary tree
    '''
    def __init__(self, source):
        if len(source) < 1:
            return None
        self.source = source
        self.top = None
        self.sorted = []
        self.build()

    def add(self, key):
        added = False
        if not self.top:
            self.top = self.__class__.ChildElem(key)
            return
        el = self.top
        while not added:
            if key < el.key:
                if el.left:
                    el = el.left
                    continue
                else:
                    new = self.__class__.ChildElem(key, parent=el)
                    el.left = new
                    added = True
            else:
                if el.right:
                    el = el.right
                    continue
                else:
                    new = self.__class__.ChildElem(key, parent=el)
                    el.right = new
                    added = True

    def build(self):
        '''
        tree structure builder
        :return: None
        '''
        self.top = None
        for key in self.source:
            self.add(key)

    def sort(self):
        el = self.top
        while el.parent or el == self.top:
            if el.left and (not el.left.sorted):
                el = el.left
                # el.lc = True # "is left child" mark
                continue
            else:
                if not el.sorted:
                    self.sorted.append(el.key)
                    el.sorted = True
                if el.right and (not el.right.sorted):
                    el = el.right
                    # el.rc = True
                    continue
                else:
                    if not el.sorted:
                        self.sorted.append(el.key)
                        el.sorted = True
                    if el.parent:
                        el = el.parent
                    else:
                        break
        return self.sorted

    class ChildElem:

        def __init__(self, key, parent=None):
            self.key = key
            self.parent = parent
            self.left = None
            self.right = None
            self.sorted = False
            # self.lc = False
            # self.rc = False

        def __str__(self):
            if self.key:
                return str(self.key)
            return ''


if __name__ == '__main__':
    arr = [76, 0, -3, 34, 23, 8, 66, 5, 78, 98, 4, 6, 23, 445, -99, 56, 86, 21, 6, 1]
    t = Tree(arr)
    sorted = t.sort()
    print(len(t.source), t.source)
    print(len(sorted), sorted)
