import graphviz

# Node class representing a node in a binary tree
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class SearchBinaryTree:
    def __init__(self):
        self.root = None
 
    # Method to insert a new node with the given value into the tree
    def insert(self, value):
        newNode = Node(value)
        #se a árvore estiver vazia
        if not self.root:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                father = currentNode
                if value < currentNode.value:
                    currentNode = currentNode.left
                    if currentNode == None:
                        father.left = newNode
                        return
                else:
                    currentNode = currentNode.right
                    if currentNode == None:
                      father.right = newNode
                      return
                    
    def search(self, value):
        currentNode = self.root
        while currentNode.value != value:
            if value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
            if currentNode == None:
                return None
        
        return currentNode
    
    def Preorder(self, node):
        if node != None:
            print(node.value)
            self.Preorder(node.left)
            self.Preorder(node.right)
    
    def order(self, node):
        if node != None:
            self.Preorder(node.left)
            print(node.value)
            self.Preorder(node.right)
    
    def posorder(self, node):
        if node != None:
            self.Preorder(node.left)
            self.Preorder(node.right)    
            print(node.value)

    def delet(self, value):
        if self.root == None:
            print("empty tree")
            return
        
        #search
        currentNode = self.root
        father = self.root
        eLeft = True

        while currentNode.value != value:
            father = currentNode
            #left
            if value < currentNode.value:
                eLeft = True
                currentNode = currentNode.left
            #rigth
            else:
                eLeft = False
                currentNode = currentNode.right
    
            if currentNode == None:
                return False
            #delet sheet
            if currentNode.left == None and currentNode.right == None:
                if currentNode ==  self.root:
                    self.root = None
                elif eLeft == True:
                    father.left = None
                else:
                    father.right = None
            # no node in right
            elif currentNode.right == None:
                if currentNode == self.root:
                    self.root = currentNode.left
                elif eLeft == True:
                    father.left = currentNode.left
                else:
                    father.right = currentNode.left
            # no node in left        
            elif currentNode.left == None:
                if currentNode == self.root:
                    self.root = currentNode.right
                elif eLeft == True:
                    father.left = currentNode.right
                else :
                    father.right = currentNode.right
        
            else:
                succ = self.get_succ(currentNode)
                if currentNode == self.root:
                    self.root = succ
                elif eLeft == True:
                    father.left = succ
                else:
                    father.right = succ
                
                succ.left = currentNode.left
                return True
            
    def get_succ(self, node):
        succParent = node
        succ = node
        currentNode = node.right
        while currentNode != None:
            succParent = succ
            succ = currentNode
            currentNode = currentNode.left
        if succ != node.right:
            succParent.left = succ.right
            succ.right = node.right
        return succ
     





                    
    def visualize_binary_tree(self, root):
        dot = graphviz.Digraph()
        dot.node(str(root.value))

        def add_nodes_edges(node):
            if node.left:
                dot.node(str(node.left.value))
                dot.edge(str(node.value), str(node.left.value))
                add_nodes_edges(node.left)
            if node.right:
                dot.node(str(node.right.value))
                dot.edge(str(node.value), str(node.right.value))
                add_nodes_edges(node.right)

        add_nodes_edges(root)
        dot.render('binary_tree', view=True, format='png')

arvore = SearchBinaryTree()
arvore.insert(53)
arvore.insert(30)
arvore.insert(14)
arvore.insert(39)
arvore.insert(9)

arvore.insert(23)
arvore.insert(34)
arvore.insert(49)
arvore.insert(72)
arvore.insert(61)
arvore.insert(84)
arvore.insert(79)
arvore.delet(79)

arvore.visualize_binary_tree(arvore.root)