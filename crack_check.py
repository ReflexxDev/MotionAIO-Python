import os
from art import *
import http.cookies
from pypresence import Presence
import brotli
from loguru import logger
from requests_futures.sessions import FuturesSession
import re
from unicodedata import name
import requests
import json
import asyncio
from datetime import datetime
from datetime import datetime
import time
from wsgiref import headers
import urllib3
import random
import psutil
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordWebhook, DiscordEmbed


FgBlack = "\x1b[30m"
FgRed = "\x1b[31m"
FgGreen = "\x1b[32m"
FgYellow = "\x1b[33m"
FgBlue = "\x1b[34m"
FgMagenta = "\x1b[35m"
FgCyan = "\x1b[36m"
FgWhite = "\x1b[37m"
Reset = "\x1b[0m"


async def checkIfProcessRunning():
    with open("settings.json") as f:
        data = json.load(f)
        key = data["info"]["key"]

    process_name = ['dnspy', 'httpdebuggersvc', 'fiddler', 'charles', 'wireshark', 'dragonfly', 'httpwatch', 'burpsuite', 'hxd', 'http toolkit', 'glasswire']

    for proc in psutil.process_iter():
        try:
            for i in process_name:
                if i.lower() in proc.name().lower():
                    webhook = DiscordWebhook(
                        url='')

                    embed = DiscordEmbed(
                        title='Cracker Detected', color='5865F2')
                    embed.set_thumbnail(url="https://i.imgur.com/Jk7zjuT.png")
                    embed.add_embed_field(
                        name="Process", value=i, inline=False)
                    embed.add_embed_field(name="Key", value=key, inline=False)

                    webhook.add_embed(embed)
                    response = webhook.execute()
                    print("[" + str(datetime.now()) + "]" + " " + "|" +
                          " " + FgRed + "Cracking Tool Detected!" + Reset)

                    print("[" + str(datetime.now()) + "]" + " " + "|" +
                          " " + FgRed + "Exiting In 10 Seconds" + Reset)
                    time.sleep(10)
                    exit()

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False
