# Problem Statement: You are tasked with implementing a singly linked list class in Python. The class should support basic operations such as insertion, deletion, and traversal.

#? Task 1: Implement the Node class to represent individual nodes in the linked list.
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#! Task 2: Implement the SinglyLinkedList class with methods for insertion, deletion, and traversal.
class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def insertion(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
      
  def deletion(self, data):
    current = self.head
    previous = None
    while current:
      if current.data == data:
        if previous:
          previous.next = current.next
        else:
          self.head = current.next
        if current.next is None:
          self.tail = previous
          return True
      previous = current
      current = current.next
    return False
  
  def __iter__(self):
    current = self.head
    while current:
      yield current.data
      current = current.next
  
  def traversal(self):
    print("Linked list elements:")
    for data in self:
      print(data, end=" -> ")
    print("None")

#* Task 3: Test the implemented functionality by performing various operations on the linked list.

linked_list = SinglyLinkedList()
linked_list.insertion("Jonathan")
linked_list.insertion("James")
linked_list.insertion("Lilly")
linked_list.insertion("Tim")

for data in linked_list:
  print(data)

linked_list.deletion("James")

linked_list.traversal()


# You are tasked with implementing a doubly linked list class in Python. The class should support operations such as insertion, deletion, and traversal.

#! Task 1: Implement the **Node** class to represent individual nodes in the doubly linked list.
class Node: 
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None 

#? Task 2: Implement the **DoublyLinkedList** class with methods for insertion, deletion, and traversal.
class DoublyLinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
    
  def insert_data(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
      
  def delete_data(self, data):
    current = self.head
    while current:
      if current.data == data:
        if current == self.head:
          self.head = current.next
        if current == self.tail:
          self.tail = current.prev
        if current.prev:
          current.prev.next = current.next
        if current.next:
          current.next.prev = current.prev
        return True
      current = current.next
    return False
  
  def __iter__(self):
    current = self.head
    while current:
      yield current.data
      current = current.next
  
  def traverse_data(self):
    if not self.head:
      print("Linked list is empty.")
      return
    current = self.head
    while current:
      print(f"Student: {current.data}")
      current = current.next

#* Task 3: Test the implemented functionality by performing various operations on the doubly linked list
doubly_linked_list = DoublyLinkedList()

doubly_linked_list.insert_data("Hattie")
doubly_linked_list.insert_data("Grace")
doubly_linked_list.insert_data("Joey")
doubly_linked_list.insert_data("Jack")

for data in doubly_linked_list:
  print(data)
  
doubly_linked_list.delete_data("Joey")

doubly_linked_list.traverse_data()
