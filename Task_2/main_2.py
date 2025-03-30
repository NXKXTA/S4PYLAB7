import sys
from PySide6.QtWidgets import QApplication
from task2 import Window


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())