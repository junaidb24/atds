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
        
