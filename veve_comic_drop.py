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
from webhook import reserve_webhook
from datetime import datetime
from datetime import datetime
import time
from wsgiref import headers
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordWebhook, DiscordEmbed
import urllib3
import random
from crack_check import checkIfProcessRunning
from capmonster_python import HCaptchaTask
import threading
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


cookies = []
with open("cookies.txt", 'r') as f:
    for i in f:
        i.replace("\n", "")
        cookies.append(i)

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


async def get_latest_drop():
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

    session.get('https://mobile.api.prod.veve.me/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp')

    resp = session.post("https://mobile.api.prod.veve.me/graphql", headers={
        'client-operation': 'StoreDigitalComics',
        'accept': '*/*',
        'connection': 'Keep-Alive',
        'content-type': 'application/json',
        'cookie': session_cookie

    }, data=json.dumps({
        "operationName": "StoreDigitalComics",
        "variables": {},
        "query": "query StoreDigitalComics($cursor: String) {\n  comicTypeList(first: 1, after: $cursor) {\n    pageInfo {\n      hasNextPage\n      endCursor\n      __typename\n    }\n    totalCount\n    edges {\n      node {\n        id\n        name\n        storePrice\n        totalOwnedComicsByUser\n        totalAvailable\n        totalIssued\n        description\n        comicNumber\n        startYear\n        cover {\n          id\n          image {\n            id\n            url\n            direction\n            __typename\n          }\n          __typename\n        }\n        artists(first: 20) {\n          totalCount\n          edges {\n            node {\n              id\n              name\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        writers(first: 20) {\n          totalCount\n          edges {\n            node {\n              id\n              name\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }))

    try:
        data = json.loads(resp.content)
        comic_id = data["data"]["comicTypeList"]["edges"][0]["node"]["id"]
        name = data["data"]["comicTypeList"]["edges"][0]["node"]["name"]
    except:
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Failed To Fetch Data" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Exiting In 10 Seconds" + Reset)
        time.sleep(10)
        exit()
    

    print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " Is " + "'" + name + " The Comic You Wish To Mint? (Y/N)" + Reset)
    confirm_input = input("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgCyan + "> " + Reset)

    if confirm_input == "Y":
        await get_drop(comic_id)
    elif confirm_input == "y":
        await get_drop(comic_id)
    else:
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Exiting In 10 Seconds" + Reset)
        time.sleep(10)
        exit()


async def get_drop(comic_id):
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

    resp = session.post("https://mobile.api.prod.veve.me/graphql", headers={
        'client-operation': 'ComicQuery',
        'accept': '*/*',
        'connection': 'Keep-Alive',
        'content-type': 'application/json',
        'cookie': session_cookie

    }, data=json.dumps({
        "operationName": "ComicQuery",
        "variables": {
            "comicTypeId": comic_id,
            "hasListing": False,
            "marketListingId": "",
            "comicId": "",
            "hasComicId": False,
            "marketEnabled": False
        },
        "query": "fragment Comic on ComicType {\n  id\n  name\n  description\n  totalIssued\n  totalAvailable\n  totalStoreAllocation\n  storePrice\n  availableReservations\n  pendingStorePurchasesForUser\n  availableForStorePurchase\n  unableToStorePurchaseReason\n  storeCurrencyType\n  isUnlimited\n  isFree\n  timeUntilDropDate\n  covers(first: 5) {\n    edges {\n      node {\n        id\n        rarity\n        totalIssued\n        totalAvailable\n        totalStoreAllocation\n        image {\n          id\n          url\n          type\n          direction\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    totalCount\n    __typename\n  }\n  totalOwnedComicsByUser\n  totalLikes\n  likedByUser\n  bookmarkedByUser\n  totalComments\n  comicNumber\n  pageCount\n  startYear\n  minimumAge\n  cover {\n    id\n    rarity\n    image {\n      id\n      url\n      type\n      direction\n      __typename\n    }\n    __typename\n  }\n  artists(first: 10) {\n    totalCount\n    edges {\n      node {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    totalCount\n    __typename\n  }\n  writers(first: 10) {\n    totalCount\n    edges {\n      node {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  characters(first: 10) {\n    totalCount\n    edges {\n      node {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  comicSeries {\n    id\n    name\n    publisher {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nquery ComicQuery($comicTypeId: ID!, $hasListing: Boolean!, $marketListingId: ID!, $comicId: ID!, $hasComicId: Boolean!, $marketEnabled: Boolean!) {\n  comicType(id: $comicTypeId) {\n    ...Comic\n    __typename\n  }\n  comic(id: $comicId) @include(if: $hasComicId) @skip(if: $hasListing) {\n    id\n    ownedByUser\n    issueNumber\n    openMarketListingId @include(if: $marketEnabled)\n    readingStatus\n    transactions {\n      edges {\n        node {\n          id\n          createdAt\n          amountGem\n          feeGem\n          amountUsd\n          buyer {\n            id\n            username\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    cover {\n      id\n      rarity\n      floorMarketPrice\n      totalMarketListings\n      totalOwnedComicsByUser\n      image {\n        id\n        url\n        type\n        direction\n        __typename\n      }\n      totalIssued\n      artists(first: 10) {\n        totalCount\n        edges {\n          node {\n            id\n            name\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  marketListing(id: $marketListingId) @include(if: $hasListing) {\n    id\n    createdAt\n    status\n    listingType\n    endingAt\n    price: currentPrice\n    currentPrice\n    userBidPosition\n    seller {\n      id\n      username\n      __typename\n    }\n    marketMetadata {\n      totalMarketListings\n      __typename\n    }\n    bids(first: 1) {\n      totalCount\n      edges {\n        node {\n          id\n          createdAt\n          price\n          status\n          bidder {\n            id\n            username\n            avatar {\n              id\n              url\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    element {\n      ... on Comic {\n        id\n        issueNumber\n        ownedByUser\n        readingStatus\n        openMarketListingId @include(if: $marketEnabled)\n        cover {\n          id\n          rarity\n          image {\n            id\n            url\n            type\n            direction\n            __typename\n          }\n          totalIssued\n          totalMarketListings\n          floorMarketPrice\n          totalOwnedComicsByUser\n          artists(first: 10) {\n            edges {\n              node {\n                id\n                name\n                __typename\n              }\n              __typename\n            }\n            totalCount\n            __typename\n          }\n          __typename\n        }\n        transactions {\n          edges {\n            node {\n              id\n              createdAt\n              amountGem\n              feeGem\n              amountUsd\n              buyer {\n                id\n                username\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }))

    try:
        data = json.loads(resp.content)
        cover_img = data["data"]["comicType"]["cover"]["image"]["url"]
        comic_number = data["data"]["comicType"]["comicNumber"]
        comic_type_id = data["data"]["comicType"]["id"]
        dropTime = int(data["data"]["comicType"]["timeUntilDropDate"])
    except:
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Failed To Fetch Data" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Exiting In 10 Seconds" + Reset)
        time.sleep(10)
        exit()

    print("[" + str(datetime.now()) + "]" + " " + "|" + FgCyan + " Waiting " + "For " + "'" + data["data"]["comicType"]["name"] + " #" + comic_number + "'" + " To Drop!" + Reset)


    while dropTime >= 10:
        time.sleep(0.3)

        try:
            session.proxies = formated_proxies[random.randrange(0,len(formated_proxies))]
        except:
            print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " " + "Proxy Banned, Rotating...  " + Reset)
            session.proxies = formated_proxies[random.randrange(0,len(formated_proxies))]

        resp = session.post("https://mobile.api.prod.veve.me/graphql", headers={
            'client-operation': 'ComicQuery',
            'accept': '*/*',
            'connection': 'Keep-Alive',
            'content-type': 'application/json',
            'cookie': session_cookie

        }, data=json.dumps({
            "operationName": "ComicQuery",
            "variables": {
                "comicTypeId": comic_id,
                "hasListing": False,
                "marketListingId": "",
                "comicId": "",
                "hasComicId": False,
                "marketEnabled": False
            },
            "query": "fragment Comic on ComicType {\n  id\n  name\n  description\n  totalIssued\n  totalAvailable\n  totalStoreAllocation\n  storePrice\n  availableReservations\n  pendingStorePurchasesForUser\n  availableForStorePurchase\n  unableToStorePurchaseReason\n  storeCurrencyType\n  isUnlimited\n  isFree\n  timeUntilDropDate\n  covers(first: 5) {\n    edges {\n      node {\n        id\n        rarity\n        totalIssued\n        totalAvailable\n        totalStoreAllocation\n        image {\n          id\n          url\n          type\n          direction\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    totalCount\n    __typename\n  }\n  totalOwnedComicsByUser\n  totalLikes\n  likedByUser\n  bookmarkedByUser\n  totalComments\n  comicNumber\n  pageCount\n  startYear\n  minimumAge\n  cover {\n    id\n    rarity\n    image {\n      id\n      url\n      type\n      direction\n      __typename\n    }\n    __typename\n  }\n  artists(first: 10) {\n    totalCount\n    edges {\n      node {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    totalCount\n    __typename\n  }\n  writers(first: 10) {\n    totalCount\n    edges {\n      node {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  characters(first: 10) {\n    totalCount\n    edges {\n      node {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  comicSeries {\n    id\n    name\n    publisher {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nquery ComicQuery($comicTypeId: ID!, $hasListing: Boolean!, $marketListingId: ID!, $comicId: ID!, $hasComicId: Boolean!, $marketEnabled: Boolean!) {\n  comicType(id: $comicTypeId) {\n    ...Comic\n    __typename\n  }\n  comic(id: $comicId) @include(if: $hasComicId) @skip(if: $hasListing) {\n    id\n    ownedByUser\n    issueNumber\n    openMarketListingId @include(if: $marketEnabled)\n    readingStatus\n    transactions {\n      edges {\n        node {\n          id\n          createdAt\n          amountGem\n          feeGem\n          amountUsd\n          buyer {\n            id\n            username\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    cover {\n      id\n      rarity\n      floorMarketPrice\n      totalMarketListings\n      totalOwnedComicsByUser\n      image {\n        id\n        url\n        type\n        direction\n        __typename\n      }\n      totalIssued\n      artists(first: 10) {\n        totalCount\n        edges {\n          node {\n            id\n            name\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  marketListing(id: $marketListingId) @include(if: $hasListing) {\n    id\n    createdAt\n    status\n    listingType\n    endingAt\n    price: currentPrice\n    currentPrice\n    userBidPosition\n    seller {\n      id\n      username\n      __typename\n    }\n    marketMetadata {\n      totalMarketListings\n      __typename\n    }\n    bids(first: 1) {\n      totalCount\n      edges {\n        node {\n          id\n          createdAt\n          price\n          status\n          bidder {\n            id\n            username\n            avatar {\n              id\n              url\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    element {\n      ... on Comic {\n        id\n        issueNumber\n        ownedByUser\n        readingStatus\n        openMarketListingId @include(if: $marketEnabled)\n        cover {\n          id\n          rarity\n          image {\n            id\n            url\n            type\n            direction\n            __typename\n          }\n          totalIssued\n          totalMarketListings\n          floorMarketPrice\n          totalOwnedComicsByUser\n          artists(first: 10) {\n            edges {\n              node {\n                id\n                name\n                __typename\n              }\n              __typename\n            }\n            totalCount\n            __typename\n          }\n          __typename\n        }\n        transactions {\n          edges {\n            node {\n              id\n              createdAt\n              amountGem\n              feeGem\n              amountUsd\n              buyer {\n                id\n                username\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
        }))

        try:
            data = json.loads(resp.content)
            comic_type_id = data["data"]["comicType"]["id"]
            dropTime = int(data["data"]["comicType"]["timeUntilDropDate"])
        except:
            print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Failed To Fetch Data, Retrying..." + Reset)
            await get_drop(comic_id)
    cont=0
    while cont <= len(cookies)-1:
        x = threading.Thread(target=test1, args=(comic_type_id,cover_img,cont))
        x.start()
        cont=cont+1

def test1(a,b,c):
    #The Thread function cant be an async function 
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(reserve_comic(a,b,c))
    loop.close()
    
    


async def reserve_comic(comic_type_id, img_url,c):
    print("[" + str(datetime.now()) + "]" + " " + "|" + FgYellow + " Attempting To Reserve Comic..." + Reset)
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

    resp = session.post("https://mobile.api.prod.veve.me/graphql", headers={
        'client-operation': 'PlaceStoreReservation',
        'accept': '*/*',
        'connection': 'Keep-Alive',
        'content-type': 'application/json',
        'cookie': cookies[c]

    }, data=json.dumps({
        "operationName": "PlaceStoreReservation",
        "variables": {
            "id": comic_type_id
        },
        "query": "mutation PlaceStoreReservation($id: ID!) {\n  placeStoreReservation(elementId: $id) {\n    element {\n      availableReservations\n      id\n      isFree\n      isUnlimited\n      storePrice\n      totalAvailable\n      totalIssued\n      ... on ComicType {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    expiresAt\n    id\n    issueNumber\n    status\n    __typename\n  }\n}\n"
    }))

    print(resp.content)
    time.sleep(1)

    try:
        data = json.loads(resp.content)
    except:
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Failed To Fetch Data, Retrying..." + Reset)
        await reserve_comic(comic_type_id, img_url)

    try:
        if data["errors"]:
            if data["errors"][0]["message"] == "There are no available store purchase reservations for this element":
                print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Unable To Reserve Item" + Reset)
                time.sleep(0.7)
                await reserve_comic(comic_type_id, img_url)

            if data["errors"][0]["message"] == "Store element has sold out":
                print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Item Already Sold Out" + Reset)
                
                
    except:
        if data["data"]:
            if data["data"]["placeStoreReservation"]["status"] == "RESERVED":
                reservation_id = data["data"]["placeStoreReservation"]["element"]["id"]
                name = data["data"]["placeStoreReservation"]["element"]["name"]
                price = data["data"]["placeStoreReservation"]["element"]["storePrice"]
                print("[" + str(datetime.now()) + "]" + " " + "|" + FgGreen + " Sucesfully Reserved " + "'" + name + "'" + Reset)
                await reserve_webhook(name, price, "COMIC", img_url)
                await comic_checkout(reservation_id,c)



async def comic_checkout(reservation_id,c):
    print("[" + str(datetime.now()) + "]" + " " + "|" + FgYellow + " Attempting To Solve Captcha..." + Reset)

    try:
        captcha = HCaptchaTask(client_key="") #Enter new hcaptcha solving token here
        task_id = captcha.create_task("https://mobile.api.prod.veve.me/graphql", "86c60170-2a73-489f-89ad-fca627914423")
        cap_response = captcha.join_task_result(task_id)

        if cap_response != "":
            cap_code = cap_response["gRecaptchaResponse"]
        else:
            print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Failed To Solve Captcha, Retrying..." + Reset)
            await comic_checkout(reservation_id)
    
    except:
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Failed To Solve Captcha, Retrying..." + Reset)
        await comic_checkout(reservation_id)


    print("[" + str(datetime.now()) + "]" + " " + "|" + FgYellow + " Submitting Checkout..." + Reset)
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

    resp = session.post("https://mobile.api.prod.veve.me/graphql", headers={
        'client-operation': 'StorePurchase',
        'accept': '*/*',
        'connection': 'Keep-Alive',
        'content-type': 'application/json',
        'cookie': cookies[c]

    }, data=json.dumps({
        "operationName": "StorePurchase",
        "variables": {
            "id": reservation_id,
            "captchaCode": cap_code,
            "captchaSiteKey": "86c60170-2a73-489f-89ad-fca627914423"
        },
        "query": "mutation StorePurchase($id: ID!, $captchaCode: String!, $captchaSiteKey: String!) {\n  storePurchase(\n    elementId: $id\n    captchaCode: $captchaCode\n    captchaSiteKey: $captchaSiteKey\n  ) {\n    id\n    status\n    buyer {\n      gemBalance\n      __typename\n    }\n    __typename\n  }\n}\n"
    }))

    try:
        data = json.loads(resp.content)
        print(data)
        #purchase_id = data["data"]["storePurchase"]["id"]
    except:
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Failed To Fetch Data" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Exiting In 10 Seconds" + Reset)
        time.sleep(10)
        exit()
    
    if data["data"]["storePurchase"]["status"] == "PENDING":
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgGreen + " Succesfully Submited Order, Check Pending Deliveries" + Reset)
        time.sleep(10)
        exit()
    else:
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Failed To Submit Order" + Reset)
        print("[" + str(datetime.now()) + "]" + " " + "|" + FgRed + " Exiting In 10 Seconds" + Reset)
        time.sleep(10)
        exit()        

        