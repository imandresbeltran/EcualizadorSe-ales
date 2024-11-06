import pygame
from PySide6.QtWidgets import QMainWindow, QMessageBox, QComboBox
from PySide6.QtCore import QTimer
from DESIGN_FILES.player import Ui_MainWindow as PlayerUI
from FUNCTIONS.AudioSessionManager import AudioSessionManager
from FUNCTIONS.AudioController import AudioController
from FUNCTIONS.Equalizer import Equalizer
from FUNCTIONS.AudioVisualizer import AudioVisualizer
import numpy as np

class AudioPlayer(QMainWindow):
    def __init__(self, file_path, parent=None):
        super(AudioPlayer, self).__init__(parent)
        self.ui = PlayerUI()
        self.ui.setupUi(self)

        self.audio_manager = AudioSessionManager()
        self.file_path = self.audio_manager.save_audio_copy(file_path)
        self.equalizer = Equalizer()
        self.audio_controller = AudioController(self.file_path, self.equalizer)
        self.original_visualizer = AudioVisualizer(self.ui.original_signal_widget)
        self.equalized_visualizer = AudioVisualizer(self.ui.equalized_signal_widget)

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

        self.load_audio()
        self.setup_equalizer()

    def load_audio(self):
        try:
            self.audio_controller.load_audio()
            self.ui.ContadorTiempo.setRange(0, int(self.audio_controller.get_audio_length()))
            self.ui.Label_Start_2.setText(f"{self.format_time(self.audio_controller.get_audio_length())}")
            self.ui.ContadorTiempo_2.setValue(100)
            self.audio_controller.adjust_volume(100)
            self.plot_original_signal()
            self.plot_equalized_signal()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar el archivo de audio: {str(e)}")

    def plot_original_signal(self):
        original_signal = np.array(self.audio_controller.audio_segment.get_array_of_samples())
        self.original_visualizer.plot_signal(original_signal, title="Original Signal")

    def plot_equalized_signal(self):
        # Extraer muestras, aplicar ecualización y obtener el resultado para graficar
        samples = np.array(self.audio_controller.audio_segment.get_array_of_samples())
        equalized_samples = self.audio_controller.equalizer.apply_equalizer(samples)
        self.equalized_visualizer.plot_signal(equalized_samples, title="Equalized Signal")

    def play_audio(self):
        try:
            self.audio_controller.play_audio()
            self.timer.start()
        except Exception as e:
            print(f"Error al reproducir el audio: {e}")

    def pause_audio(self):
        self.audio_controller.pause_audio()
        self.timer.stop()

    def stop_audio(self):
        self.audio_controller.stop_audio()
        self.timer.stop()
        self.ui.ContadorTiempo.setValue(0)

    def seek_audio(self, position):
        self.audio_controller.seek_audio(position)
        self.ui.ContadorTiempo.setValue(position)

    def seek_backward(self):
        self.audio_controller.seek_backward()
        self.ui.ContadorTiempo.setValue(int(self.audio_controller.get_current_position()))

    def seek_forward(self):
        self.audio_controller.seek_forward()
        self.ui.ContadorTiempo.setValue(int(self.audio_controller.get_current_position()))

    def adjust_volume(self):
        volume = self.ui.ContadorTiempo_2.value()
        self.audio_controller.adjust_volume(volume)

    def update_progress(self):
        current_position = self.audio_controller.get_current_position()
        self.ui.ContadorTiempo.setValue(int(current_position))
        self.ui.Label_Start.setText(self.format_time(current_position))

        if int(current_position) >= int(self.audio_controller.get_audio_length()):
            self.timer.stop()

    def closeEvent(self, event):
        self.audio_manager.clean_up()
        event.accept()

    def setup_equalizer(self):
        self.ui.comboBox = QComboBox(self)
        self.ui.comboBox.addItems(self.equalizer.modes.keys())
        self.ui.comboBox.currentTextChanged.connect(self.change_equalizer_mode)

    def change_equalizer_mode(self, mode):
        self.equalizer.set_mode(mode)
        self.audio_controller.apply_equalizer()
        self.plot_equalized_signal()
        if self.audio_controller.is_playing:
            self.audio_controller.load_audio()
            self.audio_controller.play_audio()

    @staticmethod
    def format_time(seconds):
        mins, secs = divmod(seconds, 60)
        return f"{int(mins):02}:{int(secs):02}"
