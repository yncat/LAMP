# -*- coding: utf-8 -*-
#Application startup file


import simpleDialog, sys, os
simpleDialog.dialog("debug", str(os.getcwd()) + "\n" + "\n".join(sys.argv))
import sys
import traceback
def exchandler(type, exc, tb):
	msg=traceback.format_exception(type, exc, tb)
	print("".join(msg))
	f=open("errorLog.txt", "a")
	f.writelines(msg)
	f.close()

sys.excepthook=exchandler

import multiprocessing
import win32timezone#ダミー
def _(string): pass#dummy

#dllを相対パスで指定した時のため、カレントディレクトリを変更

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Python3.8対応
#dllやモジュールをカレントディレクトリから読み込むように設定

multiprocessing.freeze_support() #これがないとマルチプロセスでおかしなことになる

if sys.version_info.major>=3 and sys.version_info.minor>=8:
	os.add_dll_directory(os.path.dirname(os.path.abspath(__file__)))
	sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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
