#proxy scrapper 
import discord
from discord.ext import commands
import discum
import os
import requests
import asyncio
import random
import codecs

token = ""

prefix = "-"
os.system('clear')

client = commands.Bot(command_prefix=prefix, self_bot = True)

intents = discord.Intents.all()
intents.members = True

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"



@client.event
async def on_ready():
  print(f"Successfully Logged Into {client.user}")




@client.command(aliases=["proxygen",])
async def proxies(ctx, type):
        if type == "http":
            if not os.path.isdir("data/proxies/"): os.makedirs("data/proxies/");
            file = open("data/proxies/http.txt", "a+")
            request = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000")
            proxies = []
            for proxy in request.text.split("\n"):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
                    file.write(str(proxy)+"\n")
            file.close()
            await ctx.send(content=f"Successfully Scraped `{len(proxies)}` HTTP proxies.", file=discord.File("data/proxies/http.txt"))

        if type == "https":
            if not os.path.isdir("data/proxies/"): os.makedirs("data/proxies/");
            file = open("data/proxies/https.txt", "a+")
            request = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=5000")
            proxies = []
            for proxy in request.text.split("\n"):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
                    file.write(str(proxy)+"\n")
            file.close()
            await ctx.send(content=f"Successfully Scraped`{len(proxies)}` HTTPS proxies.", file=discord.File("data/proxies/https.txt"))  

        if type == "socks4":
            if not os.path.isdir("data/proxies/"): os.makedirs("data/proxies/");
            file = open("data/proxies/socks4.txt", "a+")
            request = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=5000")
            proxies = []
            for proxy in request.text.split("\n"):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
                    file.write(str(proxy)+"\n")
            file.close()
            await ctx.send(content=f"Successfully Scraped `{len(proxies)}` SOCKS4 proxies.", file=discord.File("data/proxies/socks4.txt"))   

        if type == "socks5":
            if not os.path.isdir("data/proxies/"): os.makedirs("data/proxies/");
            file = open("data/proxies/socks5.txt", "a+")
            request = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000")
            proxies = []
            for proxy in request.text.split("\n"):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
                    file.write(str(proxy)+"\n")
            file.close()
            await ctx.send(content=f"Successfully Scraped `{len(proxies)}` SOCKS5 proxies.", file=discord.File("data/proxies/socks5.txt"))

        if type == "all":
            if not os.path.isdir("data/proxies/"): os.makedirs("data/proxies/");
            file = open("data/proxies/all.txt", "a+")
            request = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=5000")
            proxies = []
            for proxy in request.text.split("\n"):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
                    file.write(str(proxy)+"\n")
            file.close()
            await ctx.send(content=f"Successfully Scraped `{len(proxies)}` HTTP, HTTPS, SOCKS4 AND SOCKS5 proxies.", file=discord.File("data/proxies/all.txt"))  



client.run(token, bot=False)