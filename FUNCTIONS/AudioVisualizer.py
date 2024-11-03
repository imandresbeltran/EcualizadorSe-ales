import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QWidget, QVBoxLayout

class AudioVisualizer(QWidget):
    def __init__(self, parent=None):
        super(AudioVisualizer, self).__init__(parent)
        self.figure = Figure(figsize=(4.5,3.5))
        self.canvas = FigureCanvas(self.figure)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def plot_signal(self, signal, title="Audio Signal"):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(signal)
        ax.set_title(title)
        self.canvas.draw()