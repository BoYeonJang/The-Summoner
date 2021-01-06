# ⌃R 코드 새로고침

import sys
import os
import random
import textwrap
# 타이틀을 1초마다 띄우면서 완성시킨다.
from time import sleep

print(" _____ _   _ _____   ____  _   _ __  __ __  __  ___  _   _ _____ ____   ")
sleep(0.5)
print("|_   _| | | | ____| / ___|| | | |  \/  |  \/  |/ _ \| \ | | ____|  _ \  ")
sleep(0.5)
print("  | | | |_| |  _|   \___ \| | | | |\/| | |\/| | | | |  \| |  _| | |_) | ")
sleep(0.5)
print("  | | |  _  | |___   ___) | |_| | |  | | |  | | |_| | |\  | |___|  _ <  ")
sleep(0.5)
print("  |_| |_| |_|_____| |____/ \___/|_|  |_|_|  |_|\___/|_| \_|_____|_| \_\ ")
sleep(1)


def title_screen_selections():
    option = input("> ")
    if option == "1":
        start_game()
    elif option == "2":
        help_menu()
    elif option == "3":
        sys.exit()
    while option not in ['1', '2', '3']:
        print("해당 번호 중에서 눌러주세요.")
        if option == "1":
            start_game()
        elif option == "2":
            help_menu()
        elif option == "3":
            sys.exit()


# 타이틀 화면 # 불러오기는 제작 미정
def title_screen():
    print("--------------------")
    print("[1] 시작하기")
    print("[2] 제작자보기")
    print("[3] 종료하기")
    input("--------------------")
    title_screen_selections()


def help_menu():
    print("--------------------")
    print("제작자: 물병자라")
    print("버전: v0.1")
    print("수정일자: 2021.01.05")
    print("문의: waterbottlezara@gmail.com")
    print("--------------------")
    title_screen_selections()






def intro():
    print("")

