from typing import TYPE_CHECKING

from abc import ABC

if TYPE_CHECKING:
    from src.view.Base import BaseView
    from src.model.DataModel import DataModel


class BaseController(ABC):
    view: 'BaseView'
    model: 'DataModel'

    def __init__(self, view: 'BaseView', model: 'DataModel'):
        self.view = view
        self.model = model
