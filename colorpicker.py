import PySimpleGUI as sg
import pyautogui as pag
from clipboard import copy

# Recommended for Python 3.7 over 3.8 since pag.pixel tends to break on 3.8 for some reason
# if you encounter the reason for that, feel free to PR

try:
    pos = pag.position()
    R, G, B = pag.pixel(pos.x, pos.y)
    copy(f'#{R:02x}{G:02x}{B:02x}')
    print("Color copied", ":)")
except Exception as e:
    sg.SystemTray.notify("Whoops", str(e))
    print("Whoops", str(e))

