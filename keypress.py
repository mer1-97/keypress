#!python3
#-*- coding: utf-8 -*-

"""
자동 키보드 입력 모듈
"""

import ctypes
from time import sleep

# 변수 설정
USER32 = ctypes.windll.user32

KEY = {
    # 숫자
    "0": 0x30,  "1": 0x31,  "2": 0x32,  "3": 0x33,  "4": 0x34,   
    "5": 0x35,  "6": 0x36,  "7": 0x37,  "8": 0x38,  "9": 0x39,

    # 알파벳
    "a": 0x41,    "b": 0x42,    "c": 0x43,    "d": 0x44,    "e": 0x45,
    "f": 0x46,    "g": 0x47,    "h": 0x48,    "i": 0x49,    "j": 0x4A,
    "k": 0x4B,    "l": 0x4C,    "m": 0x4D,    "n": 0x4E,    "o": 0x4F,
    "p": 0x50,    "q": 0x51,    "r": 0x52,    "s": 0x53,    "t": 0x54,
    "u": 0x55,    "v": 0x56,    "w": 0x57,    "x": 0x58,    "y": 0x59,  "z": 0x5A,

    # 특수문자
    ";": 0xBA,    "=": 0xBB,    ",": 0xBC,    "-": 0xBD,    ".": 0xBE,
    "/": 0xBF,    "`": 0xC0,    "[": 0xDB,    "\\": 0xDC,    "]": 0xDD,
    "'": 0xDE,

    # 기능 키
    "f1": 0x70,    "f2": 0x71,    "f3": 0x72,    "f4": 0x73,
    "f5": 0x74,    "f6": 0x75,    "f7": 0x76,    "f8": 0x77,
    "f9": 0x78,    "f10": 0x79,    "f11": 0x7A,    "f12": 0x7B,

    # 제어 키
    "esc": 0x1B,  "window": 0x5B,
    "control": 0x11,    "alt": 0x12,  "kor_eng": 0x15,
    "print_screen": 0x2C,    "scroll_lock": 0x91,   "pause_break": 0x13,

    # 화살표 키
    "left_arrow": 0x25,    "right_arrow": 0x27,
    "up_arrow": 0x26,    "down_arrow": 0x28,

    # 탐색 키
    "insert": 0x2D,    "home": 0x24,    "page_up": 0x21,
    "delete": 0x2E,    "end": 0x23,     "page_down": 0x22,

    # 편집 키
    "backspace": 0x08,  "enter": 0x0D,  "shift": 0x10,
    "tab": 0x09,    "caps_lock": 0x14,  "spacebar": 0x20,
}

# 입력한 키의 키 코드를 반환
def key_search(key):
    global KEY

    key = str(key)
    if key.isupper:
        key = key.lower()
    find_key = KEY[key]

    return find_key

# 눌렀던 키를 떼는 함수
def key_up(key_input):
    try:
        key = key_search(key_input)
        USER32.keybd_event(key, 0, 0x02, 0)
        sleep(0.1)
    except KeyError:
        print("[!] {}는 이용할 수 없는 키입니다!".format(key_input))
        exit(1)

# 키를 누르는 함수
def key_down(key_input):
    try:
        key = key_search(key_input)
        USER32.keybd_event(key, 0, 0x00, 0)
        sleep(0.5)
    except KeyError:
        print("[!] {}는 이용할 수 없는 키입니다!".format(key_input))
        exit(1)

# 키를 눌렀다 떼는 함수
def key_press(key_input):
    key_down(key_input)
    sleep(0.3)
    key_up(key_input)

# 두 개의 키를 동시에 떼는 함수
def twice_key_up(first_key_input, second_key_input):
    try:
        f_key = key_search(first_key_input)
        s_key = key_search(second_key_input)
        USER32.keybd_event(f_key, 0, 0x02, 0)
        USER32.keybd_event(s_key, 0, 0x02, 0)
        sleep(0.1)
    except KeyError:
        print("[!] 이용할 수 없는 키입니다!")
        exit(1)    

# 두 개의 키를 동시에 누르는 함수
def twice_key_down(first_key_input, second_key_input):
    try:
        f_key = key_search(first_key_input)
        s_key = key_search(second_key_input)
        USER32.keybd_event(f_key, 0, 0x00, 0)
        USER32.keybd_event(s_key, 0, 0x00, 0)
        sleep(0.5)
    except KeyError:
        print("[!] 이용할 수 없는 키입니다!")
        exit(1)

# 복사 기능
def ctrl_c():
    twice_key_down('control','c')
    key_up('control')
    key_up('c')

# 붙여넣기 기능
def ctrl_v():
    twice_key_down('control','v')
    key_up('control')
    key_up('v')

# 모두 선택 기능
def ctrl_a():
    twice_key_down('control','a')
    key_up('control')
    key_up('a')

# 종료 기능
def alt_f4():
    twice_key_down('alt','f4')
    key_up('alt')
    key_up('f4')

# 화면 전환 기능
def alt_tab():
    twice_key_down('alt','tab')
    key_up('alt')
    key_up('tab')