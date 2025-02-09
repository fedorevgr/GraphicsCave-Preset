from typing import TYPE_CHECKING, Protocol

from abc import ABC
from PySide6.QtWidgets import QWidget, QPushButton

if TYPE_CHECKING:
    from src.controller.Base import BaseController


class UI(Protocol):
    def getButtons(self):
        ...

    def setupUi(self, widget: QWidget) -> None:
        ...


class BaseView(ABC):
    controller: 'BaseController'
    widget: QWidget
    ui: UI

    def __init__(self, widget: QWidget, ui: UI):
        self.widget = widget
        self.ui = ui
        self.ui.setupUi(self.widget)

    def setController(self, controller: 'BaseController') -> None:
        self.controller = controller
