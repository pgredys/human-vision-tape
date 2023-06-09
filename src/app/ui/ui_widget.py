# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1320, 765)
        Widget.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.graphicsView = QGraphicsView(Widget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setEnabled(True)

        self.verticalLayout.addWidget(self.graphicsView)

        self.line = QFrame(Widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.load_images_button = QPushButton(Widget)
        self.load_images_button.setObjectName(u"load_images_button")

        self.verticalLayout.addWidget(self.load_images_button)

        self.line_2 = QFrame(Widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.min_dist_slider = QSlider(Widget)
        self.min_dist_slider.setObjectName(u"min_dist_slider")
        self.min_dist_slider.setMaximum(100)
        self.min_dist_slider.setSingleStep(5)
        self.min_dist_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.min_dist_slider)

        self.min_dist_value_label = QLabel(Widget)
        self.min_dist_value_label.setObjectName(u"min_dist_value_label")

        self.horizontalLayout.addWidget(self.min_dist_value_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.max_dist_slider = QSlider(Widget)
        self.max_dist_slider.setObjectName(u"max_dist_slider")
        self.max_dist_slider.setMaximum(100)
        self.max_dist_slider.setSingleStep(5)
        self.max_dist_slider.setValue(100)
        self.max_dist_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.max_dist_slider)

        self.max_dist_value_label = QLabel(Widget)
        self.max_dist_value_label.setObjectName(u"max_dist_value_label")

        self.horizontalLayout_2.addWidget(self.max_dist_value_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_3 = QFrame(Widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.save_button = QPushButton(Widget)
        self.save_button.setObjectName(u"save_button")

        self.verticalLayout.addWidget(self.save_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.load_images_button.setText(QCoreApplication.translate("Widget", u"load Image", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Min distance from camera", None))
        self.min_dist_value_label.setText(QCoreApplication.translate("Widget", u"0 m", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Max distance from camera", None))
        self.max_dist_value_label.setText(QCoreApplication.translate("Widget", u"10m", None))
        self.save_button.setText(QCoreApplication.translate("Widget", u"Save images", None))
    # retranslateUi

