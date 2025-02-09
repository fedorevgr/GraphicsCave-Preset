from typing import TYPE_CHECKING

from logging import getLogger

from src.controller.Base import BaseController
from src.model.DataModel import DataModel

if TYPE_CHECKING:
    from src.view.MainWindow import MainWindowView

log = getLogger(__name__)

class MainController(BaseController):
    view: 'MainWindowView'
    model: DataModel

    def __init__(self, view: 'MainWindowView') -> None:
        super().__init__(view, DataModel())

    def render(self) -> None:
        log.debug(f"Canvas size {self.view.getCanvasSize()}")
        self.model.draw(self.view.getCanvasSize())
        self.view.render(self.model.getImage())

    def clear(self) -> None:
        log.info("Clearing canvas")
        self.view.clear()

    def unloadImage(self) -> None:
        ...

    def loadImage(self) -> None:
        ...

