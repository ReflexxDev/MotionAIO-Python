from webhook import webhook2
import os
from art import *
import http.cookies
import sys
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
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordWebhook, DiscordEmbed
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


name = ""
issue_number = ""
rarity = ""

helheim.auth('8a4111e9-52b6-46eb-bbb8-c426b3bde831')


def now_time_ms():
    return int(datetime.now().timestamp() * 1000)


with open("cookies.txt", 'r') as f:
    session_cookie = f.readline()

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

async def get_collectable(name1, rarity1, ignore, c):
    helheim.wokou(session)

    session.headers = OrderedDict([
        ('Content-Length', None),
        ('Pragma', 'no-cache'),
        ('Cache-Control', 'no-cache,no-store'),
        ('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'),
        ('Accept', 'application/json, text/plain, */*'),
        ('Accept-Encoding', 'gzip, deflate'),
        ('Accept-Language', 'en-us'),
        ('client-name', 'veve-app-ios'),
        ('client-model', 'iphone 7'),
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

    resp = session.post("https://mobile.api.prod.veve.me/graphql", headers={
        'authority': 'mobile.api.prod.veve.me',
        'client-version': '1.0.583',
        'cookie': session_cookie,
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

    }, data=json.dumps({
        "operationName": "MarketBrowseQuery",
        "variables": {
            "sortOptions": {
                "sortBy": "CREATED_AT",
                "sortDirection": "DESCENDING"
            },
            "filterOptions": {
                "status": [
                    "OPEN"
                ],
                "onePerCollectibleType": True,
                "hashtags": []
            }
        },
        "query": "query MarketBrowseQuery($cursor: String, $sortOptions: MarketListingSort!, $filterOptions: MarketListingFilter) {\n  marketListingList(\n    first: 200\n    after: $cursor\n    sortOptions: $sortOptions\n    filterOptions: $filterOptions\n  ) {\n    pageInfo {\n      hasNextPage\n      endCursor\n      __typename\n    }\n    edges {\n      node {\n        ...MarketBaseItem\n        marketMetadata {\n          totalMarketListings\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment MarketBaseItem on MarketListing {\n  id\n  endingAt\n  seller {\n    id\n    __typename\n  }\n  listingType\n  status\n  userBidPosition\n  currentPrice\n  bids(first: 1) {\n    totalCount\n    edges {\n      node {\n        id\n        status\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  element {\n    ... on Collectible {\n      id\n      formattedIssueNumber\n      ownedByUser\n      collectibleType {\n        id\n        name\n        rarity\n        totalIssued\n        totalAvailable\n        image {\n          id\n          url\n          direction\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
    }))

    data = json.loads(resp.content)
    try:
        
        for i in range(205):
            if data["data"]["marketListingList"]["edges"][i]["node"]["element"]['collectibleType']['name'] != ignore and name1 in data["data"]["marketListingList"]["edges"][i]["node"]["element"]['collectibleType']['name']:
                if rarity1 == data["data"]["marketListingList"]["edges"][i]["node"]["element"]['collectibleType']["rarity"]:
                    rarity = data["data"]["marketListingList"]["edges"][i]["node"]["element"]['collectibleType']["rarity"]
                    Collectable_id = data["data"]["marketListingList"]["edges"][i]["node"]["element"]['collectibleType']["id"]
                    name = data["data"]["marketListingList"]["edges"][i]["node"]["element"]['collectibleType']['name']

    except:
        a = 1
    try:
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " Is " + "'" +
              name + ", " + rarity + "' " + "The Collectable You Wish To Snipe? (Y/N)" + Reset)
    except:
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed +
              " Failed To Get Collectable Please Try Again" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" +
              FgRed + " Exiting In 10 Seconds" + Reset)
        time.sleep(10)
        exit()

    confirmation_input = input(
        "[" + str(datetime.now()) + "]" + " " + "|" + " " + FgCyan + "> " + Reset)

    if confirmation_input.upper() == "Y" or confirmation_input.upper() == "YES":
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan +
          " " + "Enter The Price You Wish To Snipe At " + Reset)
        snipe_price = input("[" + str(datetime.now()) + "]" +
                        " " + "|" + FgCyan + " " + "> " + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan +
            " " + "Enter The Maximum Mint Number You Wish To Snipe At, Will Also Snipe For Under " + Reset)
        max_mint = input("[" + str(datetime.now()) + "]" +
                            " " + "|" + FgCyan + " " + "> " + Reset)
        if max_mint == "":
            max_mint = 30000

        print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan +
            " Please Enter A Monitor Delay (eg 0.1, 0.2, 0.3)" + Reset)
        delay_input = input("[" + str(datetime.now()) + "]" +
                            " " + "|" + FgCyan + " > " + Reset)#

        print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " Monitoring " + "'" + name + "' " + "For Price Of " + snipe_price + " Gems" + Reset)

        await get_market_listing(Collectable_id, name, rarity,snipe_price,delay_input,max_mint)
    elif confirmation_input == "N" or confirmation_input == "n" or confirmation_input == "No" or confirmation_input == "NO" or confirmation_input == "nO":
        if c == 1:
            print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed +
                  " Please Re Run The Bot And Try Again" + Reset)
            print("[" + str(datetime.now()) + "]" + " " + "|" +
                  FgRed + " Exiting In 10 Seconds" + Reset)
            time.sleep(10)
            exit()
        else:
            await get_collectable(name1, rarity1, name, c+1)

async def get_market_listing(Collectable_id, name, rarity,snipe_price,delay_input,max_mint):
    time.sleep(float(delay_input))

    helheim.wokou(session)

    session.headers = OrderedDict([
        ('Content-Length', None),
        ('Pragma', 'no-cache'),
        ('Cache-Control', 'no-cache,no-store'),
        ('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'),
        ('Accept', 'application/json, text/plain, */*'),
        ('Accept-Encoding', 'gzip, deflate'),
        ('Accept-Language', 'en-us'),
        ('client-name', 'veve-app-ios'),
        ('client-model', 'iphone 7'),
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


    resp = session.post("https://mobile.api.prod.veve.me/graphql", headers={
        'authority': 'mobile.api.prod.veve.me',
        'client-version': '1.0.583',
        'cookie': session_cookie,
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'client-operation': 'MarketProductMultiplesQuery',
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
        "operationName": "MarketMultiplesQuery",
        "variables": {
            "filterOptions": {
                "collectibleTypeId": Collectable_id,
                "status": [
                    "OPEN"
                ],
                "type": "FIXED"
            },
            "sortOptions": {
                "sortBy": "PRICE",
                "sortDirection": "ASCENDING"
            },

        },
        "query": "query MarketMultiplesQuery($filterOptions: MarketListingFilter, $sortOptions: MarketListingSort!, $cursor: String) {\n  marketListingList(\n    first: 1\n    after: $cursor\n    filterOptions: $filterOptions\n    sortOptions: $sortOptions\n  ) {\n    pageInfo {\n      endCursor\n      hasNextPage\n      __typename\n    }\n    edges {\n      node {\n        id\n        endingAt\n        listingType\n        userBidPosition\n        bids {\n          totalCount\n          __typename\n        }\n        currentPrice\n        seller {\n          id\n          username\n          avatar {\n            id\n            url\n            medResolutionUrl\n            __typename\n          }\n          __typename\n        }\n        element {\n          ... on Collectible {\n            id\n            issueNumber\n            collectibleType {\n              id\n              totalIssued\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }))
    
    data = json.loads(resp.content)
        
    while float(data["data"]["marketListingList"]["edges"][0]["node"]["currentPrice"]) >= float(snipe_price):
        time.sleep(float(delay_input))

        try:
            resp = session.post("https://mobile.api.prod.veve.me/graphql", headers={
            'authority': 'mobile.api.prod.veve.me',
            'client-version': '1.0.583',
            'cookie': session_cookie,
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'client-operation': 'MarketProductMultiplesQuery',
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
                "operationName": "MarketMultiplesQuery",
                "variables": {
                    "filterOptions": {
                        "collectibleTypeId": Collectable_id,
                        "status": [
                            "OPEN"
                        ],
                        "type": "FIXED"
                    },
                    "sortOptions": {
                        "sortBy": "PRICE",
                        "sortDirection": "ASCENDING"
                    },

                },
                "query": "query MarketMultiplesQuery($filterOptions: MarketListingFilter, $sortOptions: MarketListingSort!, $cursor: String) {\n  marketListingList(\n    first: 5\n    after: $cursor\n    filterOptions: $filterOptions\n    sortOptions: $sortOptions\n  ) {\n    pageInfo {\n      endCursor\n      hasNextPage\n      __typename\n    }\n    edges {\n      node {\n        id\n        endingAt\n        listingType\n        userBidPosition\n        bids {\n          totalCount\n          __typename\n        }\n        currentPrice\n        seller {\n          id\n          username\n          avatar {\n            id\n            url\n            medResolutionUrl\n            __typename\n          }\n          __typename\n        }\n        element {\n          ... on Collectible {\n            id\n            issueNumber\n            collectibleType {\n              id\n              totalIssued\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
            }))
            try:
                data = json.loads(resp.content)
            except:
                a=1     
        except:
            print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " " + "Proxy Banned, Rotating...  " + Reset)
            time.sleep(1.5)
            get_market_listing(Collectable_id, name, rarity,snipe_price,delay_input,max_mint)
            

    if int(data["data"]["marketListingList"]["edges"][0]["node"]['element']['issueNumber'])  <=int(max_mint):
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " Found " + "'" + name + "' " +
            "For Price Of " + data["data"]["marketListingList"]["edges"][0]["node"]["currentPrice"] + " Gems" + Reset)
        checkout_id = data["data"]["marketListingList"]["edges"][0]["node"]["id"]
        price = data["data"]["marketListingList"]["edges"][0]["node"]["currentPrice"]
        await market_checkout(checkout_id, name, rarity, price)
    else:
        await get_market_listing(Collectable_id, name, rarity,snipe_price,delay_input,max_mint)


async def market_checkout(checkout_id, name, rarity, price):
    price = str(price)
    helheim.wokou(session)
    try:
        print("[" + str(datetime.now()) + "]" + " " + "|" +
              FgYellow + " Attempting To Snipe..." + Reset)

        session.headers = OrderedDict([
            ('Content-Length', None),
            ('Pragma', 'no-cache'),
            ('Cache-Control', 'no-cache,no-store'),
            ('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'),
            ('Accept', 'application/json, text/plain, */*'),
            ('Accept-Encoding', 'gzip, deflate'),
            ('Accept-Language', 'en-us'),
            ('client-name', 'veve-app-ios'),
            ('client-model', 'iphone 7'),
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


        resp = session.post("https://mobile.api.prod.veve.me/graphql", headers={
            'client-operation': 'PurchaseWalletMutation',
            'cookie': session_cookie,
            'accept': '*/*',
            'content-type': 'application/json',

        }, data=json.dumps({
            "operationName": "PurchaseWalletMutation",
            "variables": {
                "id": checkout_id
            },
            "query": "mutation PurchaseWalletMutation($id: ID!) {\n  marketPurchase(marketListingId: $id) {\n    id\n    buyer {\n      gemBalance\n      __typename\n    }\n    collectibles {\n      formattedIssueNumber\n      __typename\n    }\n    __typename\n  }\n}\n"
        }))

        data = json.loads(resp.content)
    except:
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed +
              " Unable To Snipe " + "'" + name + "'" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan +
              " " + "Enter The Name Of The Collectible " + Reset)
        name = input("[" + str(datetime.now()) + "]" +
                     " " + "|" + FgCyan + " " + "> " + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" +
              FgCyan + " " + "Enter The Rarity " + Reset)
        rarity = input("[" + str(datetime.now()) + "]" +
                       " " + "|" + FgCyan + " " + "> " + Reset)
        await get_collectable(name, rarity, '', 0)

    try:
        if data["errors"][0]["message"] == "Insufficient funds":
            print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed +
                  " Unable To Snipe " + "'" + name + "'" + Reset)

            print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan +
                  " " + "Enter The Name Of The Collectible " + Reset)
            name = input("[" + str(datetime.now()) + "]" +
                         " " + "|" + FgCyan + " " + "> " + Reset)
            print("[" + str(datetime.now()) + "]" + " " + "|" +
                  FgCyan + " " + "Enter The Rarity " + Reset)
            rarity = input("[" + str(datetime.now()) + "]" +
                           " " + "|" + FgCyan + " " + "> " + Reset)
            await get_collectable(name, rarity, '', 0)

    except:
        try:
            if data["data"]["marketPurchase"]:
                await webhook2(name, price, rarity)
                print("[" + str(datetime.now()) + "]" + " " + "|" + FgGreen +
                      " Succesfully Sniped " + "'" + name + "'" + Reset)
                print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan +
                      " " + "Enter The Name Of The Collectible " + Reset)
                name = input("[" + str(datetime.now()) + "]" +
                             " " + "|" + FgCyan + " " + "> " + Reset)
                print("[" + str(datetime.now()) + "]" + " " + "|" +
                      FgCyan + " " + "Enter The Rarity " + Reset)
                rarity = input("[" + str(datetime.now()) + "]" +
                               " " + "|" + FgCyan + " " + "> " + Reset)
                await get_collectable(name, rarity, '', 0)
        except:
            a = 1
