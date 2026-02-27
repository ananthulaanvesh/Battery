from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt
from core.calculations import calculate_pack


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Battery Builder v1.0")
        self.setMinimumWidth(700)

        # ---- INPUT SECTION ----
        input_layout = QVBoxLayout()

        self.cell_voltage_input = QLineEdit()
        self.cell_voltage_input.setPlaceholderText("Cell Voltage (V)")

        self.cell_capacity_input = QLineEdit()
        self.cell_capacity_input.setPlaceholderText("Cell Capacity (Ah)")

        self.series_input = QLineEdit()
        self.series_input.setPlaceholderText("Series Count (S)")

        self.parallel_input = QLineEdit()
        self.parallel_input.setPlaceholderText("Parallel Count (P)")

        self.calculate_button = QPushButton("Calculate Pack")
        self.calculate_button.clicked.connect(self.calculate)

        input_layout.addWidget(QLabel("Electrical Inputs"))
        input_layout.addWidget(self.cell_voltage_input)
        input_layout.addWidget(self.cell_capacity_input)
        input_layout.addWidget(self.series_input)
        input_layout.addWidget(self.parallel_input)
        input_layout.addWidget(self.calculate_button)

        input_frame = QFrame()
        input_frame.setLayout(input_layout)

        # ---- RESULT SECTION ----
        result_layout = QVBoxLayout()

        self.result_label = QLabel("Results will appear here")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        result_layout.addWidget(QLabel("Pack Results"))
        result_layout.addWidget(self.result_label)

        result_frame = QFrame()
        result_frame.setLayout(result_layout)

        # ---- MAIN LAYOUT ----
        main_layout = QHBoxLayout()
        main_layout.addWidget(input_frame)
        main_layout.addWidget(result_frame)

        self.setLayout(main_layout)

        self.apply_styles()

    def calculate(self):
        try:
            cell_voltage = float(self.cell_voltage_input.text())
            cell_capacity = float(self.cell_capacity_input.text())
            series = int(self.series_input.text())
            parallel = int(self.parallel_input.text())

            results = calculate_pack(
                cell_voltage, cell_capacity, series, parallel
            )

            self.result_label.setText(
                f"Voltage: {results['voltage']:.2f} V\n\n"
                f"Capacity: {results['capacity']:.2f} Ah\n\n"
                f"Energy: {results['energy']:.3f} kWh"
            )

        except ValueError:
            self.result_label.setText("Please enter valid numbers.")

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: #ffffff;
                font-size: 14px;
            }

            QLineEdit {
                background-color: #2c2c2c;
                border: 1px solid #444;
                padding: 6px;
                border-radius: 6px;
            }

            QPushButton {
                background-color: #0078d7;
                border: none;
                padding: 8px;
                border-radius: 6px;
            }

            QPushButton:hover {
                background-color: #005ea6;
            }

            QLabel {
                font-weight: 500;
            }
        """)