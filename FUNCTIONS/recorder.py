import sounddevice as sd
import wavio
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import QTimer

class AudioRecorder:
    def __init__(self, parent):
        self.parent = parent
        self.fs = 44100
        self.recording_data = None
        self.timer = QTimer(self.parent)
        self.timer.timeout.connect(self.stop_recording)

    def start_recording(self, duration_seconds, format_selected):
        print(f"Iniciando la grabación por {duration_seconds} segundos.")
        self.recording_data = sd.rec(int(duration_seconds * self.fs), samplerate=self.fs, channels=2)
        self.timer.start(duration_seconds * 1000)
        QMessageBox.information(self.parent, "Grabación", f"Grabación iniciada por {duration_seconds} segundos.")

    def stop_recording(self):
        sd.stop()
        self.timer.stop()
        print("Grabación detenida.")
        self.save_recording()

    def save_recording(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self.parent, "Guardar archivo de grabación", "","Audio Files (*.wav);;All Files (*)", options=options)

        if file_path:
            wavio.write(file_path, self.recording_data, self.fs, sampwidth=2)
            print(f"Archivo guardado en: {file_path}")
            QMessageBox.information(self.parent, "Guardado", f"Grabación guardada en: {file_path}")

        else:
            print("No se ha guardado la grabación.")
            QMessageBox.warning(self.parent, "Cancelado", "No se ha guardado la grabación.")