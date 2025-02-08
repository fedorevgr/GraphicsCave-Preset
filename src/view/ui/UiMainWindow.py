from PySide6.QtWidgets import QMainWindow, QGraphicsView, QSizePolicy, QWidget, QVBoxLayout, QPushButton, QHBoxLayout


class UiMainWindow(object):
    _WINDOW_START_SIZE = (1200, 800)
    _RESIZEABLE = False

    def __init__(self):
        super().__init__()

        self.mainWidget = None
        self.graphicsView = None
        self.buttonSpace = None
        self.button1 = None
        self.button2 = None

    def setupUi(self, widget: QMainWindow) -> None:
        widget.resize(self._WINDOW_START_SIZE[0], self._WINDOW_START_SIZE[1])

        centralWidget = QWidget(widget)
        verticalLayout = QVBoxLayout(centralWidget)

        self.graphicsView = QGraphicsView(centralWidget)
        verticalLayout.addWidget(self.graphicsView)

        self.buttonSpace = QWidget(centralWidget)
        verticalLayout.addWidget(self.buttonSpace)

        horizontalLayout = QHBoxLayout(self.buttonSpace)
        self.button1 = QPushButton("Button 1", self.buttonSpace)
        horizontalLayout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2", self.buttonSpace)
        horizontalLayout.addWidget(self.button2)

        widget.setCentralWidget(centralWidget)






