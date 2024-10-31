import sounddevice as sd
import wavio
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import QTimer
from pydub import AudioSegment
import os

class AudioRecorder:
    def __init__(self, parent):
        self.parent = parent
        self.fs = 44100
        self.recording_data = None
        self.timer = QTimer(self.parent)
        self.timer.timeout.connect(self.stop_recording)
        self.format_selected = "WAV"

    def start_recording(self, duration_seconds, format_selected):
        try:
            print(f"Inician la grabación por {duration_seconds} segundos en formato {format_selected}.")
            self.recording_data = sd.rec(int(duration_seconds * self.fs), samplerate=self.fs, channels=2)
            self.format_selected = format_selected
            self.timer.start(duration_seconds * 1000)
            QMessageBox.information(self.parent, "Grabación", f"Grabación iniciada por {duration_seconds} segundos.")
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Error al iniciar la grabación: {str(e)}")


    def stop_recording(self):
        try:
            if self.recording_data is not None:
                sd.stop()
                self.timer.stop()
                print("Grabación detenida.")
                self.save_recording()
            else:
                QMessageBox.warning(self.parent, "Grabación", "No se detecta una grabación activa para detener.")
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Error al detener la grabación: {str(e)}")

    def save_recording(self):
        options = QFileDialog.Options()

        try:
            if self.format_selected.lower() == 'mp3':
                file_filter = "Audio Files (*.mp3);;All Files (*)"
            else:
                file_filter = "Audio Files (*.wav);;All Files (*)"

            file_path, _ = QFileDialog.getSaveFileName(self.parent, "Guardar archivo de grabación", "", file_filter, options=options)

            if file_path:
                wav_file_path = file_path if self.format_selected.lower() == 'wav' else file_path.replace(".mp3", ".wav")
                wavio.write(wav_file_path, self.recording_data, self.fs, sampwidth=2)
                print(f"Archivo guardado en: {wav_file_path}")

                if self.format_selected.lower() == 'mp3':
                    self.convert_to_mp3(wav_file_path, file_path)
                    try:
                        os.remove(wav_file_path)
                    except OSError as e:
                        print(f"Erro al eliminar el archivo temporal WAV: {e}")
                        QMessageBox.warning(self.parent, "Advertencia", f"Error al eliminar archivo temporal WAV: {str(e)}")
                QMessageBox.information(self.parent, "Guardado", f"Grabación guardada en: {file_path}")
            else:
                print("No se ha guardado la grabación.")
                QMessageBox.warning(self.parent, "Cancelado", "No se ha guardado la grabación.")

        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Error al guardar la grabación: {str(e)}")

    def convert_to_mp3(self, wav_file_path, mp3_file_path):
        try:
            audio = AudioSegment.from_wav(wav_file_path)
            audio.export(mp3_file_path, format="mp3")
            print(f"Archivo convertido a MP3. {mp3_file_path}")
        except Exception as e:
            print(f"Error al convertir a MP3: {e}")
            QMessageBox.critical(self.parent, "Error", f"Error al convertir a MP3: {str(e)}")