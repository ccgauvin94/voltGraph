from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout
import pyqtgraph as pg
import voltageEmulator
import time

##Initialize Qt
voltGraph = QApplication([])
mainWindow = QWidget()
start = QPushButton('Start')
graph = pg.PlotWidget()

#Grid layout to manage display
layout = QGridLayout()
mainWindow.setLayout(layout)
layout.addWidget(start, 0, 0)
layout.addWidget(graph, 0, 1, 3, 1)

#Graph Loop
timePassed = 0.0
coordinates = []
while True:
    readout = [timePassed, voltageEmulator.emulate()]
    timePassed = timePassed + 0.1
    coordinates.append(readout)
    time.sleep(0.1)


#Emulate voltage input
mainWindow.show()
voltGraph.exec_()

