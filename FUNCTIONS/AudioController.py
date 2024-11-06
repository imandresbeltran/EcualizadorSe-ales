import pygame
from pydub import AudioSegment
from io import BytesIO
import numpy as np

class AudioController:
    def __init__(self, file_path, equalizer, sample_rate=44100, block_size=1024):
        pygame.mixer.init()
        self.file_path = file_path
        self.audio_segment = AudioSegment.from_file(file_path)
        self.equalizer = equalizer
        self.current_position = 0
        self.is_playing = False
        self.is_paused = False
        self.sample_rate = sample_rate
        self.block_size = block_size

    def load_audio(self):
        # Aplicamos el ecualizador y luego cargamos en pygame
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
        self.current_position = min(self.get_audio_length(), self.current_position + seconds)
        self.seek_audio(self.current_position)

    def adjust_volume(self, volume):
        pygame.mixer.music.set_volume(volume / 100)

    def get_current_position(self):
        return pygame.mixer.music.get_pos() / 1000

    def get_audio_length(self):
        return len(self.audio_segment) / 1000

    def apply_equalizer(self):
        # Obtener las muestras y aplicar el ecualizador
        samples = np.array(self.audio_segment.get_array_of_samples())

        # Verificar si el audio es estéreo o mono
        if self.audio_segment.channels == 2:
            # Si es estéreo, dividimos en canales y procesamos cada uno
            samples = samples.reshape((-1, 2))
            left_channel = self.equalizer.apply_equalizer(samples[:, 0])
            right_channel = self.equalizer.apply_equalizer(samples[:, 1])
            processed_samples = np.column_stack((left_channel, right_channel))
        else:
            # Si es mono, procesamos directamente
            processed_samples = self.equalizer.apply_equalizer(samples)

        # Convertir muestras a un array de bytes para AudioSegment
        processed_samples = processed_samples.astype(np.int16).flatten()
        self.audio_segment = self.audio_segment._spawn(processed_samples.tobytes())

    def get_audio_stream(self):
        audio_stream = BytesIO()
        self.audio_segment.export(audio_stream, format="wav")
        audio_stream.seek(0)
        return audio_stream
