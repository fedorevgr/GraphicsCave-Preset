from logging import log, DEBUG

from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QMainWindow
from src.controller.MainController import MainController
from src.view.ui.UiMainWindow import UiMainWindow
from src.view.Base import BaseView


class MainWindowView(BaseView):
    controller: MainController
    widget: QMainWindow

    def __init__(self) -> None:
        super().__init__(QMainWindow(), UiMainWindow())
        self.controller = MainController(self)
        self.__bind()

    def __bind(self):
        buttons = self.ui.getButtons()

        buttons["Button 1"].clicked.connect(self.controller.render)
        buttons["Button 2"].clicked.connect(self.controller.clear)

    def render(self, image: QImage) -> None:
        log(DEBUG, image)

        pixmap = QPixmap.fromImage(image)
        self.scene.addPixmap(pixmap)
        self.scene.update()

    def clear(self) -> None:
        self.scene.clear()
