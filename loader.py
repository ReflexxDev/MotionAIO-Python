from veve_login import veve_login
import os
from art import *
import http.cookies
import brotli
from loguru import logger
from requests_futures.sessions import FuturesSession
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
import urllib.request
urllib3.disable_warnings()


FgBlack = "\x1b[30m"
FgRed = "\x1b[31m"
FgGreen = "\x1b[32m"
FgYellow = "\x1b[33m"
FgBlue = "\x1b[34m"
FgMagenta = "\x1b[35m"
FgCyan = "\x1b[36m"
FgWhite = "\x1b[37m"
Reset = "\x1b[0m"


version = "1.0.2.2"
      

async def load_settings():
    with open("settings.json") as f:
        data = json.load(f)
        if data["info"]["key"] == "":
            print("[" + str(datetime.now()) + "]" + " " + "|" + " " +
                  FgRed + "Please Enter You Key In settings.json" + Reset)
            print("[" + str(datetime.now()) + "]" + " " + "|" +
                  " " + FgRed + "Exiting In 10 Seconds" + Reset)
            time.sleep(10)
            exit()

        elif data["info"]["webhook_url"] == "":
            print("[" + str(datetime.now()) + "]" + " " + "|" +
                  " " + FgRed + "Please Enter You Webhook In settings.json" + Reset)

            print("[" + str(datetime.now()) + "]" + " " + "|" +
                  " " + FgRed + "Exiting In 10 Seconds" + Reset)
            time.sleep(10)
            exit()

        else:
            lol = 1


async def load_credentials():
    f = open("login_info.json")
    data = json.load(f)

    if data["info"]["email"] == "":
        print("[" + str(datetime.now()) + "]" + " " + "|" + " " +
              FgRed + "Please Fill Out Email In login_info.json" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" +
              " " + FgRed + "Exiting In 10 Seconds" + Reset)
        time.sleep(10)
        exit()

    elif data["info"]["password"] == "":
        print("[" + str(datetime.now()) + "]" + " " + "|" + " " +
              FgRed + "Please Fill Out Password In login_info.json" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" +
              " " + FgRed + "Exiting In 10 Seconds" + Reset)
        time.sleep(10)
        exit()

    else:
        lol = 1


async def load_proxies():
    try:
        with open("proxies.txt") as f:
            if f.readline() == "":
                lol = 1
            else:
                lol = 1
    except:
        print("[" + str(datetime.now()) + "]" + " " + "|" + " " +
              FgRed + "Unable To Load Proxies From proxies.txt" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" +
              " " + FgRed + "Exiting In 10 Seconds" + Reset)
        time.sleep(10)
        exit()


async def load_cookies():
    with open("cookies.txt") as f:
        if f.readline() == "":
            await veve_login()



async def load_tasks():
    with open('tasks.csv') as f:
        if f.readlines() == "":
            print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "No Tasks Loaded in Tasks.csv" + Reset)
            print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Exiting In 10 Seconds" + Reset)
            time.sleep(10)
            exit()
        else:
            print(f.readlines())


async def check_updates():
    try:
        r = requests.get("")
        data = json.loads(r.content)

        if data[0]["version"] != version:
            print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgYellow + "Found A New Update, Downloading..." + Reset)

            r = requests.get("")
            data = json.loads(r.content)
            download_url = data[0]["link"]
            r = requests.get(download_url)
            file_name = download_url[::-1].split("/")[0][::-1]

            urllib.request.urlretrieve(download_url,'./'+ file_name)
            print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgGreen + "Succesfully Downloaded New Version, Please Delete Old .exe And Run The New One" + Reset)
            print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Exiting In 10 Seconds" + Reset)
            time.sleep(10)
            exit() 
        
    except:
        print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Unable To Check For Updates!" + Reset)            

