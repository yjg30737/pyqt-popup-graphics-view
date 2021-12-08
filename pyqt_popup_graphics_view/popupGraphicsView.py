from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication

from pyqt_popup_graphics_view.imagePopupGraphicsView import ImagePopupGraphicsView


class PopupGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.__imagePopupGraphicsView = ImagePopupGraphicsView()
        self.__cursor_inside_flag = False
        self.__graphicItem = ''
        self.setMouseTracking(True)

    def setFileName(self, filename):
        p = QPixmap(filename)
        scene = QGraphicsScene()
        self.__graphicItem = scene.addPixmap(p)
        self.setScene(scene)
        self.fitInView(self.__graphicItem, Qt.KeepAspectRatio)
        self.__imagePopupGraphicsView.setPopupImageItem(self.__graphicItem)

    def enterEvent(self, e):
        if self.__graphicItem and self.__imagePopupGraphicsView.isHidden():
            self.__cursor_inside_flag = True
            self.__imagePopupGraphicsView.showPopupImage()
        return super().enterEvent(e)

    def mouseMoveEvent(self, e):
        if self.__cursor_inside_flag:
            self.__imagePopupGraphicsView.movePopupImage()
        return super().mouseMoveEvent(e)

    def leaveEvent(self, e):
        if self.__imagePopupGraphicsView.isVisible():
            self.__imagePopupGraphicsView.close()
            self.__cursor_inside_flag = False
        return super().leaveEvent(e)

    def resizeEvent(self, e):
        if self.__graphicItem:
            self.fitInView(self.__graphicItem, Qt.KeepAspectRatio)
        return super().resizeEvent(e)


