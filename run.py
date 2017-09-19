import time, ctypes
while 0:
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
    print("open")
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)
    print("close")
