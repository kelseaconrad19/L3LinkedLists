class Song: #? This is our data
  def __init__(self, title, artist, duration, genre):
    self.title = title
    self.artist = artist
    self.duration = duration
    self.genre = genre

class Node: #? Playing the role of our Node
  def __init__(self, song):
    self.song = song
    self.next = None
    self.prev = None  #* this is what makes this a doubly linked list
    
class PlaylistManager: #? Doubly linked list
  def __init__(self):
    self.head = None
    self.tail = None
  
  def add_song(self, title, artist, duration, genre):
    new_song = Song(title, artist, duration, genre)
    new_node = Node(new_song)
    if not self.head: #? If there are NOT any nodes in the list,
      #? our new_node is our first node. It is both the head and the tail because it's the only one.
      self.head = new_node
      self.tail = new_node
    else: #? If there ARE nodes in the list,
      #? We want to add the new node to the end of the list.
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
      
  def delete_song(self, title):
    current = self.head
    while current:
      if current.song.title == title:
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
  
  def traverse_playlist(self):
    if not self.head:
      print("Playlist is empty.")
      return
    current = self.head
    while current:
      print(f"Title: {current.song.title}")
      print(f"Artist: {current.song.artist}")
      print(f"Duration: {current.song.duration}")
      print(f"Genre: {current.song.genre}")
      print("----------------------------")
      current = current.next
      
########! Usage example !########
playlist_manager = PlaylistManager()

#* Add songs to the playlist
playlist_manager.add_song("Shape of You", "Ed Sheeran", 4.23, "Pop")
playlist_manager.add_song("Someone Like You", "Adele", 4.45, "Pop")
playlist_manager.add_song("Bohemian Rhapsody", "Queen", 5.55, "Rock")

#* Delete a song from the playlist
playlist_manager.delete_song("Someone Like You")

#* Traverse the playlist
playlist_manager.traverse_playlist()