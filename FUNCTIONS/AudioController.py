import pygame

class AudioController:
    def __init__(self, file_path):
        pygame.mixer.init()
        self.file_path = file_path
        self.audio_length = pygame.mixer.Sound(file_path).get_length()
        self.current_position = 0
        self.is_playing = False
        self.is_paused = False

    def load_audio(self):
        pygame.mixer.music.load(self.file_path)

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
        self.current_position = min(self.audio_length, self.current_position + seconds)
        self.seek_audio(self.current_position)

    def adjust_volume(self, volume):
        pygame.mixer.music.set_volume(volume / 100)

    def get_current_position(self):
        return pygame.mixer.music.get_pos() / 1000
    
    def get_audio_length(self):
        return self.audio_length