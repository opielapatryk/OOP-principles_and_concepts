from abc import abstractmethod, ABC

class MediaFile(ABC):
    @abstractmethod
    def play(self):
        pass

class AudioFile(MediaFile):
    def __init__(self, title: str) -> None:
        self.title = title
    
    def play(self):
        print(f"Playing audio file {self.title}")

class VideoFile(MediaFile):
    def __init__(self, title: str) -> None:
        self.title = title
    
    def play(self):
        print(f"Playing video file {self.title}")

class PlaybackDevice(ABC):
    @abstractmethod
    def connect(self):
        pass

class Speaker(PlaybackDevice):
    def __init__(self):
        self.connected = False
    
    def connect(self):
        self.connected = True
        print("Speaker connected")

class Screen(PlaybackDevice):
    def __init__(self):
        self.connected = False
    
    def connect(self):
        self.connected = True
        print("Screen connected")

class MediaPlayer:
    def __init__(self,file: MediaFile, device: PlaybackDevice):
        self.file = file
        self.device = device
    
    def play_media(self):
        self.device.connect()
        self.file.play()


audio = AudioFile("Song.mp3")
video = VideoFile("Movie.mp4")
speaker = Speaker()
screen = Screen()

audio_player = MediaPlayer(audio, speaker)
video_player = MediaPlayer(video, screen)

audio_player.play_media()
video_player.play_media()