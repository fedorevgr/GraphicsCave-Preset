from dataclasses import dataclass

from PySide6.QtCore import QSize, QPoint
from PySide6.QtGui import QImage, QColor, QPainter, QBrush, QPen, QPolygon

STARTING_SIZE = (1200, 800)

@dataclass
class Model:
    _image: QImage

    def __init__(self) -> None:
        self._image = QImage(STARTING_SIZE[0], STARTING_SIZE[1], QImage.Format.Format_ARGB32)

    def reset(self):
        self._image.fill(QColor("transparent"))

    def setSize(self, dimensions: QSize):
        if dimensions.width() != STARTING_SIZE[0] or dimensions.height() != STARTING_SIZE[1]:
            self._image = QImage(dimensions, QImage.Format.Format_ARGB32)

    def draw(self, dimensions: QSize) -> None:
        self.setSize(dimensions)

        self.reset()

        painter = QPainter(self._image)
        brush = QBrush(QColor("red"))
        painter.setBrush(brush)
        pen = QPen(QColor("blue"))
        painter.setPen(pen)

        painter.drawPolygon(QPolygon([QPoint(0, 0), QPoint(100, 60), QPoint(60, 100)]))

    def getImage(self) -> QImage:
        return self._image
