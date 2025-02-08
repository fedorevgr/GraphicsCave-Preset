import sys

from PySide6.QtWidgets import QApplication
from src.view.MainWindow import MainWindowView


def main() -> None:
    app = QApplication(sys.argv)
    view = MainWindowView()
    window = view.widget
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
