# -*- coding: utf-8 -*-
#Application startup file
# Copyright (C) 2020 Hiroki Fujii <hfujii@hisystron.com>

import sys, os, winsound
#カレントディレクトリを設定
if hasattr(sys,"frozen"): os.chdir(os.path.dirname(sys.executable))
else: os.chdir(os.path.abspath(os.path.dirname(__file__)))

#エラーの出力
import traceback

def exchandler(type, exc, tb):
	msg=traceback.format_exception(type, exc, tb)
	print("".join(msg))
	f=open("errorLog.txt", "a")
	f.writelines(msg)
	f.close()
	if hasattr(sys, "frozen") == False:
		winsound.Beep(1500, 100)
		winsound.Beep(1500, 100)
		winsound.Beep(1500, 300)
	else:
		simpleDialog.winDialog("error", "An error has occured. Contact to the developer for further assistance.")
	sys.exit(-1)

sys.excepthook=exchandler


import multiprocessing
multiprocessing.freeze_support() #これがないとマルチプロセスでおかしなことになる

import win32timezone#ダミー
def _(string): pass#dummy

#dllを相対パスで指定した時のため、カレントディレクトリを変更
if sys.version_info.major>=3 and sys.version_info.minor>=8:
	os.add_dll_directory(os.getcwd())
	sys.path.append(os.getcwd())


import app as application
import constants
import globalVars
import m3uManager

def main():
	app=application.Main()
	globalVars.app=app
	app.initialize()
	app.MainLoop()


#global schope
if __name__ == "__main__": main()
