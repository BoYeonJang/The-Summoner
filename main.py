# ⌃R 코드 새로고침

import sys
import os
import random
import textwrap
# 타이틀을 1초마다 띄우면서 완성시킨다.
from time import sleep

print("\033[33m")
print(" _____ _   _ _____   ____  _   _ __  __ __  __  ___  _   _ _____ ____   ")
sleep(0.5)
print("|_   _| | | | ____| / ___|| | | |  \/  |  \/  |/ _ \| \ | | ____|  _ \  ")
sleep(0.5)
print("  | | | |_| |  _|   \___ \| | | | |\/| | |\/| | | | |  \| |  _| | |_) | ")
sleep(0.5)
print("  | | |  _  | |___   ___) | |_| | |  | | |  | | |_| | |\  | |___|  _ <  ")
sleep(0.5)
print("  |_| |_| |_|_____| |____/ \___/|_|  |_|_|  |_|\___/|_| \_|_____|_| \_\ ")
print("\033[0m")
sleep(1)


class player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []


myPlayer = player()


# 타이틀 선택지
def title_screen_selections():
    option = input("> ")
    if option == "1":
        intro_screen()
    elif option == "2":
        help_menu()
    elif option == "3":
        sys.exit()
    while True:
        print("해당 번호 중에서 선택해주세요.")
        option = input("> ")
        if option == "1":
            intro_screen()
        elif option == "2":
            help_menu()
        elif option == "3":
            sys.exit()


# 타이틀 화면 선택지 # 불러오기는 제작 미정
def title_screen():
    print("--------------------")
    print("[1] 시작")
    print("[2] 진행 방법 및 제작자")
    print("[3] 종료")
    print("--------------------")
    title_screen_selections()


# 진행 방법 및 제작자
def help_menu():
    print("--------------------")
    print("제작자: 물병자라")
    print("버전: v0.1")
    print("수정일자: 2021.01.05")
    print("문의: waterbottlezara@gmail.com")
    print("--------------------")
    print("- 여러 직업을 조합하여 나라를 지켜내세요.")
    print("- 여러개의 선택지 중에서 해당하는 번호를 입력해주세요.")
    print("--------------------")
    title_screen_selections()


# 인트로 선택지
def intro_selections():
    intro_option = input("> ")
    if intro_option == "1":
        intro()
    elif intro_option == "2":
        setup_game()
    while True:
        print("해당 번호 중에서 선택해주세요.")
        intro_option = input("> ")
        if intro_option == "1":
            intro()
        elif intro_option == "2":
            setup_game()


# 인트로 화면 선택지
def intro_screen():
    print("--------------------")
    print("\033[33m" + "The Summoner-소환사-" + "\033[0m" "의 인트로를 보시겠습니까?")
    print("[1] 예. 보겠습니다.")
    print("[2] 아니요. 스킵하겠습니다.")
    print("--------------------")
    intro_selections()


# 인트로 화면
def intro():
    input("12월 31일.")
    input("제야의 종소리를 들으러 보신각에 수만 명의 인파가 모여들었다.")
    input("다가오는 새해를 향해 카운트 다운을 세었다.")
    input("5, 4, 3, 2, 1….")
    input("땡, 땡, 땡.")
    input("커다란 종소리와 함께 공중에 커다란 구멍이 생겨났고, 한 마리의 괴물이 튀어나왔다.")
    input("사람들은 놀라 도망치기 시작했고,")
    input("괴물은 손에 들고 있던 몽둥이로 여러 사람을 죽이며 도심 한복판에 자리를 잡았다.")
    input("후일 '보신각 재앙'이라고 불린 이 소식은 전 세계를 강타했고,")
    input("24시간이 채 지나지 않아 이 상황은 세계 곳곳에 동시다발적으로 일어났다.")
    input("")
    input("10일 후.")
    input("서울특별시 학동역 인근 원룸.")
    input("나는 암막 커튼을 열어젖히고 공중에 떠다니는 먼지를 손으로 휘저었다.")
    input("이윽고 냉장고를 열어 차가운 캔맥주를 하나 집어 마시고는")
    input("소파에 앉아 텔레비전을 켰다.")
    input("'보신각 재앙'에서 희생당한 고인의 유가족이 나오는 다큐멘터리를 보던 도중 머릿속에서 알 수 없는 음성이 들렸다.")
    input("[당신은 " + "\033[33m" + "한국의 소환사" + "\033[0m" + "로 선택되었습니다.]")
    input("[12시간 안에 서울 광화문에서 균열이 생성될 예정입니다.]")
    input("[파티를 꾸리시길 바랍니다.]")
    input("[남은 시간: 12:00:00]")
    input("[남은 시간: 11:59:59]")
    input("[남은 시간: 11:59:58]")
    input("…….")
    input("………….")
    input("……………….")
    input("소환사……?")
    input("--------------------")
    setup_game()


# 초기 설정 화면
def setup_game():
    # 이름 정하기
    question1 = "당신의 이름은 무엇입니까?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
    player_name = input("> ")
    myPlayer.name = player_name

    question2 = "이름이 " + "\033[33m" + player_name + "\033[0m" + "맞습니까?\n" \
                                                                "--------------------\n" \
                                                                "[1] 맞습니다.\n" \
                                                                "[2] 아닙니다. 다시 정하겠습니다.\n" \
                                                                "--------------------\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
    player_gender = input("> ")
    myPlayer.name = player_name
    if player_gender == "1":
        start_game()
    elif player_gender == "2":
        setup_game()
    while True:
        print("해당 번호 중에서 선택해주세요.")
        player_gender = input("> ")
        if player_gender == "1":
            start_game()
        elif player_gender == "2":
            setup_game()


title_screen()


def start_game():
    pass
