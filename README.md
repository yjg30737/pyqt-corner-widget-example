# pyqt-corner-widget-example
PyQt example which shows widget at the bottom-right corner of window (using event/geometry, no QGridLayout involved)

This is just for example.

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

Normal

![image](https://user-images.githubusercontent.com/55078043/171563818-a3fcae10-128c-42b9-b182-a8e9f1c3b0f1.png)

Maximize

![image](https://user-images.githubusercontent.com/55078043/171563860-be8be3b9-03d1-4a4c-a78d-47fef1fd58b0.png)

After resize

![image](https://user-images.githubusercontent.com/55078043/171563885-59a07dcf-3848-44fc-a709-f70188709d4f.png)

## See Also
<a href="https://github.com/yjg30737/pyqt-show-button-when-hover-widget.git">pyqt-show-button-when-hover-widget</a> - In this case, i used `QGridLayout` to set button's position at bottom right.  



