# Detailed Code Explanation: Custom PyQt5 Title Bar

This document provides a comprehensive explanation of the custom PyQt5 title bar implementation. We'll break down the code into its main components and explain their functionality.

## Table of Contents

1. [Import Statements](#import-statements)
2. [CustomTitleBar Class](#customtitlebar-class)
3. [MainWindow Class](#mainwindow-class)
4. [Main Execution](#main-execution)

## Import Statements

```python
import sys
from typing import Optional, Tuple
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                             QMenu, QAction, QVBoxLayout, QMenuBar, QHBoxLayout,
                             QPushButton)
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QColor, QPalette, QPixmap, QIcon, QMouseEvent, QCursor
```

These import statements bring in the necessary modules and classes from PyQt5 and the Python standard library. The `typing` module is used for type hinting, which improves code readability and helps with static type checking.

## CustomTitleBar Class

The `CustomTitleBar` class is a custom widget that replaces the default window title bar.

### Initialization

```python
class CustomTitleBar(QWidget):
    def __init__(self, parent: QMainWindow) -> None:
        super().__init__(parent)
        # ... (initialization code)
```

The `__init__` method sets up the basic structure of the title bar. It defines stylesheets for various components and initializes the title bar's appearance.

### Setup Methods

The class includes several setup methods to organize the initialization of different components:

- `_setup_icon()`: Sets up the icon in the title bar.
- `_setup_title()`: Sets up the title label.
- `_setup_buttons()`: Creates and sets up the window control buttons (minimize, maximize, fullscreen, close).
- `_setup_layout()`: Arranges the components in the title bar using layouts.
- `_setup_menubar()`: Creates and sets up the menu bar within the title bar.

### Event Handling

The class includes methods to handle mouse events for dragging the window:

- `mousePressEvent(event: QMouseEvent)`: Captures the initial position when the mouse is pressed.
- `mouseMoveEvent(event: QMouseEvent)`: Handles the window dragging functionality.

### Window Control Methods

These methods control the window state:

- `closeParent()`: Closes the parent window.
- `showParentMinimized()`: Minimizes the parent window.
- `showParentMaximized()`: Toggles between maximized and normal window states.
- `showParentFullScreen()`: Toggles between fullscreen and normal window states.

## MainWindow Class

The `MainWindow` class is a custom `QMainWindow` that uses the `CustomTitleBar` and implements resizable edges.

### Initialization

```python
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # ... (initialization code)
```

The `__init__` method sets up the main window with a frameless hint and initializes the custom title bar.

### Event Handling

The class includes methods to handle mouse events for resizing the window:

- `mousePressEvent(event: QMouseEvent)`: Determines if a resize operation should begin.
- `mouseMoveEvent(event: QMouseEvent)`: Handles the resizing operation.
- `mouseReleaseEvent(event: QMouseEvent)`: Finalizes the resize operation.

### Helper Methods

- `_get_resize_direction(pos: QPoint)`: Determines the resize direction based on the mouse position.
- `_perform_resize(global_pos: QPoint)`: Performs the actual window resizing.
- `_update_cursor(pos: QPoint)`: Updates the cursor icon based on the resize direction.

## Main Execution

```python
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
```

This section creates an instance of `QApplication`, creates and shows the main window, and starts the event loop.

## Key Concepts

1. **Frameless Window**: The main window is created with the `Qt.FramelessWindowHint` flag, removing the default window frame and decorations.

2. **Custom Title Bar**: The `CustomTitleBar` class replaces the standard title bar, allowing for full customization of its appearance and behavior.

3. **Window Dragging**: The custom title bar implements window dragging functionality in its `mouseMoveEvent` method.

4. **Resizable Edges**: The `MyMainWindow` class implements resizable edges by handling mouse events and updating the window geometry.

5. **Stylesheets**: The code uses Qt stylesheets to customize the appearance of various widgets, including the menu bar and buttons.

6. **Event Handling**: Both classes make extensive use of Qt's event system to handle mouse interactions for dragging and resizing.

This implementation provides a high degree of customization for PyQt5 applications, allowing developers to create unique and branded user interfaces while maintaining standard window management functionality.

