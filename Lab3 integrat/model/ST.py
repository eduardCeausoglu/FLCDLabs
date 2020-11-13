from src.model.BST import BST

class ST:
    def __init__(self):
        self.bst = BST()

    def getIndex(self, val):
        return self.bst.search(val)

    def insert(self, val):
        return self.bst.insert(val)

    def toString(self):
        return ' '.join(self.bst.inorder())


