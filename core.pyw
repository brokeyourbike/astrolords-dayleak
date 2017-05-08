#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import math
import codecs
import locale
import astro
from contextlib import redirect_stdout
from PyQt4 import QtCore, QtGui, uic

"""
@author: Ivan Stasiuk
@contact: brokeyourbike.com
Copyright (C) 2017
"""

__author__ = 'Ivan Stasiuk'
__version__ = '0.1'
__email__ = 'brokeyourbike@gmail.com'
__contact__ = 'www.brokeyourbike.com'


class Main_Window(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)

		uic.loadUi("data/Main.ui", self)
		self.setWindowIcon(QtGui.QIcon("data/rocket.png"))
		love = QtGui.QPixmap("data/love_8px.png")
		astro_logo = QtGui.QPixmap("data/logo.png")
		self.love_label.setPixmap(love)
		self.logo_label.setPixmap(astro_logo)
		self.broky_label.setOpenExternalLinks(True)

		self.connect(self.button_open, QtCore.SIGNAL("clicked()"),
			self.connect_astro)

		self.connect(self.button_go, QtCore.SIGNAL("clicked()"),
			self.run_algo)

		self.connect(self.button_x2, QtCore.SIGNAL("clicked()"),
			self.set_x2)

		self.connect(self.button_x5, QtCore.SIGNAL("clicked()"),
			self.set_x5)

	def connect_astro(self):
		if astro.run():
			self.button_open.setEnabled(False)
			self.button_open.setText('Подключено')
			self.button_go.setEnabled(True)
			self.button_go.setText('Запуск алгоритма')

	def set_x5(self):
		self.button_x5.setEnabled(False)
		self.button_x2.setEnabled(True)
		astro.cords = astro.x5_cords

	def set_x2(self):
		self.button_x5.setEnabled(True)
		self.button_x2.setEnabled(False)
		astro.cords = astro.x2_cords

	def run_algo(self):
		if not astro.run():
					self.button_open.setEnabled(True)
					self.button_open.setText('Подключить игру')
					self.button_go.setEnabled(False)
					self.button_go.setText('Ожидаю ..')
		else:
			fl = astro.core(astro.run())


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	app.setQuitOnLastWindowClosed(True)  # Запрещаем автоматический выход при закрытии последнего окна
	window = Main_Window()
	window.show()
	sys.exit(app.exec_())
