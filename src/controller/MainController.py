from typing import TYPE_CHECKING

from logging import log, DEBUG

from src.controller.Base import BaseController
from src.model.DataModel import DataModel

if TYPE_CHECKING:
    from src.view.MainWindow import MainWindowView


class MainController(BaseController):
    view: 'MainWindowView'
    model: DataModel

    def __init__(self, view: 'MainWindowView') -> None:
        super().__init__(view, DataModel())

    def render(self) -> None:
        log(DEBUG, self.view.getCanvasSize())
        self.model.draw(self.view.getCanvasSize())
        self.view.render(self.model.getImage())

    def clear(self) -> None:
        ...

    def unloadImage(self) -> None:
        ...

    def loadImage(self) -> None:
        ...

