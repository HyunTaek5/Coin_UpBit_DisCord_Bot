import os
import json
import discord
from discord.ext import commands

secret_file = os.path.join('secrets.json')
with open(secret_file) as f:
    secret = json.loads(f.read())


def get_secret(setting, secrets=secret):
    try:
        return secrets[setting]
    except KeyError:
        print('error!')


token = get_secret("TOKEN_KEY")

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)