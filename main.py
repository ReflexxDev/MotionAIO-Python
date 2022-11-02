from auth import check_license
from veve_sniper import get_comic
from loader import load_cookies
from loader import check_updates
from loader import load_proxies
from loader import load_credentials
from loader import load_settings
from loader import load_tasks
from crack_check import checkIfProcessRunning
from veve_login import *
from veve_sniper_collectable import get_collectable
from veve_comic_drop import get_latest_drop
import os
from art import *
import http.cookies
import brotli 
import re
from unicodedata import name
import requests
import json
import asyncio
import time
from datetime import datetime
from wsgiref import headers
from pypresence import Presence
import urllib3
from veve_comic_drop import get_latest_drop
from account_checker import veve_acc_checker
urllib3.disable_warnings()
from pypresence import Presence
import time
import sys
import psutil


version = "1.0.2.9"


client_id = '844908562069323817'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop
start_time=time.time()
RPC.update(state="Version 1.0.2.9", details="Sniping The Market",large_image="motion",start=start_time)

FgBlack = "\x1b[30m"
FgRed = "\x1b[31m"
FgGreen = "\x1b[32m"
FgYellow = "\x1b[33m"
FgBlue = "\x1b[34m"
FgMagenta = "\x1b[35m"
FgCyan = "\x1b[36m"
FgWhite = "\x1b[37m"
Reset = "\x1b[0m"


def now_time_ms():
    return int(datetime.now().timestamp() * 1000)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


async def landing():
    clearConsole()
    tprint("MotionAIO")
    
    await checkIfProcessRunning()
    await load_settings()
    await checkIfProcessRunning()

    with open('settings.json') as f:
        data = json.load(f)
        key = data['info']['key']
        
    check_license(key)
    await load_credentials()
    await load_proxies()
    await load_cookies()
    await menu()


async def menu():
    print("")
    
    print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "Please Select A Module Below: " + Reset)
    print("[" + str(datetime.now()) + "]" + " " + "|" + " " + "[" + FgCyan + "1" + Reset + "]" + " Veve Minter" + Reset)
    print("[" + str(datetime.now()) + "]" + " " + "|" + " " + "[" + FgCyan + "2" + Reset + "]" + " Veve Market Sniper" + Reset)
    print("[" + str(datetime.now()) + "]" + " " + "|" + " " + "[" + FgCyan + "3" + Reset + "]" + " Veve Account Checker" + Reset)
    print("[" + str(datetime.now()) + "]" + " " + "|" + " " + "[" + FgCyan + "4" + Reset + "]" + " Veve Account Gen(Coming Soon)" + Reset)
    module_input = input("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgCyan + "> " + Reset)

    while module_input == "":
        module_input = input("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgCyan + "> " + Reset)

    if module_input == "1":
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "Enter The Category Of The Drop " + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" + " " + "[" + FgCyan + "1" + Reset + "]" + " Digital Comics" + Reset)
        category_input = input("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgCyan + "> " + Reset)

        if category_input == "1":
              await get_latest_drop()

    if module_input == "2":
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "Enter The Category To Snipe " + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" + " " + "[" + FgCyan + "1" + Reset + "]" + " Collectibles" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" + " " + "[" + FgCyan + "2" + Reset + "]" + " Digital Comics" + Reset)
        module_input = input("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgCyan + "> " + Reset)

        while module_input == "":
            module_input = input(
                "[" + str(datetime.now()) + "]" + " " + "|" + " " + "> " + Reset)

        if module_input == '1':
            print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "Enter The Name Of The Collectible " + Reset)
            name = input("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "> " + Reset)
            print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "Enter The Rarity " + Reset)
            rarity = input("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "> " + Reset)
            await get_collectable(name, rarity, '', 0)

        if module_input == '2':    
            print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "Enter The Name Of The Comic " + Reset)
            name = input("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "> " + Reset)
            print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "Enter The Eddition Number Without # " + Reset)
            issue = input("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "> " + Reset)
            print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "Enter The Rarity " + Reset)
            rarity = input("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " " + "> " + Reset)
            await get_comic(name, issue, rarity)
    
    if module_input == "3":
        await veve_acc_checker()
        await menu()
    if module_input == "4":
        print("soon")
        time.sleep(2)
        await menu()
    


asyncio.run(landing())
