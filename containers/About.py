from PyQt5 import QtWidgets, QtCore

class AboutDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Timetable DBMS")
        self.setFixedSize(600, 400)
        
        layout = QtWidgets.QVBoxLayout()
        
        # Title
        title = QtWidgets.QLabel("Timetable Management System")
        title.setStyleSheet("font-size: 18pt; font-weight: bold;")
        layout.addWidget(title)
        
        # Project Info
        info_text = """
        <h3>Project Team:</h3>
        <ul>
        <li>PAVAN S - Development Lead & UI Design</li>
        <li>SAIDEV - Backend Development</li>
        <li>AKHILESH - Database Design</li>
        </ul>
        
        <h3>Documentation & Research:</h3>
        <ul>
        <li>PARTHA</li>
        </ul>
        
        <h3>Technical Specifications:</h3>
        <ul>
        <li>Genetic Algorithm Implementation for Timetable Optimization</li>
        <li>PyQt5 for Modern User Interface</li>
        <li>SQLite Database for Data Management</li>
        <li>Custom Evaluation Matrix for Schedule Quality</li>
        <li>CSV Import/Export Functionality</li>
        <li>Dynamic Time Slot Management</li>
        </ul>
        
        <p>Project Completed: December 2024</p>
        <p>Developed at Sahyadri College of Engineering and Management</p>
        """
        
        info = QtWidgets.QLabel(info_text)
        info.setWordWrap(True)
        info.setOpenExternalLinks(True)
        layout.addWidget(info)
        
        # Close button
        btn_close = QtWidgets.QPushButton("Close")
        btn_close.clicked.connect(self.close)
        layout.addWidget(btn_close)
        
        self.setLayout(layout)
