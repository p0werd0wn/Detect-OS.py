# coding: utf-8

import ui
from objc_util import *

UIDevice = ObjCClass('UIDevice')

def button_pressed(sender):
	
	vers = UIDevice.currentDevice().systemVersion()
	
	string = str(vers)
	
	v = sender.superview
	
	label = v['label1'].text = string


v = ui.load_view()
v.present('sheet')