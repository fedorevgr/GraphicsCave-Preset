from typing import TYPE_CHECKING

from abc import ABC

if TYPE_CHECKING:
    from src.view.Base import BaseView
    from src.model.Model import Model


class BaseController(ABC):
    view: 'BaseView'
    model: 'Model'

    def __init__(self, view: 'BaseView', model: 'Model'):
        self.view = view
        self.model = model
