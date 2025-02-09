from PySide6.QtWidgets import QMainWindow, QGraphicsView, QSizePolicy, QWidget, QVBoxLayout, QPushButton, QHBoxLayout


class UiMainWindow(object):
    _WINDOW_START_SIZE = (1200, 800)
    _RESIZEABLE = False

    mainWidget: QWidget
    graphicsView: QGraphicsView
    _buttonSpace: QWidget
    _buttons: dict[str: QPushButton]

    def __init__(self):
        super().__init__()
        self._buttons = {}

    def setupUi(self, widget: QMainWindow) -> None:
        widget.resize(self._WINDOW_START_SIZE[0], self._WINDOW_START_SIZE[1])

        centralWidget = QWidget(widget)
        verticalLayout = QVBoxLayout(centralWidget)

        self.graphicsView = QGraphicsView(centralWidget)
        verticalLayout.addWidget(self.graphicsView)

        self._buttonSpace = QWidget(centralWidget)
        verticalLayout.addWidget(self._buttonSpace)

        horizontalLayout = QHBoxLayout(self._buttonSpace)
        self._buttons["Button 1"] = QPushButton("Button 1", self._buttonSpace)
        horizontalLayout.addWidget(self._buttons["Button 1"])

        self._buttons["Button 2"] = QPushButton("Button 2", self._buttonSpace)
        horizontalLayout.addWidget(self._buttons["Button 2"])

        widget.setCentralWidget(centralWidget)

    def getButtons(self):
        return self._buttons





