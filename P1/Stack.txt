#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:11:48 2019

@author: chunyangjia
"""

class Node:
    def __init__ (self, data = None, Next = None):
        
        self.data = data
        self.next = Next
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.Next
    
    def set_next(self,new_next):
        self.next = new_next

class Stack:
    def __init__(self, head = None):
        """initialize the Stack(Linkedlist) with a head Node"""
        self.head = head
        self.tail = head
    
    def push(self,data):
        """add to the very top of the linked list"""
        newNode = Node(data)
        
        if Stack is None:
            self.head = newNode
        elif Stack is not None:
            newNode.next = self.head
        self.head = newNode
    
    def pop(self):
        """remove the very first of the node"""
        if Stack is None:
            raise ValueError("nothing to pop, the stack is empty")
        else:
            secNode = self.head.next
            head = self.head
            self.head = secNode
            return head.data
    
    def peek(self):
        """has the same return behaviour as pop 
        but leaves the top item on the stack"""
        """peek the very first of the node"""
        if Stack is None:
            raise ValueError("nothing to peek, the stack is empty")
        else:
            return self.head.data
    
    def length(self):
        """to calculate the length of the LinkedList"""
        node = self.head
        n = 0
        while node is not None:
            n = n +1
            node = node.next
        return n 
        
    def __str__(self):
        """return a string representation of the string"""

        result = '[ '
        head = self.head
        while head is not None:
            result = result + str(head.data) + ' '
            head = head.next
        result += " ]"
        return result    
            
            
        
    
    