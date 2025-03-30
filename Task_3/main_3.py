import sys
from PySide6.QtWidgets import QApplication
from task3 import Window


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())