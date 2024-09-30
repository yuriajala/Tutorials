# hello.py

"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication([])

# 3. Create the app GUI
window = QWidget()
window.setWindowTitle("PyQt tutorial App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, world!</h1>", parent=window)
helloMsg.move(60,15)

# 4. Show the app GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())
