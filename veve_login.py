from webhook import webhook
import os
from art import *
import http.cookies
import brotli
import cloudscraper
import json
from collections import OrderedDict
from loguru import logger
from requests_futures.sessions import FuturesSession
import re
from unicodedata import name
import requests
import json
import helheim
import asyncio
from pypresence import Presence
from datetime import datetime
from datetime import datetime
import time
from wsgiref import headers
import urllib3
import random
from crack_check import checkIfProcessRunning
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


def now_time_ms():
    return int(datetime.now().timestamp() * 1000)


with open("login_info.json") as f:
    data = json.load(f)
    email = data["info"]["email"]
    password_veve = data["info"]["password"]

with open("proxies.txt") as f:
    proxy = f.readlines()
    count =0 
    formated_proxies = []
    if proxy == []:
        formated_proxies= [{'https':""}]
    else:
        while len(proxy) -1 >= count:
            if proxy[count].count(":") == 3:
                host, port, username, password = proxy[count].split(":")
                proxy1 = f"{username}:{password}@{host}:{port}".replace("\n", "")
                formated_proxies.append({'https': f'http://{proxy1}/', 'http': f'http://{proxy1}/'})
            else:    
                formated_proxies.append({'https': f'http://{proxy}/', 'http': f'http://{proxy}/'})
            count = count + 1


helheim.auth('')

def injection(session, response):
    if helheim.isChallenge(session, response):
        response = helheim.solve(session, response, 3)
    return response


session = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'mobile': False,
        'platform': 'windows'
    },
    requestPostHook=injection,
    debug=False
)


async def veve_login():
    print("[" + str(datetime.now()) + "]" + " " + "|" + " " +
          FgYellow + "Logging Into VeVe Account..." + Reset)

    helheim.wokou(session)

    session.headers = OrderedDict([
        ('Content-Length', None),
        ('Pragma', 'no-cache'),
        ('Cache-Control', 'no-cache,no-store'),
        ('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'),
        ('Accept', 'application/json, text/plain, */*'),
        ('Accept-Encoding', 'gzip, deflate, br'),
        ('Accept-Language', 'en-us'),
        ('client-name', 'veve-app-ios'),
        ('client-model', 'iphone 7 plus'),
        ('client-version', '1.0.583'),
        ('client-brand', 'apple'),
        ('expires', '0'),
        ('client-installer', 'appstore'),
        ('client-manufacturer', 'apple'),
        ('client-id', 'd132a0f9-8724-4675-b97c-19d0da5ceabb'),
        ('x-kpsdk-v', 'i-1.6.0'),
    ])

    session.kasadaHooks = {
        'mobile.api.prod.veve.me': {
            'POST': [
                '/graphql',
                '/api/auth/*'
            ]
        }
    }
    try:
        session.proxies = formated_proxies[random.randrange(0,len(formated_proxies))]
    except:
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " " + "Proxy Banned, Rotating...  " + Reset)
        
        session.proxies = formated_proxies[random.randrange(0,len(formated_proxies))]


    session.get('https://mobile.api.prod.veve.me/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp')

    resp = session.post(
        'https://mobile.api.prod.veve.me/api/auth/totp/send',
        json={"email": email}

    )

    if resp.status_code != 200:
        print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Failed To Send OTP, Please Check If Email Is Correct" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Exiting In 10 Seconds" + Reset)
        time.sleep(10)
        exit()

    print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgCyan + "Please Enter One Time Password Sent To Email" + Reset)
    totp = input("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgCyan + "> " + Reset)
    try:
       session.proxies = formated_proxies[random.randrange(0,len(formated_proxies))]
    except:
       print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " " + "Proxy Banned, Rotating...  " + Reset)
       session.proxies = formated_proxies[random.randrange(0,len(formated_proxies))]



    resp = session.post("https://mobile.api.prod.veve.me/api/auth/login",
    headers={
        'content-type': 'application/json;charset=utf-8',
    },
        data='{"email":"'+email+'","password":"'+ password_veve+'","totp":"'+totp+'"}'
    )

    if resp.status_code != 201:
        print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Failed To Login To Account, Please Check If Credentials Are Correct" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Exiting In 10 Seconds" + Reset)
        time.sleep(10)
        exit()

    try:
        with open("cookies.txt", 'w') as f:
            cookie = resp.headers['set-cookie'].split(';')[0]
            f.writelines(cookie)
    except:
        print("[" + str(datetime.now()) + "]" + " " + "|" + " " +
                FgRed + "Failed To Write Cookies To cookies.txt" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" +
                " " + FgRed + "Exiting In 10 Seconds" + Reset)
        time.sleep(10)
        exit()

    print("[" + str(datetime.now()) + "]" + " " + "|" + " " +
            FgGreen + "Succesfully Logged Into Account" + Reset)

