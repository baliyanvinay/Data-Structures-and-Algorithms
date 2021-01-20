# Implementation of Binary Tree :: 22-Aug-2020
class Node(object):
    def __init__(self, value): # a node in BT would have left and right child
        self.value=value
        self.left_child, self.right_child=None, None
      
        
class BinaryTree(object):
    def __init__(self):
        self.root=None

    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(value, self.root) # private insert function
    
    def _insert(self, value, curr_node):
        if value < curr_node.value:
            if curr_node.left_child is None:
                curr_node.left_child=Node(value)
            else:
                self._insert(value, curr_node.left_child)
        elif value > curr_node.value:
            if curr_node.right_child is None:
                curr_node.right_child=Node(value)
            else:
                self._insert(value, curr_node.right_child)
        else: # case where value is equal to the node
            print("Value already in Tree")
    
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
    
    def _print_tree(self, curr_node):
        if curr_node is not None:
            self._print_tree(curr_node.left_child)
            print(curr_node.value)
            self._print_tree(curr_node.right_child)
    
    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else: 
            return 0
    
    def _height(self, curr_node, curr_height):
        if curr_node is None: return curr_height
        left_height=self._height(curr_node.left_child, curr_height+1)
        right_height=self._height(curr_node.right_child, curr_height+1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
    
    def _search(self, value, curr_node):
        if value==curr_node.value:
            return True
        elif value<curr_node.value and curr_node.left_child is not None:
            return self._search(value, curr_node.left_child)
        elif value>curr_node.value and curr_node.right_child is not None:
            return self._search(value, curr_node.right_child)
        return False


def fill_tree(tree, num_elems=20, max_int=100):
    from random import randint
    for _ in range(num_elems):
        cur_elem=randint(0,max_int)
        tree.insert(cur_elem)
    return tree

tree=BinaryTree()
tree=fill_tree(tree)
tree.print_tree()
print(f'Tree Height {tree.height()}')
tree.insert(292)
print(tree.search(292))
