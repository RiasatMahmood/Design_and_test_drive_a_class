class MusicTracker:

    def __init__(self):
        self.tracks = []

    
    def add(self, track):
        self.tracks.append(track)
        
    def show_tracks(self):
        return self.tracks