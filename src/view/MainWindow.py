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

        buttons["Button 1"].clicked.connect(lambda:print("aboba"))
        buttons["Button 2"].clicked.connect(lambda:print("aboba"))

    def render(self):
        ...
