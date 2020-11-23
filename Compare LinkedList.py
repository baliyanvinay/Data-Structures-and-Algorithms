class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
    
    def __str__(self):
        return_value=[]
        print_head=self.head
        while(print_head):
            return_value.append(print_head.data)
            print_head=print_head.next
        return f"{return_value}"
    
# Function to compare two linked list: Return 1 if they match and 0 if they don't    
def compare_lists(llist1, llist2):
    # if both are None
    if(llist1==None and llist2==None):
        return 1
    # if one is None meaning length of llist1 and llist2 differs
    if(llist1==None or llist2==None):
        return 0
    # if one node matches, recursive call to the function
    if(llist1.data==llist2.data):
        return CompareLists(llist1.next, llist2.next)
    else:
        return 0