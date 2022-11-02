from pprint import pprint
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordWebhook, DiscordEmbed
import asyncio
from crack_check import checkIfProcessRunning
import json


async def webhook(name, price, rarity, issue):
    await checkIfProcessRunning()
    with open('settings.json') as f:
        data = json.load(f)
        hook = data['info']['webhook_url']
    #user success
    webhook = DiscordWebhook(url=hook)

    embed = DiscordEmbed(title='Succesfully Sniped Market', color='5865F2')
    embed.set_thumbnail(url="https://i.imgur.com/Jk7zjuT.png")
    embed.add_embed_field(name="Module", value="VEVE - Marketplace", inline=False)
    embed.add_embed_field(name="Name", value=name + " #" + issue, inline=False)
    embed.add_embed_field(name="Rarity", value=rarity, inline=False)
    embed.add_embed_field(name="Price", value=price + " Gems", inline=False)
    webhook.add_embed(embed)
    response = webhook.execute()
    
    #priavte success channel
    webhook = DiscordWebhook(url="")

    embed = DiscordEmbed(title='Succesfully Sniped Market', color='5865F2')
    embed.set_thumbnail(url="https://i.imgur.com/Jk7zjuT.png")
    embed.add_embed_field(name="Module", value="VEVE - Marketplace", inline=False)
    embed.add_embed_field(name="Name", value=name + " #" + issue, inline=False)
    embed.add_embed_field(name="Rarity", value=rarity, inline=False)
    embed.add_embed_field(name="Price", value=price + " Gems", inline=False)
    webhook.add_embed(embed)
    response = webhook.execute()



async def reserve_webhook(name, price, type, img):
    await checkIfProcessRunning()
    with open('settings.json') as f:
        data = json.loads(f)
        hook = data['info']['webhook_url']

    webhook = DiscordWebhook(url=hook)

    embed = DiscordEmbed(title='Succesfully Reserved Item', color='5865F2')
    embed.set_thumbnail(url="https://i.imgur.com/Jk7zjuT.png")
    embed.add_embed_field(name="Module", value="VEVE - Drop", inline=False)
    embed.add_embed_field(name="Name", value=name, inline=False)
    embed.add_embed_field(name="Type", value=type, inline=False)
    embed.add_embed_field(name="Price", value=price + " Gems", inline=False)
    embed.set_thumbnail(img)
    webhook.add_embed(embed)
    response = webhook.execute()

    webhook = DiscordWebhook(url="")
    embed = DiscordEmbed(title='Succesfully Reserved Item', color='5865F2')
    embed.set_thumbnail(url="https://i.imgur.com/Jk7zjuT.png")
    embed.add_embed_field(name="Module", value="VEVE - Drop", inline=False)
    embed.add_embed_field(name="Name", value=name, inline=False)
    embed.add_embed_field(name="Type", value=type, inline=False)
    embed.add_embed_field(name="Price", value=price + " Gems", inline=False)
    webhook.add_embed(embed)
    response = webhook.execute()


async def drop_webhook(name, issue, price):
    await checkIfProcessRunning()
    with open('settings.json') as f:
        data = json.loads(f)
        hook = data['info']['webhook_url']

    webhook = DiscordWebhook(url=hook)

    embed = DiscordEmbed(title='Succesfully Reserved Item', color='5865F2')
    embed.set_thumbnail(url="https://i.imgur.com/Jk7zjuT.png")
    embed.add_embed_field(name="Module", value="VEVE - Marketplace", inline=False)
    embed.add_embed_field(name="Name", value=name, inline=False)
    embed.add_embed_field(name="Edition", value="||" + issue + "||", inline=False)
    embed.add_embed_field(name="Price", value=price + " Gems", inline=False)
    webhook.add_embed(embed)
    response = webhook.execute()



async def webhook2(name, price, rarity):
    await checkIfProcessRunning()
    with open('settings.json') as f:
        data = json.load(f)
        hook = data['info']['webhook_url']
    

    webhook = DiscordWebhook(url=hook)

    embed = DiscordEmbed(title='Succesfully Sniped Market', color='5865F2')
    embed.set_thumbnail(url="https://i.imgur.com/Jk7zjuT.png")
    embed.add_embed_field(name="Module", value="VEVE - Marketplace", inline=False)
    embed.add_embed_field(name="Name", value=name , inline=False)
    embed.add_embed_field(name="Rarity", value=rarity, inline=False)
    embed.add_embed_field(name="Price", value=price + " Gems", inline=False)
    webhook.add_embed(embed)
    response = webhook.execute()

    

async def drop_webhook(name, issue, price):
    await checkIfProcessRunning()
    with open('settings.json') as f:
        data = json.loads(f)
        hook = data['info']['webhook_url']

    webhook = DiscordWebhook(url=hook)

    embed = DiscordEmbed(title='Succesfully Reserved Item', color='5865F2')
    embed.set_thumbnail(url="https://i.imgur.com/Jk7zjuT.png")
    embed.add_embed_field(name="Module", value="VEVE - Marketplace", inline=False)
    embed.add_embed_field(name="Name", value=name, inline=False)
    embed.add_embed_field(name="Edition", value="||" + issue + "||", inline=False)
    embed.add_embed_field(name="Price", value=price + " Gems", inline=False)
    webhook.add_embed(embed)
    response = webhook.execute()
