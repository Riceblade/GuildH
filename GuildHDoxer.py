import random
import string
from os import system
import time
from tqdm import tqdm
import ctypes
from time import sleep
import replit
import random
import sys
import pyfiglet
import geocoder
import colorama
from colorama import Fore, Back, Style
colorama.init()
ctypes.windll.kernel32.SetConsoleTitleW("SkyBlock Doxer")
print(f"{Fore.BLUE}")


trolldeo = pyfiglet.figlet_format("SkyBlock Doxer")
print(trolldeo)
print("")
time.sleep(0.5)
print("Follow instructions\n")
time.sleep(0.2)
print(f"{Fore.RED}")

uname = input('Username: ')


def choose_word():
    list_of_words = []
    with open('codes.txt') as f:
        line = f.readline().strip()
        while line:
            list_of_words.append(line)
            line = f.readline().strip()
    chosen_word = random.choice(list_of_words)
    print("Address:", chosen_word)
    time.sleep(3)
    print("==========================")


choose_word()

print("Age", random.randint(1, 28))
print("==========================")
time.sleep(3)

print("Username:", uname)
print("==========================")
time.sleep(3)


def choose_word():
    list_of_words = []
    with open('funny.txt') as f:
        line = f.readline().strip()
        while line:
            list_of_words.append(line)
            line = f.readline().strip()
    chosen_word = random.choice(list_of_words)
    print("PornHub Username: ", chosen_word)
    print("==========================")
    time.sleep(3)


choose_word()


def choose_word():
    list_of_words = []
    with open('yeah.txt') as f:
        line = f.readline().strip()
        while line:
            list_of_words.append(line)
            line = f.readline().strip()
    chosen_word = random.choice(list_of_words)
    print("Logged Into Computer, Password: ", chosen_word)
    print("==========================")
    time.sleep(3)


choose_word()


def choose_word():
    list_of_words = []
    with open('tokens.txt') as f:
        line = f.readline().strip()
        while line:
            list_of_words.append(line)
            line = f.readline().strip()
    chosen_word = random.choice(list_of_words)
    print("Discord Token: ", chosen_word)
    print("==========================")
    time.sleep(3)


choose_word()


def choose_word():
    list_of_words = []
    with open('virgin.txt') as f:
        line = f.readline().strip()
        while line:
            list_of_words.append(line)
            line = f.readline().strip()
    chosen_word = random.choice(list_of_words)
    print(f"Is {uname} a virgin? ", chosen_word)
    print("==========================")
    time.sleep(3)


ip = ".".join(map(str, (random.randint(0, 255)
                        for _ in range(4))))

print("Ip Address:", ip)
print("==========================")
time.sleep(3)


def choose_word():
    list_of_words = []
    with open('yesss.txt') as f:
        line = f.readline().strip()
        while line:
            list_of_words.append(line)
            line = f.readline().strip()
    chosen_word = random.choice(list_of_words)
    print("Name: ", chosen_word)
    print("==========================")
    time.sleep(3)


def choose_word():
    list_of_words = []
    with open('yesss.txt') as f:
        line = f.readline().strip()
        while line:
            list_of_words.append(line)
            line = f.readline().strip()
    chosen_word = random.choice(list_of_words)
    print("Mom's name: ", chosen_word)
    print("==========================")
    time.sleep(3)


choose_word()


def choose_word():
    list_of_words = []
    with open('yesss.txt') as f:
        line = f.readline().strip()
        while line:
            list_of_words.append(line)
            line = f.readline().strip()
    chosen_word = random.choice(list_of_words)
    print("Dad's name: ", chosen_word)
    print("==========================")
    time.sleep(3)


choose_word()

print("Weight: ", random.randint(80, 450), "pounds")
print("==========================")
time.sleep(3)


def choose_word():
    list_of_words = []
    with open('hights.txt') as f:
        line = f.readline().strip()
        while line:
            list_of_words.append(line)
            line = f.readline().strip()
    chosen_word = random.choice(list_of_words)
    print("Height: ", chosen_word)
    print("==========================")
    time.sleep(3)


choose_word()


def choose_word():
    list_of_words = []
    with open('grades.txt') as f:
        line = f.readline().strip()
        while line:
            list_of_words.append(line)
            line = f.readline().strip()
    chosen_word = random.choice(list_of_words)
    print("Grade Average: ", chosen_word)
    print("==========================")
    time.sleep(3)


choose_word()

g = geocoder.ip('me')
print("Current GPS Location: ", g.latlng)
print("==========================")
time.sleep(3)

swat_team = input("[?] Would you like to send pizza & swat teams [Y/N] ")
if swat_team in ('y', 'Y', 'Yes', 'yes', 'yEs', 'YES', 'YEs', 'yES', 'yeS'):
    print("Getting Swat Teams Ready!")
    time.sleep(3)
    num = input("amount of swat teams to send: ")
    pamnt = input("How many pizzas to send: ")
    print(f"{num} swat teams being sent")
    print(f"{pamnt} pizzas sent")
    string = f"\nSuccess!  {num} swat teams have been sent and {pamnt} pizzas have been ordered || Trolling Complete"

    for letter in string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
else:
    print("Beamed By Guild H")

for letter in string:
    sleep(0.01)
    sys.stdout.write(letter)
    sys.stdout.flush()

time.sleep(2)


time.sleep(2)

print(" ")
print(" ")
print("SkyBlock Doxer ending")
time.sleep(5)
print("Good Night")
