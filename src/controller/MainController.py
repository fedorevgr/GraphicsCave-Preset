from typing import TYPE_CHECKING

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
        ...

    def clear(self) -> None:
        ...

    def unloadImage(self) -> None:
        ...

    def loadImage(self) -> None:
        ...

