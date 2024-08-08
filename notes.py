
##########! Linked Lists !##########

import time


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  #? Singly linked list can only go forward to the next node
  #? Doubly linked list can go forward to the next node and backward to the previous node
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
      
  def delete(self, data):
    current = self.head #? beginning of the linked list
    previous = None #?previous node
    while current: #?there's a chance that the data we're looking for doesn't exist
      if current.data == data: #? check current data passed in
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
    
#? Measure time for linked list operations
def linked_list_operations():
  linked_list = SinglyLinkedList()
  linked_list.append("Main Street") # O(1) - constant time - adding to the end of the list; size doesn't matter
  linked_list.append("Broadway")
  linked_list.append("Park Avenue")
  linked_list.append("Elm Street")
  
  #? Start measuring time for deletion
  start_time_delete = time.time()
  linked_list.delete("Broadway") # if we know the head and tail data, we can delete in O(1) time -> best case ; O(n) -> average case - dependant on size
  end_time_delete = time.time()
  delete_time = end_time_delete - start_time_delete
  
  #? Start measuring time for traversal
  start_time_traversal = time.time()
  linked_list.traversal() # Looping through the entire lis - O(n) - dependant on size
  end_time_traversal = time.time()
  traversal_time = end_time_traversal - start_time_traversal
  
  return delete_time, traversal_time


#? Measure time for linked list operations
delete_time, traversal_time = linked_list_operations()
print(f"Time taken for deletion: {delete_time} seconds")
print(f"Time taken for traversal: {traversal_time} seconds")
  
  
# my_ll = SinglyLinkedList()

# my_ll.append("1")
# my_ll.append("2")
# my_ll.append("3")
# # my_ll.delete("2")
# my_ll.traversal()