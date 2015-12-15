class binaryTree(object):
    def __init__(self, character, encoding, priority):
        self.character = character
        self.encoding = encoding
        self.priority = priority
        self.leftBranch= None
        self.rightBranch= None
        self.parent= None
    def setLeftBranch(self, node):
        self.leftBranch= node
    def setRightBranch(self, node):
        self.rightBranch= node
    def setParent(self, parent):
        self.parent= parent
    def getPriority(self):
        return self.priority
    def getLeftBranch(self):
        return self.leftBranch
    def getRightBranch(self):
        return self.rightBranch
    def getParent(self):
        return self.parent
    def __str__(self):
        return [self.character, self.encoding, self.priority]
    def printTree(self, node):
        if(node != None):
            self.printTree(node.leftBranch)
            if node.character != "EMPTY":
                print(str(node.character) + ": " + str(node.encoding))
            self.printTree(node.rightBranch)

def encode(root):
    root.encoding = ""
    codes = {}
    queue = [root]
    while len(queue) > 0:
        temp = queue.pop(0)
        if temp.getRightBranch():
            queue.insert(0, temp.getRightBranch())
            temp.getRightBranch().encoding = temp.encoding + '1'
            if temp.getRightBranch().character != "EMPTY":
                codes[temp.getRightBranch().character] = temp.getRightBranch().encoding
        if temp.getLeftBranch():
            queue.insert(0, temp.getLeftBranch())
            temp.getLeftBranch().encoding = temp.encoding + '0'
            if temp.getLeftBranch().character != "EMPTY":
                codes[temp.getLeftBranch().character] = temp.getLeftBranch().encoding
    return codes

def encode_string(string_to_encode, codes):
    encoded_string = ''
    for element in string_to_encode:
        encoded_string += codes[element]
    return encoded_string

def enqueue(element, queue):
    return [x for x in queue if x.priority < element.priority] + [element] + [x for x in queue if x.priority >= element.priority]
