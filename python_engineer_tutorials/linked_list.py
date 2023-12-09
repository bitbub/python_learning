class Node:
    """
    An object for storing a single node of a linked list.
    it stors two attributes - data and the link/pointer to the next node in the list.
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f"<Node data: {self.data}>"
    


class LinkedList:
    """
    Singly linked list.
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list. Takes O(n) time.
        """

        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next_node
        
        return count
    
    def add(self, data):
        """
        Adds new node containing new data at the head of the linked list. Takes O(1) time.
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def __repr__(self) -> str:
        """
        Return string representation of the linked list. Takes O(n) time.
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"Head: {current.data}")
            elif current.next_node is None:
                nodes.append(f"{current.data} :Tail")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node
        
        return '->'.join(nodes)