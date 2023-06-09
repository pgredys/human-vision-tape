from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene, QFileDialog

from app.ui.camera_acquisition import *
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):

    def __init__(self):
        super().__init__()
        self.PIL_image = Image.new(mode="RGB", size=(1000,500), color='#00004c')
        self.setupUi(self)
        self.setWindowTitle("Human Segmentation")
        image = QPixmap.fromImage(ImageQt(self.PIL_image))
        scene = QGraphicsScene()
        scene.addPixmap(image)
        self.graphicsView.setScene(scene)
        self.min_dist_slider.valueChanged.connect(self.sliderChanged)
        self.max_dist_slider.valueChanged.connect(self.sliderChanged)
        self.load_images_button.clicked.connect(self.load_images_from_camera)
        self.save_button.clicked.connect(self.save_image)

    def sliderChanged(self):
        if self.min_dist_slider.value() > self.max_dist_slider.value():
            self.min_dist_slider.setValue(self.max_dist_slider.value())

        self.min_dist_value_label.setText(str(self.min_dist_slider.value() / 10) + " m")
        self.max_dist_value_label.setText(str(self.max_dist_slider.value() / 10) + " m")

    def load_images_from_camera(self):
        images_cv2 = distance_segmentation_from_515(self.min_dist_slider.value() / 10, self.max_dist_slider.value() / 10)
        rgb_image = cv2.cvtColor(images_cv2, cv2.COLOR_BGR2RGB)
        self.PIL_image = Image.fromarray(rgb_image).convert('RGB')
        image = QPixmap.fromImage(ImageQt(self.PIL_image))
        scene = QGraphicsScene()
        scene.addPixmap(image)
        self.graphicsView.setScene(scene)
        # print("image loaded")

    def save_image(self):
        file = QFileDialog.getSaveFileName(
            self,
            'Save File As',
            '',
            "ReStructuredText Files (*.png)"
        )
        self.PIL_image.save(file[0])


