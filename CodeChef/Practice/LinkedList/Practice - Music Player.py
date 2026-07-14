class Node:
    def __init__(self, songId):
        self.songId = songId
        self.prev = None
        self.next = None

class MusicPlayer:
    def __init__(self):
        self.head = None
        self.currentSong = None

    # Function to add a song to the end of the list
    def addSong(self, songId):
        new_node=Node(songId)
        
        if self.head is None:
            self.head=new_node
            self.currentSong=new_node
            return
        else:
            iter=self.head
            while iter.next:
                iter=iter.next
            new_node.prev=iter
            iter.next=new_node
            return
           

    # Function to play the next song
    def playNext(self):
            self.currentSong=self.currentSong.next
            

    # Function to play the previous song
    def playPrev(self):
        self.currentSong=self.currentSong.prev
        

    # Function to switch to a specific song
    def switchSong(self, songId):
        iter=self.head
        while iter:
            if iter.songId==songId:
                self.currentSong=iter
                return
            iter=iter.next
            

    # Function to return the songId of the current song playing
    def current(self):
        return self.currentSong.songId

# Main function to test the music player
if __name__ == "__main__":
    player = MusicPlayer()
    queries = int(input())
    while queries > 0:
        line = input().split()
        query = int(line[0])

        if query == 1:
            songId = int(line[1])
            player.addSong(songId)
        elif query == 2:
            player.playNext()
        elif query == 3:
            player.playPrev()
        elif query == 4:
            songId = int(line[1])
            player.switchSong(songId)
        elif query == 5:
            print(player.current())
        else:
            print("Invalid query!")
        queries -= 1
