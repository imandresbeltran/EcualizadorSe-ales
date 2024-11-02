import pygame
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

class AudioController:
    def __init__(self, file_path, equalizer):
        pygame.mixer.init()
        self.file_path = file_path
        self.audio_segment = AudioSegment.from_file(file_path)
        self.equalizer = equalizer
        self.current_position = 0
        self.is_playing = False
        self.is_paused = False

    def load_audio(self):
        self.apply_equalizer()
        pygame.mixer.music.load(self.get_audio_stream())

    def play_audio(self):
        if not self.is_paused:
            pygame.mixer.music.play(start=self.current_position)
        else:
            pygame.mixer.music.unpause()
        self.is_playing = True
        self.is_paused = False

    def pause_audio(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.current_position = pygame.mixer.music.get_pos() / 1000

    def stop_audio(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        self.current_position = 0

    def seek_audio(self, position):
        self.current_position = position
        self.load_audio()
        self.play_audio()

    def seek_backward(self, seconds=5):
        self.current_position = max(0, self.current_position - seconds)
        self.seek_audio(self.current_position)

    def seek_forward(self, seconds=5):
        self.current_position = min(len(self.audio_segment) / 1000, self.current_position + seconds)
        self.seek_audio(self.current_position)

    def adjust_volume(self, volume):
        pygame.mixer.music.set_volume(volume / 100)

    def get_current_position(self):
        return pygame.mixer.music.get_pos() / 1000
    
    def get_audio_length(self):
        return len(self.audio_segment) / 1000
    
    def apply_equalizer(self):
        self.audio_segment = self.equalizer.apply_equalizer(self.audio_segment)

    def get_audio_stream(self):
        audio_stream = BytesIO()
        self.audio_segment.export(audio_stream, format="wav")
        audio_stream.seek(0)
        return audio_stream
    
    