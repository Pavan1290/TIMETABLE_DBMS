from PyQt5 import QtWidgets, QtCore
from components import Database as db
from containers import Main
import sys

# Entry point for application
if __name__ == '__main__':
    if not db.checkSetup():
        db.setup()
    app = QtWidgets.QApplication(sys.argv)
    
    # Apply the stylesheet
    with open('style.qss', 'r') as f:
        style = f.read()
        app.setStyleSheet(style)
    
    # Enable High DPI scaling
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    
    parent = QtWidgets.QMainWindow()
    Main.MainWindow(parent)
    parent.show()
    sys.exit(app.exec_())
