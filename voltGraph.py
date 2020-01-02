from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QToolBar, QToolButton
import pyqtgraph as pg
import voltageEmulator

# Define global variables/settings
emulator = True


def ui():
    # Initialize Qt
    app = QApplication([])

    # Initialize main window
    window = QWidget()
    window.setWindowTitle("voltGraph v0.0.1")
    layout = QGridLayout()
    window.setLayout(layout)

    # Initialize toolbar
    menu = QToolBar
    file = QToolButton()
    file.setText('File')
    edit = QToolButton()
    edit.setText('Edit')

    # Initialize buttons
    start = QPushButton('Start')
    stop = QPushButton('Stop')
    stop.setDisabled(True)
    save = QPushButton('Save')
    save.setDisabled(True)
    load = QPushButton('Load')

    # Initialize blank graph
    plot = pg.PlotWidget()

    # Grid layout to manage display
    layout.addWidget(start)
    layout.addWidget(stop)
    layout.addWidget(save)
    layout.addWidget(load)
    layout.addWidget(plot, 2, 2, 3, 3)

    # Show main UI
    window.show()
    app.exec_()


def graph():
    # Import emulator setting
    global emulator

    # Initialize the coordinates variable
    coordinates = []

    # If using emulator
    if emulator:
        while True:
            coordinates.append(voltageEmulator.emulate())


ui()
