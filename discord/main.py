import discord
from discord.ext import commands
from core import get_secret
from upbit.upBit import upbit_get_trade_price, upbit_balance_check

token = get_secret("TOKEN_KEY")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} 에 로그인하였습니다!")


@bot.command()
async def 시세(ctx, arg):
    try:
        await ctx.reply(f'{upbit_get_trade_price(arg)} KRW')
    except KeyError:
        await ctx.reply('다시 입력하십시오')


@bot.command()
async def 투자내역(ctx):
    await ctx.reply(upbit_balance_check())

bot.run(token)