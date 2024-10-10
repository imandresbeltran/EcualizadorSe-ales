import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from DESIGN_FILES.main_window import Ui_MainWindow
from DESIGN_FILES.record_design import Ui_RecordOptions
from FUNCTIONS.recorder import AudioRecorder
from FUNCTIONS.AudioImporter import AudioImporter
from FUNCTIONS.AudioTrimmer import AudioTrimmer


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if hasattr(self.ui, 'menuGRABAR'):
            self.ui.menuGRABAR.aboutToShow.connect(self.abrir_grabacion)
        else:
            print("No menu 'GRABAR' found")

        if hasattr(self.ui, 'actionIMPORTAR'):
            self.ui.actionIMPORTAR.triggered.connect(self.importar_archivo)

        else: 
            print("No action 'IMPORTAR' found")

        self.record_window = None
        self.AudioImporter = AudioImporter(self)

    def abrir_grabacion(self):
        print("Abriendo grabacion")
        if not self.record_window:
            self.record_window = RecordOptions()
        self.record_window.show()
        self.hide()


    def importar_archivo(self):
       file_path = self.AudioImporter.import_audio()

       if file_path:
           if self.AudioImporter.validate_audio_duration(file_path):
               print(f"Archivo {file_path} cargado y validad correctamente.")
           else:
               print(f"El archivo {file_path} no tiene una duración válida")
       else:
           print("No se ha seleccionado ningún archivo")
               

class RecordOptions(QMainWindow):
    def __init__(self):
        super(RecordOptions, self).__init__()
        self.ui = Ui_RecordOptions()
        self.ui.setupUi(self)

        # Instanciando la clase Recorder para manejar la grabación

        self.recorder = AudioRecorder(self)

        # Conectando el botón de grabación con la función que comienza la misma
        self.ui.IniciarGrabacion.clicked.connect(self.iniciar_grabacion)

    def iniciar_grabacion(self):

        duration_seconds = self.ui.TiempoGrabacion.value()
        format_selected = self.ui.SeleccionFormatoGrabacion.currentText().lower().replace(".", "")

        self.recorder.start_recording(duration_seconds, format_selected)

        if duration_seconds > 40:
            QMessageBox.warning(self, "Duración excedida", "La grabación excede los 40 segundos, se abrirá el recortador")
            self.open_trimmer_window(duration_seconds)

    def open_trimmer_window(self, duration_seconds):
        file_path = self.recorder.save_recording()
        if file_path:
            trimmer_window = AudioTrimmer(file_path, duration_seconds)
            trimmer_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
