import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtCore import QTimer
import requests
import json

class InventoryUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Management")
        layout = QVBoxLayout()

        self.table = QTableWidget()
        layout.addWidget(self.table)

        # ... (Add buttons and line edits for purchase/return)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_inventory) # Update every X seconds
        self.timer.start(5000) # 5 seconds

        self.setLayout(layout)
        self.update_inventory()

    def update_inventory(self):
        try:
            response = requests.get("[http://127.0.0.1:5000/inventory](https://www.google.com/search?q=http://127.0.0.1:5000/inventory)") # New endpoint to get inventory
            if response.status_code == 200:
                inventory_data = response.json()
                # ... (Populate table with inventory data)
            else:
                QMessageBox.critical(self, "Error", f"Failed to get inventory: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Connection error: {e}")

    # ... (purchase/return functions - update database via server, then call update_inventory())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryUI()
    window.show()
    sys.exit(app.exec())
