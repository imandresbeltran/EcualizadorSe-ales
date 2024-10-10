from PySide6.QtWidgets import QFileDialog, QMessageBox
from pydub import AudioSegment
from FUNCTIONS.AudioTrimmer import AudioTrimmer

class AudioImporter:
    def __init__(self, parent):
        self.parent = parent
        self.trimmer_window = None

    def import_audio(self):
        #Seleccion un archivo de audio del explorador

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self.parent, "Seleccionar archivo de audio", "", "Audio Files (*.wav *.mp3);;All Files (*)", options=options)

        if file_path:
            return file_path
        else:
            return None
        
    
    def validate_audio_duration(self, file_path):
        try:
            audio = AudioSegment.from_file(file_path)

            duration_seconds = len(audio) / 1000

            if 10 <= duration_seconds <= 40:
                QMessageBox.information(self.parent, "Archivo válido", f"El archivo tiene una duración de {duration_seconds:.2f} segundos.")

                return True
            elif duration_seconds > 40:
                QMessageBox.warning(self.parent, "Duración excedida", "El archivo excede los 40 segundos, se abrirá la ventada de recorte.")
                self.open_trimmer_window(file_path, duration_seconds)
                return False
            else:
                QMessageBox.warning(self.parent, "Duración no válida", "El archivo seleccionado no tiene una duración entre 10 y 40 segundos.")
                return False
            
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Error al cargar el archivo: {str(e)}")
            return False
        
    def open_trimmer_window(self, file_path, duration_seconds):
        if not self.trimmer_window:
            self.trimmer_window = AudioTrimmer(file_path, duration_seconds)
        self.trimmer_window.show()