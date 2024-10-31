import pygame
import os
import time
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QTimer
from DESIGN_FILES.player import Ui_MainWindow as PlayerUI
from FUNCTIONS.AudioSessionManager import AudioSessionManager

class AudioPlayer(QMainWindow):
    def __init__(self, file_path, parent=None):
        super(AudioPlayer, self).__init__(parent)
        self.ui = PlayerUI()
        self.ui.setupUi(self)

        #Pygame para la reproducción del audio
        pygame.mixer.init()

        self.audio_manager = AudioSessionManager()
        self.file_path = self.audio_manager.save_audio_copy(file_path)
        self.audio_length = 0
        self.current_position = 0
        self.is_playing = False
        self.is_paused = False

        self.ui.pushButton_Play.clicked.connect(self.play_audio)
        self.ui.pushButton_Pause.clicked.connect(self.pause_audio)
        self.ui.pushButton_Stop.clicked.connect(self.stop_audio)
        self.ui.pushButton_Seek_Backward.clicked.connect(self.seek_backward)
        self.ui.pushButton_Seek_Forward.clicked.connect(self.seek_forward)
        self.ui.ContadorTiempo_2.valueChanged.connect(self.adjust_volume)
        self.ui.ContadorTiempo.sliderMoved.connect(self.seek_audio)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_progress)

        self.load_audio(self.file_path)


    def load_audio(self, file_path):
        try:
            pygame.mixer.music.load(file_path)
            self.audio_length = pygame.mixer.Sound(file_path).get_length()
            self.ui.ContadorTiempo.setRange(0, int(self.audio_length))
            self.ui.Label_Start_2.setText(f"{self.format_time(self.audio_length)}")

            self.ui.ContadorTiempo_2.setValue(100)
            pygame.mixer.music.set_volume(1.0)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar el archivo de audio: {str(e)}")

    def play_audio(self):
        try:
            if not self.is_paused:
                pygame.mixer.music.load(self.file_path)
                pygame.mixer.music.play(start=self.current_position)
                self.timer.start()
            else:
                pygame.mixer.music.unpause()
                self.timer.start()
                
            self.is_playing = True
            self.is_paused = False

        except Exception as e:
            print(f"Error al reproducir el audio: {e}")

    def pause_audio(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.timer.stop()
            self.is_paused = True
            self.current_position = pygame.mixer.music.get_pos() / 1000

    def stop_audio(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        self.timer.stop()
        self.ui.ContadorTiempo.setValue(0)
        self.current_position = 0

    def seek_audio(self, position):
        if self.is_playing or self.is_paused:
            pygame.mixer.music.stop()
            pygame.mixer.music.play(start=position)
            self.ui.ContadorTiempo.setValue(position)
            self.is_playing = True
            self.is_paused = False
            self.timer.start()

    def seek_backward(self):
        self.current_position = max(0, self.current_position - 5)
        self.load_and_play_from_current_position()

    def seek_forward(self):
        self.current_position = min(self.audio_length, self.current_position + 5)
        self.load_and_play_from_current_position()

    def load_and_play_from_current_position(self):
        try:
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play(start=self.current_position)
            self.is_playing = True
            self.is_paused = False
        except Exception as e:
            print(f"Error al ajustar la posición y reproducir el audio: {e}")

    def adjust_volume(self):
        volume = self.ui.ContadorTiempo_2.value() / 100
        pygame.mixer.music.set_volume(volume)

    def update_progress(self):
        current_position = pygame.mixer.music.get_pos() / 1000
        self.ui.ContadorTiempo.setValue(int(current_position))
        self.ui.Label_Start.setText(self.format_time(current_position))

        if int(current_position) >= int(self.audio_length):
            self.timer.stop()

    def closeEvent(self, event):
        self.audio_manager.clean_up()
        event.accept()

    
    @staticmethod
    def format_time(seconds):
        mins, secs = divmod(seconds, 60)
        return f"{int(mins):02}:{int(secs):02}"