from PySide6.QtCore import QTimer, QUrl
from PySide6.QtMultimedia import QAudioRecorder, QAudioEncoderSettings
from PySide6.QtWidgets import QFileDialog, QMessageBox

class AudioRecorder:
    def __init__(self, parent):
        #Inicializando la grabadora del audio
        self.audio_recorder = QAudioRecorder(parent)
        self.timer = QTimer(parent)
        self.timer.timeout.connect(self.stop_recording)
        self.parent = parent

    def start_recording(self, duration_seconds, format_selected):
        # Configurando la grabadora de audio
        settings = QAudioEncoderSettings()
        if format_selected == ".MP3":
            settings.setCodec("audio/mpeg")
            file_extension = "mp3"
        elif format_selected == ".WAV":
            settings.setCodec("audio/pcm")
            file_extension = "wav"

        # Creando y configurando un archivo de salida temporal
        self.audio_recorder.setEncodingSettings(settings)
        self.audio_recorder.setOutputLocation(QUrl.fromLocalFile(f"grabacion_temporal.{file_extension}"))

        # Inciando la grabación
        self.audio_recorder.record()
        print(f"Iniciando grabación por {duration_seconds} segundos en formato {format_selected}.")

        self.timer.start(duration_seconds * 1000)

        QMessageBox.information(self.parent, "Grabación", f"La grabación ha comenzado. Duración: {duration_seconds}.")

    def stop_recording(self):
        #Deteniendo la grabación
        self.audio_recorder.stop()
        self.timer.stop()
        print("Grabación detenida")
        self.save_recording()

    def save_recording(self):
        # Opción para que el usuario seleccione la ruta del archivo grabado

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self.parent, "Guardar archivo de grabación", "","Audio Files (*.mp3 *.wav);;All Files (*)", options=options)

        if file_path:
            print(f"Archivo guardado en: {file_path}")
            QMessageBox.information(self.parent, "Guardado", f"Grabación guardada en: {file_path}")
        else:
            print("No se seleccionó ningún archivo.")
            QMessageBox.warning(self.parent, "Cancelado", "No se ha guardado la grabación.")