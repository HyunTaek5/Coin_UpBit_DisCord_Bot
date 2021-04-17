import discord
from discord.ext import commands
from core import get_secret
from upBit import balance_check, get_trade_price

token = get_secret("TOKEN_KEY")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} 에 로그인하였습니다!")


@bot.command()
async def 시세(ctx, arg):
    try:
        await ctx.reply(f'{get_trade_price(arg)} KRW')
    except KeyError:
        await ctx.reply('다시 입력하십시오')

bot.run(token)