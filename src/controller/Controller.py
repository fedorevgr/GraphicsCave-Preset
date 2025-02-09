from typing import TYPE_CHECKING

from logging import getLogger

from src.controller.Base import BaseController
from src.model.Model import Model

if TYPE_CHECKING:
    from src.view.View import View

log = getLogger(__name__)

class Controller(BaseController):
    view: 'View'
    model: Model

    def __init__(self, view: 'View') -> None:
        super().__init__(view, Model())

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

