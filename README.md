# Custom PyQt5 Title Bar

This project demonstrates how to create a custom title bar for a PyQt5 application. It includes a custom `QMainWindow` with a frameless window hint and a custom title bar widget that replaces the default window decorations.

## Features

- Custom title bar with icon, title, and window control buttons (minimize, maximize, fullscreen, close)
- Customizable menu bar integrated into the title bar
- Resizable window edges
- Draggable window from the title bar

## Requirements

- Python 3.6+
- PyQt5

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/custom-pyqt5-titlebar.git
   cd custom-pyqt5-titlebar
   ```

2. Install the required dependencies:
   ```
   pip install PyQt5
   ```

## Usage

To run the example application:

```
python custom_titlebar.py
```

To use the custom title bar in your own PyQt5 application:

1. Copy the `CustomTitleBar` and `MyMainWindow` classes from `custom_titlebar.py` into your project.
2. Customize the title bar appearance and functionality as needed.

Example:

```python
from custom_titlebar import MyMainWindow
from PyQt5.QtWidgets import QApplication
import sys

class MyApplication(MyMainWindow):
    def __init__(self):
        super().__init__()
        # Add your application-specific setup here

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyApplication()
    main_window.show()
    sys.exit(app.exec())
```

## Customization

You can customize the appearance of the title bar by modifying the following in the `CustomTitleBar` class:

- `custom_menubar_stylesheet`: Style for the menu bar
- `custom_menu_stylesheet`: Style for the menu items
- `custom_pushbutton_stylesheet`: Style for the window control buttons

To change the icon, replace `'splash_python.png'` with your own icon file in the `_setup_icon` method.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- PyQt5 documentation and community for providing the foundation for this project.

