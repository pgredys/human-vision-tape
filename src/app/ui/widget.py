import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Human Segmentation")
        self.load_images_button.clicked.connect(self.load_images_from_camera)

    def load_images_from_camera(self):
        image_path = "test_images.jpeg"
        print(image_path)
        scene = QGraphicsScene()

        scene.addPixmap(QPixmap(image_path).scaledToWidth(1000))
        self.graphicsView.setScene(scene)
