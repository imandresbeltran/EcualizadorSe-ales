from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from DESIGN_FILES.trimmer import Ui_MainWindow as TrimmerUI
from FUNCTIONS.AudioPlayer import AudioPlayer
from pydub import AudioSegment
import os
import tempfile

class AudioTrimmer(QMainWindow):
    def __init__(self, file_path, duration_seconds):
        super(AudioTrimmer, self).__init__()
        self.ui = TrimmerUI()
        self.ui.setupUi(self)

        #Guardar la ruta del archivo y su respectiva duración

        self.file_path = file_path
        self.duration_seconds = duration_seconds
        self.audio = AudioSegment.from_file(self.file_path)
        self.editor_window = None

        self.ui.SegundosGrabacion_4.setText(self.file_name())
        self.ui.SegundosGrabacion_5.setText(f"{self.duration_seconds:.2f} segundos")

        self.ui.TiempoGrabacion_3.setMaximum(40)
        self.ui.TiempoGrabacion_3.setMinimum(10)
        self.ui.TiempoGrabacion_3.valueChanged.connect(self.update_trim_duration)


        self.ui.IniciarGrabacion_3.clicked.connect(self.recortar_y_guardar)
        self.ui.IniciarGrabacion_4.clicked.connect(self.recortar_y_cargar)

        self.trim_duration = self.duration_seconds

    def file_name(self):
        return os.path.basename(self.file_path)
    
    def update_trim_duration(self):
        self.trim_duration = self.ui.TiempoGrabacion_3.value()
        self.ui.SegundosGrabacion_3.setText(f"{self.trim_duration:.0f} sec")

    def recortar_audio(self):
        try:
            trimmed_audio = self.audio[:self.trim_duration * 1000]
            return trimmed_audio
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al recortar el audio: {str(e)}")
            return None
        
    def recortar_y_guardar(self):
        trimmed_audio = self.recortar_audio()

        if trimmed_audio:
            file_dialog = QFileDialog(self)
            file_path, _ = file_dialog.getSaveFileName(self, "Guardar archivo recortado", "", "Audio Files (*.mp3 *.wav)")

            if file_path:
                try:
                    ext = os.path.splitext(file_path)[1]
                    if ext == ".mp3":
                        trimmed_audio.export(file_path, format="mp3")
                    elif ext == ".wav":
                        trimmed_audio.export(file_path, format="wav")
                    else:
                        raise ValueError("Formato de archivo no soportado")
                    QMessageBox.information(self, "Guardado", f"Archivo recortado guardado exitosamente en: {file_path}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error al guardar el archivo: {str(e)}")


    def recortar_y_cargar(self):
            trimmed_audio = self.recortar_audio()

            if trimmed_audio:
                try:
                    temp_fd, temp_path = tempfile.mkstemp(suffix=".mp3")
                    os.close(temp_fd)

                    trimmed_audio.export(temp_path, format="mp3"
                                         )
                    QMessageBox.information(self, "Cargado", "Archivo recortado cargado correctamente en el sistema.")
                    #Reproducción se insertará en esta parte
                    self.open_editor_window(temp_path)
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error al cargar el archivo: {str(e)}")

    def open_editor_window(self, file_path):
        try:
            self.editor_window = AudioPlayer(file_path)
            self.editor_window.show()
            self.close()
        except Exception as e:
            print(f"Error al abrir el editor: {e}")
            QMessageBox.critical(self, "Error", f"Error al abrir el editor: {str(e)}")
        