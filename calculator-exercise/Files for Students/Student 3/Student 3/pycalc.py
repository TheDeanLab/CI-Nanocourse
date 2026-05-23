#!/usr/bin/env python3

# calc.py
# https://realpython.com/python-pyqt-gui-calculator/

""" Simple calculator built with Python and PyQt5 library """

import os
import sys

from .view import PyCalcUi
from .controller import PyCalcCtrl
from .model import evaluateExpression

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

__version__ = "0.1"
__author__ = "Tim Jones"

def main():
    """
    Main application entry point.

    This function serves as the entry point for the calculator application. It initializes the
    calculator GUI, creates instances of the model and controller, and starts the application's main loop.

    Args:
        None

    Returns:
        None
    """
    calc = QApplication(sys.argv)
    view = PyCalcUi()   # Render calculator GUI
    view.show()         # Display calculator GUI
    model = evaluateExpression          # Create instance of model
    PyCalcCtrl(model=model, view=view)  # Create instance of controller
    sys.exit(calc.exec_())    # Execute application main loop
    
if __name__ == "__main__":
    main()