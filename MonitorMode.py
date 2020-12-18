#!/bin/python3

import os
from colorama import Fore
print(Fore.CYAN)
print("🇲​​​​​  - 🇲​​​​​ 🇴​​​​​ 🇩​​​​​ 🇪​​​​​")
print("'See Everything'")
print()
print("Press [Y] to turn on monitor mode\nPress [N] to exit")

def menu():
    print()
    choice = input()

    if choice == 'Y':
        print()
        print(Fore.RED)
        print("Chose a WiFi connection below to set into Monitor Mode:")
        print()
        print(Fore.CYAN)
        device = os.system("iwconfig")
        print()
        print(Fore.RED)
        name = input("Enter Connection Name: ")
        check = os.system("sudo airmon-ng check")
        print()
        print("READY")
        print(Fore.YELLOW)
        monitor = os.system("sudo airmon-ng check kill")
        print()
        print("SET")
        print(Fore.GREEN)
        up = os.system(f"sudo airmon-ng start {name}")
        print()
        print("GO!")
        print()
        print(Fore.CYAN)
        print("Your card is now set to Monitor Mode!")

    if choice == 'N':
        exit()

menu()