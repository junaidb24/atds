#!/usr/bin/evn python3

"""
atds.py
Advanced topics data structures
"""

__author__ = "Junaid Bhatti"
__version__ = "2024-02-11"


class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None
        
    
    def peek(self):
        """makes sure theres an item to check, then checks the top item"""
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None
        
    def size(self):
        return len(self.items)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def __repr__(self):
        return str(self.items)
    

class Queue:
    def __init__(self):
        self.que = []

    def enqueue(self, item):
        self.que.append(item)

    def dequeue(self):
        return self.que.pop(0)
    
    def size(self):
        return len(self.que)
    
    def peek(self):
        """makes sure theres an item to check, then checks the top item"""
        if len(self.que) > 0:
            return self.que[0]
        else:
            return None

    
    def is_empty(self):
        if len(self.que) == 0:
            return True
        else:
            return False
    
    def __repr__(self):
        return str(self.que)
        

class Deque:
    def __init__(self):
        self.deque = []
    
    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if self.is_empty() == False:
            return self.deque.pop(0)
        else:
            return None

    def remove_rear(self):
        if self.is_empty() == False:
            return self.deque.pop()
        else:
            return None

    def size(self):
        return len(self.deque)

    def is_empty(self):
        if len(self.deque) == 0:
            return True
        else:
            return False
class Node:
    """Defines a node class
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data
    
    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next
    
    def __repr__(self):
        return "Node[data=" + str(self.data) + ",next=" + str(self.next) + "]"

class UnorderedList(object):
    """Defines an unordered (unsorted) list of nodes.
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, data):
        """Inserts a new node at the beginning of
        the list
        """
        temp_node = Node(data)
        temp_node.set_next(self.head)
        self.head = temp_node

    def length(self):
        """Identifies the length of the list by
        going through the entire list. Painful!
        """
        node_count = 0
        current = self.head
        while current != None:
            current = current.get_next()
            node_count += 1
        return node_count 

    def search(self, data):
        """Returns True if the data is on the list.
        """
        current = self.head
        found = False
        while current != None and not found: 
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, data):
        """Removes multiple occurrences of data on the list, 
        which requires going through the entire list until
        you hit the end, or nothing if the data isn't on the list.
        """
        current = self.head
        previous = None
        while current != None and self.head != None:    # Have to search entire list
            if current.get_data() == data:              # need to remove it
                if previous == None:                    # we're at the head
                    self.head = current.get_next()
                    current = current.get_next()
                else:
                    previous.set_next(current.get_next())
                    current = current.get_next()
            else:                                       # pass on through
                previous = current
                current = current.get_next()

    def append(self, data):
        """Appends an item to the end of the list
        """
        temp = Node(data) 
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(temp)

    def index(self, data):
        """Returns the index of the first occurence of the data
        in the list.
        """
        if self.head == None:
            return None
        current = self.head
        index = 0
        while current != None and current.get_data() != data:
            current = current.get_next()
            index += 1
        if current == None:
            return None
        else:
            return index

    def insert(self, position, data):
        """Inserts the piece of data at the indicated position.
        """
        temp = Node(data)
        index = 0
        current = self.head
        previous = None
        while index < position:
            previous = current
            current = current.get_next()
            index += 1
        if index == 0:
            temp.set_next(current)
            self.head = temp
        else:
            previous.set_next(temp)
            temp.set_next(current)
            
    def pop(self, index=-1):
        """Removes item at position index, or at the end of the list
        (-1) if no index is indicated.
        """
        if self.head == None:
            return None      # Can't pop from empty list
        if index == -1:
            current = self.head
            previous = None
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            result = current.get_data()
            previous.set_next(None)
            return result
        elif index == 0:
            current = self.head
            result = current.get_data()
            self.head = current.get_next()
            return result
        else:       # returning from middle of list?
            current = self.head
            previous = None
            position = 0
            while position < index:
                previous = current
                current = current.get_next()
                position += 1
            result = current.get_data()
            previous.set_next(current.get_next())
            return result

    def __repr__(self):
        """Creates a representation of the list suitable for printing, debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result
    
class UnorderedListStack(object):
    """Implements a Stack using the UnorderedList class.
    """
    def __init__(self):
        self.ul = UnorderedList()

    def push(self, item):
        """Pushes an item onto the top of the stack"""
        self.ul.add(item)

    def pop(self):
        """Removes the item at the top of the stack and
        returns it.
        """
        return self.ul.pop(0)
    
    def peek(self):
        """Examines the item at the top of the stack
        and returns that value. Awkward: we don't have
        a way to look at data at the beginning of an
        Unordered List!"""
        value = self.ul.pop(0)
        self.ul.add(value)
        return value

    def size(self):
        return self.ul.length()

    def is_empty(self):
        return self.ul.is_empty()
    
class HashTable(object):

    def __init__(self, size):
        """Create empty lists for the Map
        """
        self.keys = size * [None]
        self.data = size * [None]
        self.size = size


    def put(self, key, value):
        """Creates an entry in the hash table
        """
        hash_value = key % self.size  
        while self.keys[hash_value] != None and self.keys[hash_value] != key:
            hash_value += 1
        # We're at a position where we can place the value
        if self.keys[hash_value] == key: 
            self.data[hash_value] = value
        else:
            # linear probe
            self.keys[hash_value] = key
            self.data[hash_value] = value
    

    def get(self, key):
        hash_value = key % self.size
        while self.keys[hash_value] != None and self.keys[hash_value] != key:
            hash_value += 1
        if self.keys[hash_value] == key: 
            return self.data[hash_value]
        else:
            return None
    

    def __str__(self):
        return "Keys: " + str(self.keys) + "\n" + \
               "Values: " + str(self.data)
        


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left_child  = None
        self.right_child = None

    def get_root_val(self):
        return self.val

    def set_root_val(self, new_val):
        self.val = new_val

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child
    
    def insert_left(self, val):
        new_subtree = BinaryTree(val)
        new_subtree.left_child = self.left_child
        self.left_child = new_subtree

    def insert_right(self, val):
        new_subtree = BinaryTree(val)
        new_subtree.right_child = self.right_child
        self.right_child = new_subtree

    def __repr__(self):
        return "BinaryTree[key = " + str(self.val) + \
        ",left=" + str(self.left_child) + \
        ", right=" + str(self.right_child) + "]"

def main():
    # The program goes here
    pass

if __name__ == "__main__":
    main()