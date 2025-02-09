from typing import TYPE_CHECKING, Protocol

from abc import ABC

from PySide6.QtCore import QSize
from PySide6.QtSensors import QGyroscope
from PySide6.QtWidgets import QWidget, QPushButton, QGraphicsScene, QGraphicsView

if TYPE_CHECKING:
    from src.controller.Base import BaseController


class UI(Protocol):
    graphicsView: QGraphicsView

    def getButtons(self) -> dict[str, QPushButton]:
        ...

    def setupUi(self, widget: QWidget) -> None:
        ...

    def getCanvasSize(self) -> QSize:
        ...


class BaseView(ABC):
    controller: 'BaseController'
    widget: QWidget
    ui: UI
    scene: QGraphicsScene

    def __init__(self, widget: QWidget, ui: UI):
        self.widget = widget
        self.ui = ui
        self.ui.setupUi(self.widget)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    def setController(self, controller: 'BaseController') -> None:
        self.controller = controller

    def getCanvasSize(self) -> QSize:
        return self.ui.getCanvasSize()
