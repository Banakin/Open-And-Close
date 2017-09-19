import time, ctypes
loop = 0
while loop == 0:
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
    print("open")
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)
    print("close")
