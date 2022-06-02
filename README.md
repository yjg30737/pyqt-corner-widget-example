# pyqt-corner-widget-example
PyQt example which shows widget at the bottom-right corner of window (using event/geometry,  no QGridLayout involved)

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install git+https://github.com/yjg30737/pyqt-corner-widget-example.git --upgrade`

## Example
```python
from PyQt5.QtWidgets import QApplication
from pyqt_corner_widget_example import MainWindow

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
```

Result

