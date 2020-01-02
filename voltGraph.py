from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout
import pyqtgraph as pg
import voltageEmulator
import subprocess

# Initialize Qt
voltGraph = QApplication([])
mainWindow = QWidget()
start = QPushButton('Start')
graph = pg.PlotWidget()

# Grid layout to manage display
layout = QGridLayout()
mainWindow.setLayout(layout)
layout.addWidget(start)
layout.addWidget(graph)

# Graph Loop
timePassed = 0.0
coordinates = []
while True:
    coordinates.append(voltageEmulator.emulate())

# Emulate voltage input
mainWindow.show()
voltGraph.exec_()
