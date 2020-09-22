﻿# -*- coding: utf-8 -*-
# sample dialog

import wx
import globalVars
import views.ViewCreator
from logging import getLogger
from views.baseDialog import *

class Dialog(BaseDialog):
	def Initialize(self, label, name):
		super().__init__("gaugeDialog")
		self.label=label
		self.log.debug("created")
		super().Initialize(self.app.hMainView.hFrame,name)
		self.InstallControls()
		return True

	def InstallControls(self):
		"""いろんなwidgetを設置する。"""
		self.creator=views.ViewCreator.ViewCreator(self.viewMode,self.panel,self.sizer,wx.VERTICAL,20)
		self.gauge,self.static=self.creator.gauge(self.label,x=400)

	# プログレス更新（現在値, ラベル, 最大値）
	def update(self, pos=None, label=None, max=None):
		if max != None:
			self.gauge.SetRange(max)
		if pos != None:
			self.gauge.SetValue(pos)
		if label != None:
			self.static.SetLabel(label)
