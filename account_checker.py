from veve_login import veve_login
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


async def veve_acc_checker():
    print("[" + str(datetime.now()) + "]" + " " + "|" + " " +
          FgYellow + "Checking All Accounts In 'cookies.txt'" + Reset)

    helheim.wokou(session)

    session.headers = OrderedDict([
        ('Content-Length', None),
        ('Pragma', 'no-cache'),
        ('Cache-Control', 'no-cache,no-store'),
        ('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'),
        ('Accept', 'application/json, text/plain, */*'),
        ('Accept-Encoding', 'gzip, deflate'),
        ('Accept-Language', 'en-us'),
        ('client-name', 'veve-app-ios'),
        ('client-model', 'iphone 7 plus'),
        ('client-version', '1.0.584'),
        ('client-brand', 'apple'),
        ('expires', '0'),
        ('client-installer', 'appstore'),
        ('client-manufacturer', 'apple'),
        ('client-id', '93c6f3077fa7ca82'),
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

    with open("cookies.txt", 'r') as f:
        for i in f:
            time.sleep(0.3)
            url = "https://mobile.api.prod.veve.me/graphql"

            payload = json.dumps({
                "operationName": "MyInfo",
                "variables": {},
                "query": "query MyInfo {\n  me {\n    id\n    firstName\n    lastName\n    username\n    email\n    statuses\n    createdAt\n    dateOfBirth\n    __typename\n  }\n}\n"
            })
            headers= {
                'authority': 'mobile.api.prod.veve.me',
                'client-version': '1.0.583',
                'cookie': i.replace("\n", ""),
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                'client-operation': 'MarketListingsByComicType',
                'client-name': 'veve-app-ios',
                'client-model': 'iphone 7',
                'client-brand': 'apple',
                'client-user-id': '14a9a2dc-28cc-4228-8284-3e719ae8b4d8',
                'accept-language': 'en-gb',
                'x-kpsdk-v': 'i-1.6.0',
                'client-installer': 'appstore',
                'client-manufacturer': 'apple',
                'accept': '*/*',
                'content-type': 'application/json',
                'client-carrier': 'unknown',
                'client-id': 'd132a0f9-8724-4675-b97c-19d0da5ceabb',
                'if-none-match': 'W/"22-0vCKLKDr8cJbzINSDCdhUbjuZoY"'

            } 

            resp = session.request("POST", url, headers=headers, data=payload)
            data = json.loads(resp.content)
            try:
                if data['data']['me']['username'] != "":
                    username = data['data']['me']['username']

                    #gets gem ballance
                    resp = session.post("https://mobile.api.prod.veve.me/graphql", headers={
                        'authority': 'mobile.api.prod.veve.me',
                        'client-version': '1.0.583',
                        'cookie': i.replace("\n", ""),
                        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                        'client-operation': 'WalletBalanceQuery',
                        'client-name': 'veve-app-ios',
                        'client-model': 'iphone 7',
                        'client-brand': 'apple',
                        'client-user-id': '14a9a2dc-28cc-4228-8284-3e719ae8b4d8',
                        'accept-language': 'en-gb',
                        'x-kpsdk-v': 'i-1.6.0',
                        'client-installer': 'appstore',
                        'client-manufacturer': 'apple',
                        'accept': '*/*',
                        'content-type': 'application/json',
                        'client-carrier': 'unknown',
                        'client-id': 'd132a0f9-8724-4675-b97c-19d0da5ceabb',
                        'if-none-match': 'W/"22-0vCKLKDr8cJbzINSDCdhUbjuZoY"'

                    }, data=json.dumps({
                        "operationName": "WalletBalanceQuery",
                        "variables": {},
                        "query": "query WalletBalanceQuery {\n  me {\n    id\n    gemBalance\n    __typename\n  }\n}\n"
                    }))

                    data = json.loads(resp.content)
                    ballance = data["data"]["me"]["gemBalance"]

                    print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgGreen + "Account Found -> "+username + " -> " + ballance + " Gems" + Reset)
                    time.sleep(3)
                    #await menu()
            except:
                print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Failed To Check Account, May Be Banned!" + Reset)
                time.sleep(3)


