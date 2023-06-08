import os
import cv2
import numpy as np
from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene

from app.ui.camera_acquisition import *
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Human Segmentation")
        # self.start_button.clicked.connect(self.start_loading_images())
        self.min_dist_slider.valueChanged.connect(self.sliderChanged)
        self.max_dist_slider.valueChanged.connect(self.sliderChanged)
        self.load_images_button.clicked.connect(self.load_images_from_camera)

    def sliderChanged(self):
        print(self.sender().objectName() + " : " + str(self.sender().value()))
        print(self.min_dist_slider.value())
    def load_images_from_camera(self):
        images = distance_segmentation_from_515(self.min_dist_slider.value()/10, self.max_dist_slider.value()/10)
        rgb_image = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
        PIL_image = Image.fromarray(rgb_image).convert('RGB')
        image = QPixmap.fromImage(ImageQt(PIL_image))
        scene = QGraphicsScene()
        scene.addPixmap(image)
        self.graphicsView.setScene(scene)
        print("image loaded")