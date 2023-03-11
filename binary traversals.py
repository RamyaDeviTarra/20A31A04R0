class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key
def printInorder(root):
    if root:
        #1st recursion on left child
        printInorder(root.left)
        #print the data of node
        print(root.value,end = ' ')
        #now recursion on right child
        printInorder(root.right)

def printPreorder(root):
    if root:
        #print the data of node
        print(root.value,end = ' ')
        #1st recursion on left child
        printPreorder(root.left)
         #now recursion on right child
        printPreorder(root.right)
def printPostorder(root):
    if root:
        #1st recursion on left child
        printPostorder(root.left)
         #now recursion on right child
        printPostorder(root.right)
        #print the data of node
        print(root.value,end = ' ')
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("\nPreorder:")
printPreorder(root)
print()
print("\nInorder:")
printInorder(root)
print()
print("\nPostorder:")
printPostorder(root)
print()
