import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from DESIGN_FILES.main_window import Ui_MainWindow
from DESIGN_FILES.record_design import Ui_RecordOptions
from FUNCTIONS import recorder
from FUNCTIONS.recorder import AudioRecorder

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if hasattr(self.ui, 'menuGRABAR'):
            self.ui.menuGRABAR.aboutToShow.connect(self.abrir_grabacion)
        else:
            print("No menu 'GRABAR' found")

        self.record_window = None

    def abrir_grabacion(self):
        print("Abriendo grabacion")
        if not self.record_window:
            self.record_window = RecordOptions()
        self.record_window.show()
        self.hide()

class RecordOptions(QMainWindow):
    def __init__(self):
        super(RecordOptions, self).__init__()
        self.ui = Ui_RecordOptions()
        self.ui.setupUi(self)

        # Instanciando la clase Recorder para manejar la grabación

        self.recorder = recorder(self)

        # Conectando el botón de grabación con la función que comienza la misma
        self.ui.IniciarGrabacion.clicked.connect(self.iniciar_grabacion)

    def iniciar_grabacion(self):

        duration_seconds = self.ui.TiempoGrabacion.value()
        format_selected = self.ui.SeleccionFormatoGrabacion.currentText()

        self.recorder.start_recording(duration_seconds, format_selected)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
