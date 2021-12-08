from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem


class ImagePopupGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.__item = ''
        self.__corner = Qt.TopLeftCorner
        self.__initUi()

    def __initUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow | Qt.WindowStaysOnTopHint)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def setPopupImageItem(self, item: QGraphicsItem):
        self.__item = item
        p = self.__item.pixmap()
        width = p.width()+self.horizontalScrollBar().heightMM()
        height = p.height()+self.verticalScrollBar().widthMM()
        self.setFixedSize(width, height)

    def setCornerDirectionOfImageBasedOnCursor(self, corner):
        self.__corner = corner

    def showPopupImage(self):
        p = self.__item.pixmap()
        scene = QGraphicsScene()
        scene.addPixmap(p)
        self.setScene(scene)
        self.fitInView(self.__item, Qt.KeepAspectRatio)
        self.__setGeometryOfPopupImage()
        if self.isVisible():
            pass
        else:
            self.show()

    def movePopupImage(self):
        self.fitInView(self.__item, Qt.KeepAspectRatio)
        self.__setGeometryOfPopupImage()
        if self.isVisible():
            pass
        else:
            self.show()

    def __setGeometryOfPopupImage(self):
        geo = self.geometry()
        p = self.window().cursor().pos()
        p.setX(p.x() + 20)
        p.setY(p.y() + 20)
        if self.__corner == Qt.TopLeftCorner:
            geo.moveTopLeft(p)
        if self.__corner == Qt.TopRightCorner:
            geo.moveTopRight(p)
        elif self.__corner == Qt.BottomLeftCorner:
            geo.moveBottomLeft(p)
        elif self.__corner == Qt.BottomRightCorner:
            geo.moveBottomRight(p)
        self.setGeometry(geo)
