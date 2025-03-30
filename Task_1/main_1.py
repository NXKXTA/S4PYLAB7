import sys
from task1 import ChartWindow
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)
window = ChartWindow()
window.show()
sys.exit(app.exec())