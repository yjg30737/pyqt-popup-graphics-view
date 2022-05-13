# pyqt-popup-graphics-view
PyQt Popup QGraphicsView (Image will pop up when move the mouse cursor inside the QGraphicsView, follow the cursor if you move it inside of the window)

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-popup-graphics-view`

## Example
Code Example
```python
from PyQt5.QtWidgets import QApplication
from pyqt_popup_graphics_view.popupGraphicsView import PopupGraphicsView


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    popupGraphicsView = PopupGraphicsView()
    popupGraphicsView.setFileName('nico_bellic.png')
    popupGraphicsView.show()
    app.exec_()
```

Result

![example](https://user-images.githubusercontent.com/55078043/145152674-baeb0b37-7e56-4185-92da-6d6d663ae829.png)

Note: Mouse cursor should've been top left of the image. Windows capture feature doesn't include the mouse cursor in the screenshot.
