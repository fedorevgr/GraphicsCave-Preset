import sys
import logging

from PySide6.QtWidgets import QApplication
from src.view.View import View

logger = logging.getLogger(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG)

def main() -> None:
    logger.info("App start")

    app = QApplication(sys.argv)
    view = View()
    window = view.widget
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
