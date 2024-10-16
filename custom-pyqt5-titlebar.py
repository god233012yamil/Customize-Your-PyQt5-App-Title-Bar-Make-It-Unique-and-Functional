import sys
from typing import Optional, Tuple
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                             QMenu, QAction, QVBoxLayout, QMenuBar, QHBoxLayout,
                             QPushButton)
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QColor, QPalette, QPixmap, QIcon, QMouseEvent, QCursor


class CustomTitleBar(QWidget):
    """
    A custom title bar widget for QMainWindow.

    This class creates a customized title bar with an icon, title, menu bar,
    and window control buttons (minimize, maximize, full screen, and close).
    """

    def __init__(self, parent: QMainWindow) -> None:
        """
        Initialize the CustomTitleBar.

        Args:
            parent (QMainWindow): The parent QMainWindow widget.
        """
        super().__init__(parent)

        # Stylesheet used to style the QMenuBar widget.
        custom_menubar_stylesheet = '''
        QMenuBar {
            background-color: rgb(100, 100, 100);
        }
        QMenuBar::item {
            background-color: transparent;
            color: white;
            padding: 4px 12px;
        }
        QMenuBar::item:selected {
            background-color: #5dade2;
            color: black;
        }
        '''
        # Stylesheet used to style the QMenu widget.
        custom_menu_stylesheet = '''
        QMenu {
            background-color: rgb(100, 100, 100);
            color: white;
        }
        QMenu::item:selected {
            background-color: #5dade2;
            color: white;
        }
        '''
        # Stylesheet used to style the QPushButton widget.
        custom_pushbutton_stylesheet = """
        QPushButton {
            background-color: transparent;
        }
        QPushButton:hover {
            background-color: #5dade2;
        }
        QPushButton:pressed {
            background-color: green;
        }
        """

        self.start: Optional[QPoint] = None

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Background, QColor(120, 120, 120))
        self.setPalette(palette)

        self.setFixedHeight(65)

        #
        self.icon = None
        self.title = None
        self.minimizeButton = None
        self.maximizeButton = None
        self.fullScreenButton = None
        self.closeButton = None
        self.menu_bar = None

        self._setup_icon()
        self._setup_title()
        self._setup_buttons(custom_pushbutton_stylesheet)
        self._setup_menubar(custom_menubar_stylesheet, custom_menu_stylesheet)
        self._setup_layout()

    def _setup_icon(self) -> None:
        """Set up the title bar icon."""
        self.icon = QLabel("", self)
        self.icon.setFixedHeight(25)
        pixmap = QPixmap('Images\\splash_python.png')
        scaled_pixmap = pixmap.scaledToHeight(self.icon.height(), Qt.SmoothTransformation)
        self.icon.setPixmap(scaled_pixmap)

    def _setup_title(self) -> None:
        """Set up the title bar title."""
        self.title = QLabel("Title", self)
        self.title.setStyleSheet("QLabel {font: Arial; font-size: 20px; color: white;}")
        self.title.move(0, 0)
        self.title.setFixedHeight(35)

    def _setup_buttons(self, button_style: str) -> None:
        """Set up the window control buttons."""
        self.closeButton = self._create_button('Images\\close-button-icon-white.png',
                                               self.closeParent,
                                               "Exit Application",
                                               button_style)
        self.maximizeButton = self._create_button('Images\\maximize-button-icon-white.png',
                                                  self.showParentMaximized,
                                                  "Maximize Application",
                                                  button_style)
        self.minimizeButton = self._create_button('Images\\minimize-button-icon-white.png',
                                                  self.showParentMinimized,
                                                  "Minimize Application",
                                                  button_style)
        self.fullScreenButton = self._create_button('Images\\fullscreen-button-icon-white.png',
                                                    self.showParentFullScreen,
                                                    "FullScreen Application",
                                                    button_style)

    def _create_button(self, icon_path: str, callback: callable, tooltip: str, button_style: str) -> QPushButton:
        """
        Create a window control button.

        Args:
            icon_path (str): Path to the button icon.
            callback (callable): Function to call when the button is clicked.
            tooltip (str): Tooltip text for the button.

        Returns:
            QPushButton: The created button.
        """
        button = QPushButton("")
        button.setIconSize(QSize(15, 15))
        button.setIcon(QIcon(icon_path))
        button.setStyleSheet(button_style)
        button.clicked.connect(callback)
        button.setToolTip(tooltip)
        return button

    def _setup_layout(self) -> None:
        """Set up the layout for the title bar."""
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 5, 0)
        horizontal_layout.addSpacing(5)
        horizontal_layout.addWidget(self.icon)
        horizontal_layout.addWidget(self.title)
        horizontal_layout.addStretch(1)
        horizontal_layout.addWidget(self.minimizeButton)
        horizontal_layout.addWidget(self.maximizeButton)
        horizontal_layout.addWidget(self.fullScreenButton)
        horizontal_layout.addWidget(self.closeButton)

        vertical_layout = QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addSpacing(0)
        vertical_layout.addWidget(self.menu_bar)
        vertical_layout.addStretch(1)

        self.setLayout(vertical_layout)

    def _setup_menubar(self, menubar_style: str, menu_style: str) -> None:
        """
        Set up the menu bar and its menus.

        Args:
            menubar_style (str): CSS stylesheet for the menu bar.
            menu_style (str): CSS stylesheet for the menus.
        """
        self.menu_bar = QMenuBar(self)
        self.menu_bar.setFixedHeight(25)
        self.menu_bar.setStyleSheet(menubar_style)

        self.menu_file = QMenu("&File", self)
        self.menu_file.setStyleSheet(menu_style)

        self.action_new = QAction("&New", self)
        self.action_new.setShortcut("Ctrl+N")
        self.action_new.setStatusTip("Create new ...")
        self.menu_file.addAction(self.action_new)

        self.action_quit = QAction("Exit", self)
        self.action_quit.setShortcut("Ctrl+Q")
        self.action_quit.setStatusTip("Exit application")
        self.action_quit.triggered.connect(self.closeParent)
        self.menu_file.addAction(self.action_quit)

        self.menu_bar.addMenu(self.menu_file)

        self.menu_help = QMenu("&Help", self)
        self.menu_help.setStyleSheet(menu_style)

        self.action_about = QAction("About", self)
        self.action_about.setShortcut("Ctrl+H")
        self.action_about.setStatusTip("Help about application")
        self.menu_help.addAction(self.action_about)

        self.menu_bar.addMenu(self.menu_help)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Handle mouse press events.

        Args:
            event (QMouseEvent): The mouse event.
        """
        self.start = event.globalPos()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Handle mouse move events for window dragging.

        Args:
            event (QMouseEvent): The mouse event.
        """
        if self.parent().isMaximized() or self.parent().isFullScreen():
            self.parent().showNormal()
            self.maximizeButton.setIcon(QIcon('maximize-button-icon-white.png'))
            self.fullScreenButton.setIcon(QIcon('fullscreen-button-icon-white.png'))

        delta = QPoint(event.globalPos() - self.start)
        self.parent().move(self.parent().x() + delta.x(), self.parent().y() + delta.y())
        self.start = event.globalPos()

    def closeParent(self) -> None:
        """Close the parent window."""
        self.parent().close()

    def showParentMinimized(self) -> None:
        """Minimize the parent window."""
        self.parent().showMinimized()

    def showParentMaximized(self) -> None:
        """Maximize or restore the parent window."""
        if self.parent().isMaximized():
            self.maximizeButton.setIcon(QIcon('maximize-button-icon-white.png'))
            self.fullScreenButton.setIcon(QIcon('fullscreen-button-icon-white.png'))
            self.parent().showNormal()
        else:
            self.maximizeButton.setIcon(QIcon('normal-button-icon-white.png'))
            self.parent().showMaximized()

    def showParentFullScreen(self) -> None:
        """Toggle full screen mode for the parent window."""
        if self.parent().isFullScreen():
            self.fullScreenButton.setIcon(QIcon('fullscreen-button-icon-white.png'))
            self.maximizeButton.setIcon(QIcon('maximize-button-icon-white.png'))
            self.parent().showNormal()
        else:
            self.fullScreenButton.setIcon(QIcon('end-fullscreen-button-icon-white.png'))
            self.parent().showFullScreen()


class MainWindow(QMainWindow):
    """
    Custom main window with a custom title bar and resizable edges.
    """

    def __init__(self) -> None:
        """Initialize the MyMainWindow."""
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)

        self._drag_pos: Optional[QPoint] = None
        self._resizing: bool = False
        self._edge_margin: int = 8
        self._resize_direction: Optional[str] = None

        self.customTitleBar = CustomTitleBar(self)
        self.setMenuWidget(self.customTitleBar)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.setMinimumSize(800, 600)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Handle mouse press events for resizing.

        Args:
            event (QMouseEvent): The mouse event.
        """
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos()
            self._resize_direction = self._get_resize_direction(event.pos())
            if self._resize_direction:
                self._resizing = True

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Handle mouse move events for resizing or updating cursor.

        Args:
            event (QMouseEvent): The mouse event.
        """
        if self._resizing and self._resize_direction:
            self._perform_resize(event.globalPos())
            self._update_cursor(event.pos())

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """
        Handle mouse release events.

        Args:
            event (QMouseEvent): The mouse event.
        """
        self._resizing = False
        self._resize_direction = None
        self.setCursor(Qt.ArrowCursor)

    def _get_resize_direction(self, pos: QPoint) -> Optional[str]:
        """
        Determine the resize direction based on cursor position.

        Args:
            pos (QPoint): The cursor position.

        Returns:
            Optional[str]: The resize direction or None.
        """
        rect = self.rect()
        near_left = pos.x() <= self._edge_margin
        near_right = pos.x() >= rect.width() - self._edge_margin
        near_top = pos.y() <= self._edge_margin
        near_bottom = pos.y() >= rect.height() - self._edge_margin

        if near_left and near_top:
            return "top-left"
        elif near_left and near_bottom:
            return "bottom-left"
        elif near_right and near_top:
            return "top-right"
        elif near_right and near_bottom:
            return "bottom-right"
        elif near_left:
            return "left"
        elif near_right:
            return "right"
        elif near_top:
            return "top"
        elif near_bottom:
            return "bottom"
        return None

    def _perform_resize(self, global_pos: QPoint) -> None:
        """
        Resize the window based on the direction of the resize.

        Args:
            global_pos (QPoint): The global cursor position.
        """
        delta = global_pos - self._drag_pos
        rect = self.geometry()

        if "right" in self._resize_direction:
            rect.setWidth(max(rect.width() + delta.x(), self.minimumWidth()))
        if "left" in self._resize_direction:
            rect.setLeft(rect.left() + delta.x())
        if "bottom" in self._resize_direction:
            rect.setHeight(max(rect.height() + delta.y(), self.minimumHeight()))
        if "top" in self._resize_direction:
            rect.setTop(rect.top() + delta.y())

        self.setGeometry(rect)
        self._drag_pos = global_pos

    def _update_cursor(self, pos: QPoint) -> None:
        """
        Update the cursor based on the position near edges.

        Args:
            pos (QPoint): The cursor position.
        """
        direction = self._get_resize_direction(pos)
        if direction in ["left", "right"]:
            self.setCursor(Qt.SizeHorCursor)
        elif direction in ["top", "bottom"]:
            self.setCursor(Qt.SizeVerCursor)
        elif direction in ["top-left", "bottom-right"]:
            self.setCursor(Qt.SizeFDiagCursor)
        elif direction in ["top-right", "bottom-left"]:
            self.setCursor(Qt.SizeBDiagCursor)
        else:
            self.setCursor(Qt.ArrowCursor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())