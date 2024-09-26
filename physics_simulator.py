"""
Physics Simulator - by: jGDarkness (jeremy.g.davenport@gmail.com)

github: https://github.com/jGDarkness/PhysicsSimulator

A hobby project designed to test my software development skills and develop them, while at the same time teaching me more
about how the world and space work.
"""

from PyQt6 import (
    QtCore, 
    QtGui, 
    QtWidgets
)
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QPushButton, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel, 
    QLineEdit, 
    QMessageBox
)
import numpy as np
import scipy as sp
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("Physics Simulator - feature_implementation_1.0")
    window.setGeometry(100, 100, 800, 600)
    window.show()
    app.exec()